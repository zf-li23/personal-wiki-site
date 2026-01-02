import { useEffect, useState, useRef } from 'react';

interface PythonPlotBlockProps {
  code: string;
}

declare global {
  interface Window {
    loadPyodide: any;
    pyodide: any;
  }
}

// Global queue to serialize Pyodide execution across all component instances
const queueKey = '__pyodide_execution_queue__';
if (!(window as any)[queueKey]) {
    (window as any)[queueKey] = Promise.resolve();
}

export default function PythonPlotBlock({ code }: PythonPlotBlockProps) {
  const [showCode, setShowCode] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [output, setOutput] = useState<string>('');
  const [plotImage, setPlotImage] = useState<string>('');
  const [error, setError] = useState('');
  const [isPyodideLoaded, setIsPyodideLoaded] = useState(false);
  const hasRunRef = useRef(false);

  // Check if Pyodide script is already added
  useEffect(() => {
    const scriptId = 'pyodide-script';
    const existingScript = document.getElementById(scriptId) as HTMLScriptElement;

    if (!existingScript) {
      const script = document.createElement('script');
      script.id = scriptId;
      script.src = 'https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js';
      script.onload = () => setIsPyodideLoaded(true);
      document.body.appendChild(script);
    } else {
      if (window.loadPyodide) {
        setIsPyodideLoaded(true);
      } else {
        // Script exists but not loaded, wait for it
        existingScript.addEventListener('load', () => setIsPyodideLoaded(true));
      }
    }
  }, []);

  const runPython = async () => {
    if (!isPyodideLoaded) return;
    
    setIsLoading(true);
    setError('');
    setOutput('');
    setPlotImage('');

    // Append to global queue
    (window as any)[queueKey] = (window as any)[queueKey].then(async () => {
        try {
            // Initialize Pyodide if needed (only once globally)
            if (!window.pyodide) {
                window.pyodide = await window.loadPyodide();
                await window.pyodide.loadPackage(['matplotlib', 'numpy']);
            }

            const isDark = document.documentElement.classList.contains('dark');

            // Setup matplotlib backend to Agg and set theme
            // We must do this BEFORE every plot to ensure clean state
            await window.pyodide.runPythonAsync(`
                import matplotlib
                matplotlib.use("Agg")
                import matplotlib.pyplot as plt
                import io, base64
                import sys
                
                # Mock plt.show to do nothing (we capture manually)
                # We define it to print a message so we know it was called
                def noop_show(*args, **kwargs):
                    print("Debug: plt.show() called (ignored)")
                plt.show = noop_show

                # Set style based on theme
                if ${isDark ? 'True' : 'False'}:
                    plt.style.use('dark_background')
                else:
                    plt.style.use('default')
                
                # Reset figure explicitly
                plt.clf()
                plt.close('all')
            `);

            // Capture stdout
            window.pyodide.setStdout({ batched: (msg: string) => setOutput(prev => prev + msg + '\n') });

            // Run user code
            console.log("Running user code...");
            await window.pyodide.runPythonAsync(code);

            // Get plot
            const image = await window.pyodide.runPythonAsync(`
                buf = io.BytesIO()
                # Check if any figure exists
                fignums = plt.get_fignums()
                print(f"Debug: Active figures: {fignums}")
                
                if fignums:
                    plt.savefig(buf, format='png', bbox_inches='tight')
                    buf.seek(0)
                    img_str = base64.b64encode(buf.read()).decode('utf-8')
                    plt.close('all')
                    img_str
                else:
                    print("Debug: No figures found to save.")
                    ""
            `);
            
            if (image) {
                setPlotImage(`data:image/png;base64,${image}`);
            }
        } catch (err: any) {
            console.error('Python execution error:', err);
            setError(err.message);
        } finally {
            setIsLoading(false);
        }
    });
  };

  // Auto-run once when visible/loaded
  useEffect(() => {
      if (isPyodideLoaded && !hasRunRef.current) {
          hasRunRef.current = true;
          runPython();
      }
  }, [isPyodideLoaded]);

  // Re-run on theme change
  useEffect(() => {
    const observer = new MutationObserver(() => {
       if (isPyodideLoaded && !isLoading) {
           runPython();
       }
    });
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    return () => observer.disconnect();
  }, [isPyodideLoaded, code]);

  return (
    <div className="my-4 border rounded-lg overflow-hidden bg-card">
      <div className="flex justify-between items-center p-2 bg-muted/30 border-b">
        <span className="text-xs font-mono text-muted-foreground">Python Plot</span>
        <div className="flex gap-2">
            <button
            onClick={runPython}
            disabled={isLoading || !isPyodideLoaded}
            className="text-xs px-2 py-1 rounded bg-green-500/10 hover:bg-green-500/20 text-green-600 transition-colors disabled:opacity-50"
            >
            {isLoading ? 'Running...' : 'Run'}
            </button>
            <button
            onClick={() => setShowCode(!showCode)}
            className="text-xs px-2 py-1 rounded bg-primary/10 hover:bg-primary/20 text-primary transition-colors"
            >
            {showCode ? 'Show Plot' : 'Show Code'}
            </button>
        </div>
      </div>
      
      <div className="p-4 overflow-x-auto flex flex-col items-center bg-white dark:bg-gray-900 transition-colors min-h-[200px] justify-center">
        {showCode ? (
          <pre className="text-sm font-mono whitespace-pre-wrap text-left w-full text-foreground">
            {code}
          </pre>
        ) : (
          <>
            {!isPyodideLoaded && <div className="text-muted-foreground text-sm">Loading Python environment...</div>}
            {isLoading && <div className="text-muted-foreground text-sm animate-pulse">Generating plot...</div>}
            {error && <div className="text-destructive text-sm whitespace-pre-wrap">{error}</div>}
            {plotImage && (
                <img src={plotImage} alt="Python Plot" className="max-w-full rounded shadow-sm" />
            )}
            {output && (
                <pre className="mt-2 w-full text-xs bg-black/5 dark:bg-white/5 p-2 rounded text-foreground">
                    {output}
                </pre>
            )}
          </>
        )}
      </div>
    </div>
  );
}

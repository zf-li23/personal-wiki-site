import { useEffect, useState } from 'react';
import md5 from 'js-md5';

interface PythonPlotBlockProps {
  code: string;
  folderPath?: string; // We'll need this prop
}

export default function PythonPlotBlock({ code, folderPath }: PythonPlotBlockProps) {
  const [showCode, setShowCode] = useState(false);
  const [plotSrc, setPlotSrc] = useState<string>('');
  const [copied, setCopied] = useState(false);
  const [imgError, setImgError] = useState(false);

  // Normalize code for hash calculation: trim whitespace from both ends to match python script's .strip()
  const normalizedCode = code.trim();
  // @ts-ignore
  const codeHash = md5(normalizedCode);

  useEffect(() => {
    // Determine theme on mount and change
    const updateSrc = () => {
        const isDark = document.documentElement.classList.contains('dark');
        const theme = isDark ? 'dark' : 'light';
        // Construct path: base + wiki-content + folderPath + hash + theme + .png
        // import.meta.env.BASE_URL usually includes trailing slash
        const baseUrl = import.meta.env.BASE_URL;
        // folderPath pass logic:
        // MarkdownRenderer passes 'currentPath'. e.g. "1.Discrete/index".
        // The image is next to index.md.
        // So we need to remove "/index" if present or keep folder structure.
        
        // If helper removes "index", we get "1.Discrete".
        // URL needs "1.Discrete/".
        
        let pathPart = folderPath || '';
        if (pathPart.endsWith('/index')) {
            pathPart = pathPart.replace(/\/index$/, '');
        } else if (pathPart === 'index') {
            pathPart = '';
        }
        
        // Ensure pathPart ends with / if not empty
        if (pathPart && !pathPart.endsWith('/')) {
            pathPart += '/';
        }
        
        // Encode path components to handle Chinese characters
        const encodedPathPart = pathPart.split('/').map(segment => encodeURIComponent(segment)).join('/');
        
        const src = `${baseUrl}wiki-content/${encodedPathPart}${codeHash}_${theme}.png?v=2`;
        setPlotSrc(src);
        setImgError(false); // Reset error on source change
    };

    updateSrc();
    
    // Observer for class change on html
    const observer = new MutationObserver(updateSrc);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    return () => observer.disconnect();
  }, [codeHash, folderPath]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code:', err);
    }
  };

  return (
    <div className="my-4 border rounded-lg overflow-hidden bg-card">
      <div className="flex justify-between items-center p-2 bg-muted/30 border-b">
        <span className="text-xs font-mono text-muted-foreground">Python Plot</span>
        <div className="flex gap-2">
            <button
            onClick={handleCopy}
            className="text-xs px-2 py-1 rounded bg-muted/50 hover:bg-muted text-muted-foreground transition-colors"
            title="Copy code"
            >
            {copied ? 'Copied!' : 'Copy'}
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
          <pre className="text-sm font-mono whitespace-pre-wrap text-left w-full bg-gray-50 text-gray-900 dark:bg-gray-950 dark:text-gray-100 p-4 rounded border border-border">
            {code}
          </pre>
        ) : (
          <>
            {!imgError ? (
                <img 
                    src={plotSrc} 
                    alt="Python Plot" 
                    className="max-w-full rounded shadow-sm"
                    onError={() => setImgError(true)}
                />
            ) : (
                <div className="text-muted-foreground text-sm flex flex-col items-center gap-2">
                    <span>⚠️ Plot not available</span>
                    <span className="text-xs opacity-70">Run 'pnpm run build' to generate plots locally.</span>
                </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}

import { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';

interface MermaidBlockProps {
  code: string;
}

export default function MermaidBlock({ code }: MermaidBlockProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [showCode, setShowCode] = useState(false);
  const [svgContent, setSvgContent] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    // Initialize mermaid
    mermaid.initialize({
      startOnLoad: false,
      theme: document.documentElement.classList.contains('dark') ? 'dark' : 'default',
      securityLevel: 'loose',
    });

    const renderDiagram = async () => {
      if (!containerRef.current) return;
      
      try {
        const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
        const { svg } = await mermaid.render(id, code);
        setSvgContent(svg);
        setError('');
      } catch (err) {
        console.error('Mermaid render error:', err);
        setError('Failed to render diagram. Please check syntax.');
      }
    };

    renderDiagram();
    
    // Re-render on theme change
    const observer = new MutationObserver(() => {
       mermaid.initialize({
          theme: document.documentElement.classList.contains('dark') ? 'dark' : 'default',
       });
       renderDiagram();
    });
    
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    
    return () => observer.disconnect();
  }, [code]);

  return (
    <div className="my-4 border rounded-lg overflow-hidden bg-card">
      <div className="flex justify-end p-2 bg-muted/30 border-b">
        <button
          onClick={() => setShowCode(!showCode)}
          className="text-xs px-2 py-1 rounded bg-primary/10 hover:bg-primary/20 text-primary transition-colors"
        >
          {showCode ? 'Show Diagram' : 'Show Source'}
        </button>
      </div>
      
      <div className="p-4 overflow-x-auto flex justify-center bg-white dark:bg-gray-900 transition-colors">
        {showCode ? (
          <pre className="text-sm font-mono whitespace-pre-wrap text-left w-full text-foreground">
            {code}
          </pre>
        ) : (
          <>
            {error ? (
              <div className="text-destructive text-sm">{error}</div>
            ) : (
              <div 
                ref={containerRef}
                dangerouslySetInnerHTML={{ __html: svgContent }} 
                className="mermaid-diagram"
              />
            )}
          </>
        )}
      </div>
    </div>
  );
}

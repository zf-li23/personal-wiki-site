import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeHighlight from 'rehype-highlight';
import rehypeKatex from 'rehype-katex';
import 'highlight.js/styles/github-dark.css';
import 'katex/dist/katex.min.css';
import { useState } from 'react';
import MermaidBlock from './MermaidBlock';
import PythonPlotBlock from './PythonPlotBlock';

interface MarkdownRendererProps {
  content: string;
  currentPath?: string; // e.g. "1.DiscreteMath/index" or "1.DiscreteMath"
}

// Pre-process content to replace \( \) with $ $ and \[ \] with $$ $$
const preprocessMath = (content: string) => {
  return content
    .replace(/\\\[([\s\S]*?)\\\]/g, '$$$$$1$$$$') // \[ ... \] -> $$ ... $$
    .replace(/\\\(([\s\S]*?)\\\)/g, '$$$1$$');   // \( ... \) -> $ ... $
};

const CopyButton = ({ text }: { text: string }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy:', err);
    }
  };

  return (
    <button
      onClick={handleCopy}
      className="absolute right-2 top-2 p-1 rounded bg-muted/50 hover:bg-muted text-xs text-muted-foreground transition-colors"
      title="Copy code"
    >
      {copied ? 'Copied!' : 'Copy'}
    </button>
  );
};

export default function MarkdownRenderer({ content, currentPath }: MarkdownRendererProps) {
  const processedContent = preprocessMath(content);

  // Calculate base path for images
  // currentPath is like "1.DiscreteMath/index" or "1.DiscreteMath"
  // We want the folder path.
  // If it ends with /index, remove it.
  const folderPath = currentPath ? currentPath.replace(/\/index$/, '') : '';
  
  // Base URL for assets
  // In dev: /personal-wiki-site/wiki-content/FOLDER/IMAGE
  // In prod: /personal-wiki-site/wiki-content/FOLDER/IMAGE
  // Note: vite-plugin-static-copy puts files in dist/wiki-content
  // Vite base is /personal-wiki-site/
  const assetBase = `/personal-wiki-site/wiki-content/${folderPath}`;

  return (
    <div className="prose prose-slate dark:prose-invert max-w-none">
      <ReactMarkdown 
        remarkPlugins={[remarkGfm, remarkMath]} 
        rehypePlugins={[rehypeHighlight, rehypeKatex]}
        components={{
          img({ src, alt, ...props }) {
             let finalSrc = src;
             if (src && !src.startsWith('http') && !src.startsWith('/')) {
                 // Relative path
                 // Remove ./ prefix if present
                 const cleanSrc = src.replace(/^\.\//, '');
                 finalSrc = `${assetBase}/${cleanSrc}`.replace(/\/+/g, '/');
             }
             return <img src={finalSrc} alt={alt} {...props} className="rounded-lg shadow-md max-w-full mx-auto" />;
          },
          code({ node, inline, className, children, ...props }: any) {
            const match = /language-(\w+)/.exec(className || '');
            const codeText = String(children).replace(/\n$/, '');
            const language = match ? match[1] : '';

            if (!inline) {
                if (language === 'mermaid') {
                    return <MermaidBlock code={codeText} />;
                }
                if (language === 'python-plot' || (language === 'python' && codeText.includes('plt.show') || codeText.includes('plt.savefig'))) {
                    // Use PythonPlotBlock for explicit 'python-plot' or python code that looks like plotting
                    // Actually, let's stick to explicit 'python-plot' or maybe just 'python' if user wants?
                    // User said "support using python to draw".
                    // Let's use a specific language tag 'python-plot' to be safe, 
                    // or just 'python' if it imports matplotlib?
                    // Let's check for 'python-plot' OR if the code imports matplotlib.
                    if (language === 'python-plot' || codeText.includes('import matplotlib')) {
                        return <PythonPlotBlock code={codeText} />;
                    }
                }

              return (
                <div className="relative group">
                  <CopyButton text={codeText} />
                  <code className={className} {...props}>
                    {children}
                  </code>
                </div>
              );
            }
            
            // Inline code styling
            return (
              <code className={`${className} bg-muted px-1.5 py-0.5 rounded text-sm font-mono before:content-[''] after:content-['']`} {...props}>
                {children}
              </code>
            );
          },
          pre({ children }) {
             return <pre className="relative">{children}</pre>;
          }
        }}
      >
        {processedContent}
      </ReactMarkdown>
    </div>
  );
}

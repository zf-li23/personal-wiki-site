import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeHighlight from 'rehype-highlight';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'highlight.js/styles/github-dark.css';
import 'katex/dist/katex.min.css';
import { useState } from 'react';
import MermaidBlock from './MermaidBlock';
import PythonPlotBlock from './PythonPlotBlock';
import { generateId } from '@/lib/utils';

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
  // currentPath is the slug, e.g. "1.DiscreteMath/index" or "1.DiscreteMath/1.1.Logic"
  // Since the wiki structure is folder-based (index.md files), the slug represents the folder.
  // We use the slug directly as the folder path.
  const folderPath = currentPath || '';
  
  // Base URL for assets
  // In dev: /personal-wiki-site/wiki-content/FOLDER/IMAGE
  // In prod: /personal-wiki-site/wiki-content/FOLDER/IMAGE
  // Note: vite-plugin-static-copy puts files in dist/wiki-content
  // Vite base is /personal-wiki-site/
  // If folderPath is empty, we shouldn't add a trailing slash if we want to be clean, but double slash is usually fine.
  const assetBase = `/personal-wiki-site/wiki-content/${folderPath}`;

  return (
    <div className="prose prose-slate dark:prose-invert max-w-none">
      <ReactMarkdown 
        remarkPlugins={[remarkGfm, remarkMath]} 
        rehypePlugins={[
          rehypeRaw, 
          rehypeHighlight, 
          [rehypeKatex, { strict: false }]
        ]}
        remarkRehypeOptions={{ allowDangerousHtml: true }}
        components={{
          h2({ children, ...props }) {
            const id = generateId(String(children));
            return <h2 id={id} {...props}>{children}</h2>;
          },
          h3({ children, ...props }) {
            const id = generateId(String(children));
            return <h3 id={id} {...props}>{children}</h3>;
          },
          img({ src, alt, ...props }) {
             let finalSrc = src;
             if (src && !src.startsWith('http') && !src.startsWith('/')) {
                 // Relative path
                 // Remove ./ prefix if present
                 const cleanSrc = src.replace(/^\.\//, '');
                 // Join with assetBase
                 // If assetBase ends with /, don't add another.
                 // But assetBase is constructed with template literal, might not end with /.
                 // folderPath might be empty.
                 finalSrc = `${assetBase}/${cleanSrc}`.replace(/\/+/g, '/');
             }
             return <img src={finalSrc} alt={alt} {...props} className="rounded-lg shadow-md max-w-full mx-auto" />;
          },
          code({ node, inline, className, children, ...props }: any) {
            const match = /language-(\w+)/.exec(className || '');
            const codeText = String(children).replace(/\n$/, '');
            const language = match ? match[1] : '';
            const isMultiLine = codeText.includes('\n');

            // Treat as block if it's explicitly not inline, OR if it has a language, OR if it's multiline
            // This helps when rehype-raw or other plugins might mess up the 'inline' prop
            const isBlock = !inline && (match || isMultiLine);

            if (isBlock) {
                if (language === 'mermaid') {
                    return <MermaidBlock code={codeText} />;
                }
                if (language === 'python-plot' || (language === 'python' && codeText.includes('import matplotlib'))) {
                    return <PythonPlotBlock code={codeText} />;
                }

              return (
                <div className="relative group my-4">
                  <CopyButton text={codeText} />
                  <code className={className} {...props}>
                    {children}
                  </code>
                </div>
              );
            }
            
            // Inline code styling
            return (
              <code className="bg-muted px-1.5 py-0.5 rounded text-sm font-mono text-foreground" {...props}>
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

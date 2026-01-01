import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeHighlight from 'rehype-highlight';
import rehypeKatex from 'rehype-katex';
import 'highlight.js/styles/github-dark.css';
import 'katex/dist/katex.min.css';
import { useState } from 'react';

interface MarkdownRendererProps {
  content: string;
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

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
  const processedContent = preprocessMath(content);

  return (
    <div className="prose prose-slate dark:prose-invert max-w-none">
      <ReactMarkdown 
        remarkPlugins={[remarkGfm, remarkMath]} 
        rehypePlugins={[rehypeHighlight, rehypeKatex]}
        components={{
          code({ node, inline, className, children, ...props }: any) {
            const match = /language-(\w+)/.exec(className || '');
            const codeText = String(children).replace(/\n$/, '');

            if (!inline && match) {
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

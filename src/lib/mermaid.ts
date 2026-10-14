/**
 * Renders `.wiki-mermaid` blocks produced by the content pipeline:
 *   <div class="wiki-mermaid"><pre class="wiki-mermaid-source">graph TD; ...</pre></div>
 * Mermaid is loaded on demand (it is large) and the source is kept in a data
 * attribute so diagrams can be re-rendered when the theme changes.
 */
import type { Theme } from './preferences.ts';

let counter = 0;

export async function renderMermaidBlocks(root: HTMLElement, theme: Theme): Promise<void> {
  const blocks = [...root.querySelectorAll<HTMLElement>('.wiki-mermaid')];
  if (!blocks.length) return;
  const { default: mermaid } = await import('mermaid');
  mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: theme === 'dark' ? 'dark' : 'default' });
  for (const block of blocks) {
    const source = (block.dataset.source ??= block.querySelector('.wiki-mermaid-source')?.textContent ?? '');
    if (block.dataset.renderedTheme === theme) continue;
    try {
      const { svg } = await mermaid.render(`wiki-mermaid-${++counter}`, source);
      block.innerHTML = svg;
      block.dataset.renderedTheme = theme;
      block.classList.remove('wiki-mermaid-error');
    } catch (e) {
      block.classList.add('wiki-mermaid-error');
      block.textContent = `Mermaid: ${e instanceof Error ? e.message : String(e)}\n\n${source}`;
    }
  }
}

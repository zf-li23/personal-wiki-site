/**
 * Connects the content pipeline to Vite:
 *  - publicDir is .generated/public (page JSON, media, plots, search index)
 *  - `virtual:wiki/site` exports the SiteData (navigation) to the client bundle
 *  - dev: builds once on startup, rebuilds on every change under content/, then
 *    either reloads the page (navigation changed) or tells the client to refetch
 *    the current page (`wiki:content` event), keeping the scroll position
 *  - build: fails on content errors; after bundling, prerenders every route
 */
import path from 'node:path';
import type { Plugin, ResolvedConfig } from 'vite';
import { type BuildResult, buildContent } from './build.ts';
import { CONTENT_DIR, GENERATED_PUBLIC_DIR, PLOT_RENDERER } from './paths.ts';
import { prerender } from './prerender.ts';

const VIRTUAL_ID = 'virtual:wiki/site';
const RESOLVED_ID = `\0${VIRTUAL_ID}`;

export function wikiContent(): Plugin {
  let config: ResolvedConfig;
  let result: BuildResult | null = null;
  let navJson = '';

  const log = (m: string) => config.logger.info(`[wiki] ${m}`, { timestamp: true });

  return {
    name: 'wiki-content',
    config: () => ({ publicDir: GENERATED_PUBLIC_DIR }),
    configResolved(c) {
      config = c;
    },

    async buildStart() {
      if (config.command !== 'build') return;
      result = await buildContent({ log });
      if (result.diag.items.length) config.logger.warn(result.diag.format());
      if (result.diag.errorCount) this.error(`content has ${result.diag.errorCount} error(s); see above`);
    },

    resolveId: (id) => (id === VIRTUAL_ID ? RESOLVED_ID : undefined),
    load(id) {
      if (id !== RESOLVED_ID) return undefined;
      if (!result) throw new Error('wiki content was not built');
      return `export default ${JSON.stringify(result.site)};`;
    },

    async configureServer(server) {
      const rebuild = async () => {
        const started = Date.now();
        result = await buildContent({ dev: true, log });
        const { diag, site } = result;
        if (diag.items.length) config.logger.warn(diag.format());
        log(`content built: ${result.tree.pages.size} pages, ${diag.errorCount} error(s), ${diag.warningCount} warning(s) in ${Date.now() - started}ms`);
        const nextNav = JSON.stringify(site.nav);
        const navChanged = navJson !== '' && nextNav !== navJson;
        navJson = nextNav;
        return navChanged;
      };
      await rebuild();

      let timer: NodeJS.Timeout | undefined;
      let running: Promise<void> = Promise.resolve();
      const schedule = (file: string) => {
        if (!file.startsWith(CONTENT_DIR + path.sep) && file !== PLOT_RENDERER) return;
        clearTimeout(timer);
        timer = setTimeout(() => {
          running = running.then(async () => {
            const navChanged = await rebuild();
            const mod = server.moduleGraph.getModuleById(RESOLVED_ID);
            if (mod) server.moduleGraph.invalidateModule(mod);
            if (navChanged) server.ws.send({ type: 'full-reload' });
            else server.ws.send({ type: 'custom', event: 'wiki:content', data: { buildId: result!.site.buildId } });
          }).catch((e: unknown) => config.logger.error(`[wiki] rebuild failed: ${String(e)}`));
        }, 150);
      };
      server.watcher.add([CONTENT_DIR, PLOT_RENDERER]);
      server.watcher.on('change', schedule);
      server.watcher.on('add', schedule);
      server.watcher.on('unlink', schedule);
      server.watcher.on('unlinkDir', schedule);
    },

    closeBundle() {
      if (config.command !== 'build' || !result || config.build.ssr) return;
      const count = prerender(path.resolve(config.root, config.build.outDir), result);
      log(`prerendered ${result.payloads.size} pages (${count} in sitemap)`);
    },
  };
}

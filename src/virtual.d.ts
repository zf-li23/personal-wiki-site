declare module 'virtual:wiki/site' {
  /** Navigation tree produced by the content pipeline (scripts/wiki/vite-plugin.ts). */
  const site: import('./shared/types.ts').SiteData;
  export default site;
}

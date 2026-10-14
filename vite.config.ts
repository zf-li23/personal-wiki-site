import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
import { wikiContent } from './scripts/wiki/vite-plugin.ts';
import { BASE_PATH } from './site.config.ts';

export default defineConfig({
  base: BASE_PATH,
  plugins: [react(), tailwindcss(), wikiContent()],
  build: {
    chunkSizeWarningLimit: 800,
    rollupOptions: {
      output: {
        // GitHub Pages (Jekyll) ignores files starting with "_".
        sanitizeFileName: (name) => name.replace(/^_+/, ''),
      },
    },
  },
});

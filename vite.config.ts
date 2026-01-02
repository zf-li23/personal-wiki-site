import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import { viteStaticCopy } from 'vite-plugin-static-copy'
import fs from 'fs'
import serveStatic from 'serve-static'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    viteStaticCopy({
      targets: [
        {
          src: 'docs/wiki/**/*',
          dest: 'wiki-content'
        }
      ]
    }),
    {
      name: 'serve-wiki-content',
      configureServer(server) {
        server.middlewares.use(
          '/personal-wiki-site/wiki-content',
          serveStatic(path.resolve(__dirname, 'docs/wiki'))
        )
      }
    }
  ],
  base: '/personal-wiki-site/', // Set base to repository name for GitHub Pages
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})

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
  build: {
    chunkSizeWarningLimit: 1000, // Increase warning limit to 1MB
    rollupOptions: {
      output: {
        manualChunks: {
          'mermaid': ['mermaid'],
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'markdown-core': ['react-markdown', 'remark-gfm', 'rehype-raw', 'rehype-slug'],
          'math-vendor': ['remark-math', 'rehype-katex', 'katex'],
          'syntax-vendor': ['highlight.js', 'rehype-highlight']
        },
        // Force chunk names to not start with _ to avoid Jekyll issues on GitHub Pages
        chunkFileNames: (chunkInfo) => {
          const name = chunkInfo.name.replace(/^_/, 'safe_');
          return `assets/js/${name}-[hash].js`;
        },
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
      }
    }
  }
})

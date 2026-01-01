export interface WikiPage {
  id: string;
  title: string;
  slug: string;
  content?: string;
  children?: WikiPage[];
}

export const wikiData: WikiPage[] = [
  {
    id: '1',
    title: 'Introduction',
    slug: 'intro',
    content: `# Introduction

Welcome to my personal wiki. This is where I store my knowledge.

## About this Wiki
This wiki is built with React and Markdown. It features:
- Hierarchical structure
- Markdown rendering
- Dark/Light mode
- Responsive design

## How to navigate
Use the sidebar on the left to navigate through different topics.
`,
  },
  {
    id: '2',
    title: 'Frontend Development',
    slug: 'frontend',
    children: [
      {
        id: '2-1',
        title: 'React',
        slug: 'react',
        content: `# React

React is a JavaScript library for building user interfaces.

## Core Concepts
- Components
- Props
- State

## Hooks
1. useState
2. useEffect
3. useContext
`,
        children: [
          {
            id: '2-1-1',
            title: 'Hooks Deep Dive',
            slug: 'hooks',
            content: `# Hooks Deep Dive

Detailed explanation of React Hooks.

### useState
\`\`\`javascript
const [count, setCount] = useState(0);
\`\`\`
`
          }
        ]
      },
      {
        id: '2-2',
        title: 'TypeScript',
        slug: 'typescript',
        content: `# TypeScript

TypeScript is JavaScript with syntax for types.

## Basic Types
- string
- number
- boolean
- array
- any
`
      }
    ]
  },
  {
    id: '3',
    title: 'Backend Development',
    slug: 'backend',
    children: [
      {
        id: '3-1',
        title: 'Node.js',
        slug: 'nodejs',
        content: '# Node.js\n\nJavaScript runtime built on Chrome\'s V8 JavaScript engine.'
      }
    ]
  }
];

export function findPageByPath(path: string, data: WikiPage[] = wikiData): WikiPage | null {
  const segments = path.split('/').filter(Boolean);
  if (segments.length === 0) return null;

  let currentLevel = data;
  let foundPage: WikiPage | null = null;

  for (const segment of segments) {
    foundPage = currentLevel.find(p => p.slug === segment) || null;
    if (!foundPage) return null;
    
    if (foundPage.children) {
      currentLevel = foundPage.children;
    } else {
      // If we have more segments but no children, it's a mismatch (or maybe we want to support partial matches?)
      // For now, strict match.
      currentLevel = []; 
    }
  }

  return foundPage;
}

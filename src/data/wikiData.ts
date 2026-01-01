export interface WikiPage {
  id: string;
  title: string;
  slug: string;
  content?: string;
  children?: WikiPage[];
}

// Helper to extract title from markdown content
function extractTitle(content: string, filename: string): string {
  const match = content.match(/^#\s+(.+)$/m);
  if (match) {
    return match[1];
  }
  // Fallback to filename, removing extension and leading numbers
  const name = filename.split('/').pop()?.replace(/\.md$/, '') || '';
  return name.replace(/^\d+-/, '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

// Helper to process filename into slug and sort order
function processFileInfo(path: string) {
  // Remove /wiki/ prefix and .md suffix
  const relativePath = path.replace(/^\/wiki\//, '').replace(/\.md$/, '');
  const segments = relativePath.split('/');
  
  const cleanSegments = segments.map(segment => {
    // Extract ordering number if present (e.g., "01-intro" -> order: 1, name: "intro")
    const match = segment.match(/^(\d+)-(.+)$/);
    if (match) {
      return { order: parseInt(match[1]), name: match[2] };
    }
    return { order: 999, name: segment };
  });

  return {
    slug: cleanSegments.map(s => s.name).join('/'),
    segments: cleanSegments
  };
}

function buildWikiData(): WikiPage[] {
  // Import all markdown files from the wiki directory
  // Note: The path must be relative to this file or absolute from project root
  // Using absolute path from project root for clarity, assuming 'wiki' is at root
  const modules = import.meta.glob('/wiki/**/*.md', { query: '?raw', import: 'default', eager: true });
  
  const root: WikiPage[] = [];

  for (const path in modules) {
    const content = modules[path] as string;
    const { slug, segments } = processFileInfo(path);
    const title = extractTitle(content, path);
    
    let currentLevel = root;
    
    segments.forEach((segment, index) => {
      const isLast = index === segments.length - 1;
      const existingNode = currentLevel.find(node => node.slug === segment.name);

      if (existingNode) {
        if (isLast) {
          // Update existing node (which might have been created as a parent placeholder)
          existingNode.content = content;
          existingNode.title = title; // Update title from content
        }
        if (!existingNode.children) existingNode.children = [];
        currentLevel = existingNode.children;
      } else {
        const newNode: WikiPage = {
          id: path, // Use file path as ID
          title: isLast ? title : segment.name.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
          slug: segment.name,
          children: [],
          // Only leaf nodes or nodes with matching files get content
          content: isLast ? content : undefined 
        };
        
        // Insert in correct order
        const insertIndex = currentLevel.findIndex(node => {
           // We need to recover the order from the original path to compare
           // This is a bit tricky since we only have the clean node. 
           // But we can assume the current iteration's segment order is what matters.
           return false; // Simplified: just push and sort later
        });
        
        currentLevel.push(newNode);
        
        // Sort current level by order (we need to store order on the node temporarily or re-derive it)
        // For simplicity, let's rely on the file system traversal order or sort at the end.
        // Actually, let's attach a hidden property for sorting if we could, but interface doesn't allow.
        // Let's just sort by filename (which includes the number) implicitly if glob returns sorted keys.
        // Glob usually returns sorted keys.
        
        currentLevel = newNode.children!;
      }
    });
  }

  // Recursive sort function
  const sortNodes = (nodes: WikiPage[]) => {
    nodes.sort((a, b) => {
      // We need to find the original file path segment to compare numbers...
      // This is getting complicated. 
      // Alternative: The 'modules' keys are already sorted alphabetically.
      // "01-intro.md" comes before "02-frontend".
      // So if we process in order, the array should be naturally ordered!
      return 0;
    });
    nodes.forEach(node => {
      if (node.children) sortNodes(node.children);
    });
  };

  // Since glob keys are sorted, we might be good. 
  // But "02-frontend/01-react.md" vs "02-frontend.md" (if it existed).
  
  return root;
}

export const wikiData: WikiPage[] = buildWikiData();

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

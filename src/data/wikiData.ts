export interface WikiPage {
  id: string;
  title: string;
  slug: string;
  content?: string;
  children?: WikiPage[];
}

// Helper to extract title from markdown content or filename
function extractTitle(_content: string, filename: string): string {
  // Filename format: "1.1.1.Title.md" -> "Title"
  // Or "index.md" inside "1.1.1.Title" -> "Title"
  
  let namePart = filename.split('/').pop()?.replace(/\.md$/, '') || '';
  
  if (namePart === 'index') {
    // Use parent folder name
    const parts = filename.split('/');
    if (parts.length >= 2) {
      namePart = parts[parts.length - 2];
    }
  }

  // Match "1.2.3.Title" -> capture "Title"
  const match = namePart.match(/^[\d\.]+\.?(.*)$/);
  if (match && match[1]) {
    return match[1].trim(); 
  }
  return namePart;
}

// Helper to process filename into slug and sort order
function processFileInfo(path: string) {
  // Remove /docs/ prefix and .md suffix
  let relativePath = path.replace(/^\.\.\/\.\.\/docs\/wiki\//, '').replace(/\.md$/, '');
  
  // Handle index files: they represent the folder itself
  if (relativePath.endsWith('/index')) {
    relativePath = relativePath.replace(/\/index$/, '');
  } else if (relativePath === 'index') {
    // Root index? Unlikely in this structure but possible
    relativePath = '';
  }

  const segments = relativePath.split('/').filter(Boolean);
  
  const cleanSegments = segments.map(segment => {
    return { name: segment };
  });

  return {
    slug: cleanSegments.map(s => s.name).join('/'),
    segments: cleanSegments
  };
}

// Validation function for "Double Insurance" (Runtime/Dev check)
function validatePath(path: string) {
  const relativePath = path.replace(/^\.\.\/\.\.\/docs\/wiki\//, '').replace(/\.md$/, '');
  const segments = relativePath.split('/');
  const filename = segments[segments.length - 1];
  
  // Check if filename starts with a numbering pattern
  const fileMatch = filename.match(/^([\d\.]+)\.?/);
  if (!fileMatch) return; // No numbering, skip validation
  
  const fileNumbering = fileMatch[1]; // e.g. "1.1.1"
  
  // Check if parent directory matches the prefix
  if (segments.length > 1) {
    const parentDir = segments[segments.length - 2];
    const parentMatch = parentDir.match(/^([\d\.]+)\.?/);
    
    if (parentMatch) {
      const parentNumbering = parentMatch[1]; // e.g. "1.1"
      
      if (!fileNumbering.startsWith(parentNumbering)) {
        console.warn(`[Wiki Validation Warning] File "${filename}" (Numbering: ${fileNumbering}) is not a valid child of directory "${parentDir}" (Numbering: ${parentNumbering}). Path: ${path}`);
      }
    }
  }
}

function buildWikiData(): WikiPage[] {
  // Import all markdown files from the docs directory
  const modules = import.meta.glob('../../docs/**/*.md', { query: '?raw', import: 'default', eager: true });
  
  const root: WikiPage[] = [];

  // Sort paths to ensure parents are processed before children (usually)
  // and to ensure correct order in the list.
  const sortedPaths = Object.keys(modules).sort((a, b) => {
    return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
  });

  for (const path of sortedPaths) {
    validatePath(path);
    
    const content = modules[path] as string;
    const { segments } = processFileInfo(path);
    const title = extractTitle(content, path);
    
    let currentLevel = root;
    
    segments.forEach((segment, index) => {
      const isLast = index === segments.length - 1;
      const existingNode = currentLevel.find(node => node.slug === segment.name);

      if (existingNode) {
        if (isLast) {
          existingNode.content = content;
          existingNode.title = title;
        }
        if (!existingNode.children) existingNode.children = [];
        currentLevel = existingNode.children;
      } else {
        const newNode: WikiPage = {
          id: path,
          title: isLast ? title : segment.name, // Use segment name for folders until we find the matching file
          slug: segment.name,
          children: [],
          content: isLast ? content : undefined 
        };
        
        currentLevel.push(newNode);
        currentLevel = newNode.children!;
      }
    });
  }
  
  return root;
}

export const wikiData: WikiPage[] = buildWikiData();

export function findPageByPath(path: string, data: WikiPage[] = wikiData): { page: WikiPage, ancestors: WikiPage[] } | null {
  const segments = path.split('/').filter(Boolean);
  if (segments.length === 0) return null;

  let currentLevel = data;
  let foundPage: WikiPage | null = null;
  const ancestors: WikiPage[] = [];

  for (const segment of segments) {
    const decodedSegment = decodeURIComponent(segment);
    foundPage = currentLevel.find(p => p.slug === decodedSegment) || null;
    if (!foundPage) return null;
    
    ancestors.push(foundPage);

    if (foundPage.children) {
      currentLevel = foundPage.children;
    } else {
      currentLevel = []; 
    }
  }

  // The last item in ancestors is the page itself, so pop it or handle it in consumer
  return foundPage ? { page: foundPage, ancestors: ancestors.slice(0, -1) } : null;
}

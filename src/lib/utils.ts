import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"
 
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export interface TOCItem {
  id: string;
  text: string;
  level: number;
}

export function generateId(text: string): string {
  return text
    .toString()
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w\-\.\u4e00-\u9fa5]+/g, '') // Keep alphanumeric, hyphens, dots, and Chinese characters
    .replace(/^\-+|\-+$/g, ''); // Remove leading/trailing hyphens
}

export function extractHeaders(markdown: string): TOCItem[] {
  const lines = markdown.split('\n');
  const headers: TOCItem[] = [];
  
  // Helper to strip markdown syntax from header text (e.g. **Bold**, `Code`)
  const cleanText = (text: string) => {
    return text
      .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // Links
      .replace(/`([^`]+)`/g, '$1')             // Inline code
      .replace(/\*\*([^*]+)\*\*/g, '$1')       // Bold
      .replace(/\*([^*]+)\*/g, '$1')           // Italic
      .trim();
  };
  
  lines.forEach((line) => {
    const match = line.match(/^(#{2,3})\s+(.+)$/); // Only h2 and h3 for TOC to avoid clutter
    if (match) {
      const level = match[1].length;
      const rawText = match[2];
      const text = cleanText(rawText);
      const id = generateId(text);
      headers.push({ id, text, level });
    }
  });
  
  return headers;
}

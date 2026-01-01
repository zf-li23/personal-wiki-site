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

export function extractHeaders(markdown: string): TOCItem[] {
  const lines = markdown.split('\n');
  const headers: TOCItem[] = [];
  
  lines.forEach((line) => {
    const match = line.match(/^(#{2,3})\s+(.+)$/); // Only h2 and h3 for TOC to avoid clutter
    if (match) {
      const level = match[1].length;
      const text = match[2];
      const id = text.toLowerCase().replace(/[^\w]+/g, '-');
      headers.push({ id, text, level });
    }
  });
  
  return headers;
}

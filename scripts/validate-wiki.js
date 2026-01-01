import fs from 'fs';
import path from 'path';

const WIKI_ROOT = path.join(process.cwd(), 'docs/wiki');

function validateDirectory(dirPath, parentNumbering) {
  if (!fs.existsSync(dirPath)) return;

  const items = fs.readdirSync(dirPath);

  items.forEach(item => {
    if (item.startsWith('.')) return; // Skip hidden files

    const fullPath = path.join(dirPath, item);
    const stat = fs.statSync(fullPath);
    
    // Extract numbering from item name
    // Matches "1.2.3.Title" or "1.Title"
    const match = item.match(/^([\d\.]+)\.?/);
    
    if (match) {
      const currentNumbering = match[1]; // e.g. "1.1.1" or "1.1"
      
      // Check if it matches parent
      if (parentNumbering) {
        if (!currentNumbering.startsWith(parentNumbering)) {
          console.error(`\x1b[31m[Error] Naming Mismatch:\x1b[0m`);
          console.error(`  File/Dir: ${item}`);
          console.error(`  Path:     ${fullPath}`);
          console.error(`  Expected to start with: ${parentNumbering}`);
          console.error(`  Actual numbering:       ${currentNumbering}`);
          process.exit(1);
        }
        
        // Strict check: Child numbering must be longer than parent numbering
        // e.g. Parent 1.1, Child 1.1.1 (OK), Child 1.1 (Error)
        // Exception: index.md (which we handle separately below, but here we are checking folders/files)
        // If it's a folder, it must be deeper.
        // If it's a file, it must be deeper UNLESS it's index.md (but index.md doesn't have numbering in name usually)
        
        if (currentNumbering === parentNumbering) {
             // This is the case "1.1.2.Title.md" inside "1.1.2.Title" folder?
             // No, folder name is "1.1.2.Title". File name is "1.1.2.Title.md".
             // If we migrated to index.md, this file shouldn't exist.
             // But if it does, it's a duplicate/ambiguous.
             console.error(`\x1b[31m[Error] Ambiguous Structure:\x1b[0m`);
             console.error(`  File/Dir: ${item} has same numbering as parent.`);
             console.error(`  If this is the content for the folder, please rename it to 'index.md'.`);
             process.exit(1);
        }
      }

      if (stat.isDirectory()) {
        validateDirectory(fullPath, currentNumbering);
      }
    } else {
      // Item doesn't start with a number. 
      if (item === 'index.md') {
          // Valid index file.
          return;
      }
      // If it's a markdown file or a folder in the wiki structure, it SHOULD start with a number according to user rules.
      // But maybe assets or other things?
      // User said: "Strict numbering".
      if (item.endsWith('.md') || stat.isDirectory()) {
         console.warn(`\x1b[33m[Warning] Item without numbering found: ${item} in ${dirPath}\x1b[0m`);
      }
    }
  });
}

console.log('Validating Wiki Structure...');
try {
    validateDirectory(WIKI_ROOT, null);
    console.log('\x1b[32mWiki Structure Validation Passed.\x1b[0m');
} catch (e) {
    console.error(e);
    process.exit(1);
}

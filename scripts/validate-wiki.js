import fs from 'fs';
import path from 'path';

const WIKI_ROOT = path.join(process.cwd(), 'docs');

function validateDirectory(dirPath, parentNumbering) {
  if (!fs.existsSync(dirPath)) return;

  const items = fs.readdirSync(dirPath);

  items.forEach(item => {
    if (item.startsWith('.')) return; // Skip hidden files

    const fullPath = path.join(dirPath, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
        // Only validate directories that look like wiki sections (start with number)
        const match = item.match(/^([\d\.]+)\.?/);
        
        if (match) {
            const currentNumbering = match[1]; // e.g. "1.1.1" or "1.1"
            
            // Check if it matches parent
            if (parentNumbering) {
                if (!currentNumbering.startsWith(parentNumbering)) {
                    console.error(`\x1b[31m[Error] Naming Mismatch:\x1b[0m`);
                    console.error(`  Dir:      ${item}`);
                    console.error(`  Path:     ${fullPath}`);
                    console.error(`  Expected to start with: ${parentNumbering}`);
                    console.error(`  Actual numbering:       ${currentNumbering}`);
                    process.exit(1);
                }
                
                if (currentNumbering === parentNumbering) {
                     console.error(`\x1b[31m[Error] Ambiguous Structure:\x1b[0m`);
                     console.error(`  Dir: ${item} has same numbering as parent.`);
                     process.exit(1);
                }
            }
            
            // Recurse into numbered directory
            validateDirectory(fullPath, currentNumbering);
        } else {
            // Non-numbered directory (e.g. "assets", "images")
            // Ignore it (don't recurse, don't validate)
        }
    } else {
        // It is a file
        // User requested: "Files can be unchecked"
        // So we ignore all files. 
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

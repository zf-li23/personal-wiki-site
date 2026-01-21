import os
import re
import hashlib
import matplotlib
import matplotlib.pyplot as plt
import sys
import textwrap
from pathlib import Path

# Set non-interactive backend
matplotlib.use('Agg')

# Find all python-plot blocks
WIKI_ROOT = Path("docs/wiki")

def extract_code_blocks(md_content):
    # Regex for ```python-plot ... ``` (non-greedy)
    # Returns list of code strings
    # Allow whitespace before closing backticks
    pattern = re.compile(r'```python-plot\s*\n(.*?)\n\s*```', re.DOTALL)
    blocks = pattern.findall(md_content)
    # Dedent to handle indented code blocks (e.g. inside lists)
    cleaned = []
    for b in blocks:
        # Remove empty first lines if any (caused by spaces after ```)
        lines = b.split('\n')
        # Dedent the whole block based on the first non-empty line
        dedented = textwrap.dedent(b)
        cleaned.append(dedented.strip())
    return cleaned

def generate_plot(code, output_path, is_dark):
    try:
        # Reset plot
        plt.clf()
        plt.close('all')
        
        # Set style
        if is_dark:
            plt.style.use('dark_background')
        else:
            plt.style.use('default')
            
        # Execute code
        # We need to capture the plot state after execution
        exec_globals = {}
        # print(f"DEBUG CODE:\n{code}\nEND DEBUG") 
        try:
            exec(code, exec_globals)
        except Exception:
            print("--- CODE START ---")
            print(code)
            print("--- CODE END ---")
            raise
        
        # Save figure
        # Check if user plot created a figure
        if plt.get_fignums():
            plt.savefig(output_path, format='png', bbox_inches='tight', dpi=100)
            plt.close('all')
            return True
        else:
            print(f"  [Warning] No plot generated for code block.")
            return False
    except Exception as e:
        print(f"  [Error] Failed to generate plot: {e}")
        return False

def main():
    print("Scanning for python-plot blocks...")
    count = 0
    
    for md_file in WIKI_ROOT.rglob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            blocks = extract_code_blocks(content)
            
            if not blocks:
                continue
                
            print(f"Processing {md_file} ({len(blocks)} blocks)")
            
            for block in blocks:
                # Calculate hash using the same logic as frontend (md5 of trimmed string usually)
                # Ensure we handle newlines exactly as the frontend would receive them
                # React 'children' usually keeps newlines.
                # Let's normalize by stripping trailing newlines which extract_code_blocks regex does implicitly by capture group placement?
                # Actually regex `\n(.*?)\n``` ` captures content WITHOUT the last newline before ```
                # But frontend `String(children).replace(/\n$/, '')` effectively removes trailing newline.
                
                # To be safe, let's normalize: logic matches `codeText` in MarkdownRenderer
                code_text = block
                
                # Check for cached/existing files
                # Filename: {hash}_light.png and {hash}_dark.png
                code_hash = hashlib.md5(code_text.encode('utf-8')).hexdigest()
                
                light_path = md_file.parent / f"{code_hash}_light.png"
                dark_path = md_file.parent / f"{code_hash}_dark.png"
                
                # Generate Light
                if not light_path.exists():
                    print(f"  Generating Light: {light_path.name}")
                    generate_plot(code_text, light_path, is_dark=False)
                else:
                    # check if we should overwrite? Assume hash change = content change, so existing file is valid for this content
                    pass
                    
                # Generate Dark
                if not dark_path.exists():
                     print(f"  Generating Dark:  {dark_path.name}")
                     generate_plot(code_text, dark_path, is_dark=True)
                
                count += 1
                
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    print(f"Done. Processed {count} plot blocks.")

if __name__ == "__main__":
    main()

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
        # Determine smart dedent logic to match frontend behavior
        lines = b.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        normalized_text = b
        if non_empty_lines:
            # Check common indentation
            common_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
            
            if common_indent > 0:
                normalized_text = textwrap.dedent(b)
        
        cleaned.append(normalized_text.strip())
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
            # Force white background for light mode
            plt.gcf().set_facecolor('white')
            plt.gca().set_facecolor('white')

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
            plt.savefig(output_path, format='png', bbox_inches='tight', dpi=100, facecolor=plt.gcf().get_facecolor(), transparent=False)
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
            
            for code_text in blocks:
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

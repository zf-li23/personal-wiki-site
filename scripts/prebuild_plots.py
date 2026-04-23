import os
import re
import hashlib
import sys
import textwrap
import json
from pathlib import Path

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    print("[Info] matplotlib is not installed, skip prebuild plot generation.")
    sys.exit(0)

# Find all python-plot blocks
WIKI_ROOT = Path("docs/wiki")
MANIFEST_PATH = Path("src/data/plot_manifest.json")

def load_manifest():
    if MANIFEST_PATH.exists():
        try:
             return json.loads(MANIFEST_PATH.read_text('utf-8'))
        except:
             return {}
    return {}

def save_manifest(manifest):
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding='utf-8')

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

def generate_plot(code, output_dir, file_hash, is_dark):
    try:
        # Reset plot
        plt.clf()
        plt.close('all')
        
        # Set style
        if is_dark:
            plt.style.use('dark_background')
            # Patch code to replace black lines with white lines for dark mode
            # This is a heuristic to fix explicit 'k' or 'black' usage
            code = code.replace("'k'", "'w'")\
                       .replace('"k"', '"w"')\
                       .replace("'black'", "'white'")\
                       .replace('"black"', '"white"')\
                       .replace("'k-'", "'w-'")\
                       .replace("'k--'", "'w--'")
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
        figs = plt.get_fignums()
        n_figs = len(figs)
        
        if n_figs == 0:
            print(f"  [Warning] No plot generated for code block.")
            return 0
            
        theme = 'dark' if is_dark else 'light'
        
        if n_figs == 1:
             output_path = output_dir / f"{file_hash}_{theme}.png"
             plt.figure(figs[0])
             plt.savefig(output_path, format='png', bbox_inches='tight', dpi=100, facecolor=plt.gcf().get_facecolor(), transparent=False)
        else:
             for idx, num in enumerate(figs):
                 output_path = output_dir / f"{file_hash}_{idx}_{theme}.png"
                 plt.figure(num)
                 plt.savefig(output_path, format='png', bbox_inches='tight', dpi=100, facecolor=plt.gcf().get_facecolor(), transparent=False)
                 
        plt.close('all')
        return n_figs

    except Exception as e:
        print(f"  [Error] Failed to generate plot: {e}")
        return 0

def main():
    print("Scanning for python-plot blocks...")
    manifest = load_manifest()
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
                
                # Logic to determine if we should generate
                should_run = False
                
                # Old path check
                single_light = md_file.parent / f"{code_hash}_light.png"
                
                # New path check (suffix 0)
                multi_light_0 = md_file.parent / f"{code_hash}_0_light.png"
                
                if code_hash in manifest:
                    n = manifest[code_hash]
                    if n > 1:
                        if not multi_light_0.exists():
                            should_run = True
                    else: # n=1 or 0
                        if not single_light.exists():
                             should_run = True
                else:
                    # If not in manifest, and single file missing, run.
                    # Note: If single file exists, we assume it's correct (count=1),
                    # unless user deleted it to force regen.
                    if not single_light.exists():
                        should_run = True

                if should_run:
                    print(f"  Generating plot for {code_hash[:8]}...")
                    # Generate Light
                    n_light = generate_plot(code_text, md_file.parent, code_hash, is_dark=False)
                    
                    # Generate Dark
                    n_dark = generate_plot(code_text, md_file.parent, code_hash, is_dark=True)
                    
                    if n_light != n_dark:
                         print(f"  [Warning] Light ({n_light}) and Dark ({n_dark}) created different number of plots for {code_hash[:8]}")
                    
                    if n_light > 0:
                        manifest[code_hash] = n_light
                        count += 1
                
        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    save_manifest(manifest)
    print(f"Done. Processed/checked {count} plot blocks.")

if __name__ == "__main__":
    main()

/**
 * Chemical structures for ```smiles code blocks, drawn at build time with RDKit (WebAssembly).
 *
 * Each line of a block is one structure: a SMILES string, or a reaction SMILES (`A.B>>C`),
 * optionally followed by whitespace and a short language-neutral label (a compound number,
 * "(R)", a formula). The structures of one block are laid out in a row. Drawings are
 * monochrome and use `currentColor`, so they follow the reader's light or dark theme, and
 * every structure is drawn at the same bond length so sizes are comparable across the site.
 */
import initRDKitModule from '@rdkit/rdkit';
import type { MainModule } from '@rdkit/rdkit';

/** Bond length in CSS pixels: all structures on the site share this scale. */
const BOND_LENGTH = 25;

let rdkit: Promise<MainModule> | undefined;

function module(): Promise<MainModule> {
  rdkit ??= initRDKitModule().then((m) => {
    m.disable_logging();
    return m;
  });
  return rdkit;
}

export interface ChemLine {
  smiles: string;
  label?: string;
  reaction: boolean;
}

/** Split a block into structures; blank lines and `#` comments are skipped. */
export function parseChemBlock(source: string): ChemLine[] {
  return source
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith('#'))
    .map((l) => {
      const [smiles, ...rest] = l.split(/\s+/);
      const label = rest.join(' ').trim();
      return { smiles, reaction: smiles.includes('>'), ...(label ? { label } : {}) };
    });
}

const DRAW_OPTIONS = JSON.stringify({
  width: -1,
  height: -1,
  fixedBondLength: BOND_LENGTH,
  padding: 0.08,
  bondLineWidth: 1.5,
  clearBackground: false,
});

/** Draw one structure as an inline SVG, or return null when RDKit cannot parse it. */
export async function drawStructure(line: ChemLine): Promise<string | null> {
  const rd = await module();
  const obj = line.reaction ? rd.get_rxn(line.smiles) : rd.get_mol(line.smiles);
  if (!obj) return null;
  try {
    return themable(obj.get_svg_with_highlights(DRAW_OPTIONS));
  } finally {
    obj.delete();
  }
}

/** Strip the XML prologue, make the drawing scale with its container and inherit the text colour. */
function themable(svg: string): string {
  return svg
    .replace(/^<\?xml[^>]*>\s*/, '')
    .replace(/<!--[^]*?-->\s*/g, '')
    .replace(/<rect [^>]*\/>\s*/, (rect) => (/fill:#FFFFFF|fill:#ffffff/.test(rect) ? '' : rect))
    .replace(/#[0-9A-Fa-f]{6}\b/g, 'currentColor')
    .replace(/<svg ([^>]*?)width='([\d.]+)px' height='([\d.]+)px'/, "<svg $1width='$2' height='$3' class='wiki-chem-svg' role='img'");
}

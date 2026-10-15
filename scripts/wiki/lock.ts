/**
 * A cross-process lock for content builds. Several builds may run at once (agents writing in
 * parallel, the dev server); they share the plot cache and the output directory, so they take
 * turns. The lock is a directory (mkdir is atomic); a lock whose owner has exited, or that is
 * older than STALE_MS, is taken over.
 */
import fs from 'node:fs';
import path from 'node:path';
import { REPO_ROOT } from './paths.ts';

const LOCK_DIR = path.join(REPO_ROOT, '.cache', 'build.lock');
const STALE_MS = 45 * 60 * 1000;
const sleep = (ms: number) => Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);

/** The lock's owner process has exited without releasing it (e.g. it was killed). */
function ownerIsGone(): boolean {
  try {
    const pid = Number(fs.readFileSync(path.join(LOCK_DIR, 'pid'), 'utf8'));
    if (!pid) return false;
    process.kill(pid, 0);
    return false;
  } catch (e) {
    return (e as NodeJS.ErrnoException).code === 'ESRCH';
  }
}

export function acquireBuildLock(log: (message: string) => void = () => {}): () => void {
  fs.mkdirSync(path.dirname(LOCK_DIR), { recursive: true });
  let warned = false;
  for (;;) {
    try {
      fs.mkdirSync(LOCK_DIR);
      fs.writeFileSync(path.join(LOCK_DIR, 'pid'), String(process.pid));
      break;
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code !== 'EEXIST') throw e;
      let age = 0;
      try {
        age = Date.now() - fs.statSync(LOCK_DIR).mtimeMs;
      } catch {
        continue; // released between the two calls
      }
      if (age > STALE_MS || ownerIsGone()) {
        fs.rmSync(LOCK_DIR, { recursive: true, force: true });
        continue;
      }
      if (!warned) log('[wiki] another content build is running; waiting for it to finish');
      warned = true;
      sleep(500);
    }
  }
  let released = false;
  const release = () => {
    if (released) return;
    released = true;
    fs.rmSync(LOCK_DIR, { recursive: true, force: true });
  };
  process.once('exit', release);
  return release;
}

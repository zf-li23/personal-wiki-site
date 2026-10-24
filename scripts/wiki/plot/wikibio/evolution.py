"""Evolutionary dynamics for figures: Wright-Fisher drift and selection, fixation probabilities,
selection on quantitative traits, and the genealogy schematic of a Wright-Fisher population.

    from wikibio import evolution as evo
    p = evo.wright_fisher(N=100, s=0.02, p0=0.1, generations=200, reps=20, rng=rng)   # (gens+1, reps)
    u = evo.fixation_probability(N=50, s=0.01, p0=1 / 100, reps=20000, rng=rng)       # simulated
    evo.kimura_u(1 / 100, N=50, s=0.01)                                              # diffusion theory
    evo.genealogy(ax, (1, 1), 10, 8, width=7, height=5, rng=rng)                     # drawn on a canvas
    evo.lande_arnold(z, w)                                                           # beta, gamma, SEs

Model (diploid, N individuals = 2N gene copies, additive/genic selection): an allele with selection
coefficient s changes deterministically as p' = p (1 + s) / (1 + s p) (so dp ~ s p q per generation), then
the next generation is a binomial sample of 2N copies. Kimura's diffusion approximation gives the
fixation probability u(p) = (1 - exp(-4 N s p)) / (1 - exp(-4 N s)), which is p when s = 0 and about 2s
for a new beneficial mutation (p = 1/2N) when N s >> 1 (Haldane).
"""

import math

import numpy as np
from matplotlib.patches import Circle

from . import palette as P

# ------------------------------------------------------------------ Wright-Fisher


def _select(p, s):
    return p * (1 + s) / (1 + s * p)


def wright_fisher(N, s=0.0, p0=0.5, generations=100, reps=10, rng=None):
    """Allele-frequency trajectories, shape (generations + 1, reps), in a diploid population of N."""
    rng = rng or np.random.default_rng(0)
    out = np.empty((generations + 1, reps))
    p = np.full(reps, float(p0))
    out[0] = p
    for g in range(1, generations + 1):
        p = rng.binomial(2 * N, _select(p, s)) / (2 * N)
        out[g] = p
    return out


def deterministic(s, p0, generations):
    """The infinite-population trajectory p_t under the same selection model."""
    p = np.empty(generations + 1)
    p[0] = p0
    for g in range(generations):
        p[g + 1] = _select(p[g], s)
    return p


def fixation_probability(N, s, p0, reps=20000, rng=None, max_generations=100000):
    """Simulated probability that an allele at frequency p0 fixes (run until every replicate is absorbed).

    Returns (u, lo, hi): the fraction fixed and its 95 % Wilson interval."""
    rng = rng or np.random.default_rng(0)
    k = np.full(reps, int(round(p0 * 2 * N)))
    fixed = 0
    for _ in range(max_generations):
        k = rng.binomial(2 * N, _select(k / (2 * N), s))
        fixed += int((k == 2 * N).sum())
        k = k[(k > 0) & (k < 2 * N)]
        if not len(k):
            break
    return (fixed / reps, *wilson(fixed, reps))


def wilson(x, n, z=1.959964):
    """95 % Wilson score interval of a binomial proportion x / n."""
    p = x / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def kimura_u(p, N, s, Ne=None):
    """Kimura's fixation probability (1 - e^(-4 Ne s p)) / (1 - e^(-4 Ne s)) (p itself when s = 0)."""
    Ne = N if Ne is None else Ne
    s = np.asarray(s, float)
    a = 4 * Ne * s
    with np.errstate(divide="ignore", invalid="ignore"):
        u = -np.expm1(-a * p) / -np.expm1(-a)
    return np.where(np.abs(a) < 1e-9, p, u)


def heterozygosity(H0, N, t):
    """Expected heterozygosity under pure drift: H_t = H_0 (1 - 1/(2N))^t."""
    return H0 * (1 - 1 / (2 * N)) ** np.asarray(t, float)


def genealogy(ax, origin, N, generations, width=6.0, height=5.0, p0=0.5, s=0.0, tokens=("dna", "rna"), r=None,
              rng=None, trace=True, zorder=8):
    """A Wright-Fisher genealogy: rows of N haploid gene copies (oldest at the top), each copy linked to
    a parent drawn at random from the row above (weighted by fitness 1 + s for allele 1). Copies are
    coloured by allele (``tokens`` = allele 0, allele 1); with ``trace`` the ancestry of the last row is
    drawn in ink and all other links faintly, which shows drift and coalescence at once.

    Returns dict(xy=array (generations, N, 2), allele=array (generations, N), parents=array, freq=list).
    """
    rng = rng or np.random.default_rng(0)
    x0, y0 = origin
    r = r if r is not None else min(width / N, height / generations) * 0.28
    xs = x0 + (np.arange(N) + 0.5) * width / N
    ys = y0 + height - (np.arange(generations) + 0.5) * height / generations
    allele = np.zeros((generations, N), int)
    allele[0, : int(round((1 - p0) * N))] = 0
    allele[0, int(round((1 - p0) * N)):] = 1
    rng.shuffle(allele[0])
    parents = np.zeros((generations, N), int)
    for g in range(1, generations):
        w = np.where(allele[g - 1] == 1, 1 + s, 1.0)
        par = rng.choice(N, N, p=w / w.sum())
        # sort children by parent so that lines rarely cross (positions are arbitrary in the model)
        par = np.sort(par)
        parents[g] = par
        allele[g] = allele[g - 1, par]
    # ancestry of the last row
    anc = np.zeros((generations, N), bool)
    anc[-1] = True
    for g in range(generations - 1, 0, -1):
        anc[g - 1, parents[g][anc[g]]] = True
    faint = P.mix(P.muted(), P.surface(), 0.55)
    for g in range(1, generations):
        for i in range(N):
            j = parents[g, i]
            on = trace and anc[g, i]
            ax.plot([xs[j], xs[i]], [ys[g - 1] - r, ys[g] + r], color=P.ink() if on else faint, lw=1.0 if on else 0.6,
                    zorder=zorder + (1 if on else 0), solid_capstyle="round")
    for g in range(generations):
        for i in range(N):
            t = tokens[allele[g, i]]
            ax.add_patch(Circle((xs[i], ys[g]), r, facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.8, zorder=zorder + 2))
    xy = np.stack(np.meshgrid(xs, ys), axis=-1)
    return dict(xy=xy, allele=allele, parents=parents, freq=list(allele.mean(axis=1)), rows=ys, r=r)


# ------------------------------------------------------------------ quantitative traits


def normal_pdf(z, mu=0.0, sd=1.0):
    return np.exp(-0.5 * ((np.asarray(z, float) - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))


def fitness(z, mode, theta=0.0, width=1.0, strength=1.0):
    """Survival probability of trait value z (in units of the phenotypic SD): ``mode`` "directional"
    (logistic, increasing), "stabilizing" (Gaussian peak at theta) or "disruptive" (Gaussian dip)."""
    z = np.asarray(z, float)
    if mode == "directional":
        return 1 / (1 + np.exp(-(z - theta) * strength / width))
    g = np.exp(-0.5 * ((z - theta) / width) ** 2)
    if mode == "stabilizing":
        return g
    if mode == "disruptive":
        return 1 - strength * g
    raise ValueError(f"unknown selection mode {mode!r}")


def selected_moments(z, f, w):
    """Mean and variance of a trait density f (on grid z) before and after viability selection w."""
    dz = z[1] - z[0]
    f = f / (f.sum() * dz)
    g = f * w
    g = g / (g.sum() * dz)
    m0, m1 = (z * f).sum() * dz, (z * g).sum() * dz
    v0, v1 = ((z - m0) ** 2 * f).sum() * dz, ((z - m1) ** 2 * g).sum() * dz
    return dict(mean=m0, var=v0, mean_sel=m1, var_sel=v1, S=m1 - m0, density_sel=g)


def lande_arnold(z, w):
    """Lande & Arnold (1983) selection gradients from individual trait values z and fitness w (e.g.
    survival 0/1): z is standardized, w made relative (w / mean w). ``beta`` is the slope of the
    linear regression, ``gamma`` twice the quadratic coefficient of the quadratic regression.
    Returns dict(beta, beta_se, gamma, gamma_se, S) with ordinary least-squares standard errors."""
    z = np.asarray(z, float)
    z = (z - z.mean()) / z.std()
    w = np.asarray(w, float) / np.mean(w)

    def ols(X):
        coef, *_ = np.linalg.lstsq(X, w, rcond=None)
        res = w - X @ coef
        s2 = res @ res / (len(w) - X.shape[1])
        cov = s2 * np.linalg.inv(X.T @ X)
        return coef, np.sqrt(np.diag(cov))

    one = np.ones_like(z)
    c1, se1 = ols(np.c_[one, z])
    c2, se2 = ols(np.c_[one, z, z**2 / 2])
    S = float((w * z).mean())  # selection differential (standardized) = Cov(w, z)
    return dict(beta=c1[1], beta_se=se1[1], gamma=c2[2], gamma_se=se2[2], S=S)


def logistic_fit(z, y, degree=2):
    """Maximum-likelihood logistic regression of survival y (0/1) on a polynomial in z (degree 1 or 2).

    Returns (coef, se, predict): coefficients from the intercept upwards, their standard errors
    (inverse Fisher information) and a function z -> fitted survival probability."""
    from scipy import optimize

    z, y = np.asarray(z, float), np.asarray(y, float)
    X = np.vander(z, degree + 1, increasing=True)

    def nll(b):
        eta = X @ b
        return float(np.sum(np.logaddexp(0, eta) - y * eta))

    def grad(b):
        return X.T @ (1 / (1 + np.exp(-(X @ b))) - y)

    b = optimize.minimize(nll, np.zeros(degree + 1), jac=grad, method="BFGS").x
    pr = 1 / (1 + np.exp(-(X @ b)))
    info = X.T @ (X * (pr * (1 - pr))[:, None])
    se = np.sqrt(np.diag(np.linalg.inv(info)))

    def predict(zz):
        return 1 / (1 + np.exp(-(np.vander(np.asarray(zz, float), degree + 1, increasing=True) @ b)))

    return b, se, predict


__all__ = ["logistic_fit", "wright_fisher", "deterministic", "fixation_probability", "wilson", "kimura_u", "heterozygosity",
           "genealogy", "normal_pdf", "fitness", "selected_moments", "lande_arnold"]

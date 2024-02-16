from dist import Distribution, Binomial, Poisson
from typing import Dict

BINOM = 'Binomial'
POISSON = 'Poisson'

DIST_NAMES = [
    BINOM,
    POISSON,
    # 'Geometric',
    # 'Negative Binomial',
    # 'Normal',
    # 'Uniform',
    # 'Exponential',
    # 'Beta',
    # 'Gamma',
]
DIST_NAMES.sort()

INITIAL_DISTRIBUTION: str = BINOM

D2I: Dict[str, int] = {d: i for i, d in enumerate(DIST_NAMES)}
I2D: Dict[int, str] = {i: d for d, i in D2I.items()}

DISTNAME2DIST: Dict[str, Distribution] = {
    BINOM: Binomial(),
    POISSON: Poisson(),
}



from dist import Distribution, Binomial, Poisson, Geometric, NegativeBinomial, Normal, Beta, Exponential, Gamma
from typing import Dict, List

BINOM = 'Binomial'
POISSON = 'Poisson'
GEOM = 'Geometric'
NORM = 'Normal'
BETA = 'Beta'

# I don't understand these fully yet. So won't actually display,
NBINOM = 'Negative Binomial'
EXPON = 'Exponential'
GAMMA = 'Gamma'

DIST_NAMES: List[str] = [
    BINOM,
    POISSON,
    GEOM,
    # NBINOM,
    NORM,
    BETA,
    # EXPON,
    # GAMMA,
    # 'Uniform',
]
DIST_NAMES.sort()

INITIAL_DISTRIBUTION: str = BINOM

D2I: Dict[str, int] = {d: i for i, d in enumerate(DIST_NAMES)}
I2D: Dict[int, str] = {i: d for d, i in D2I.items()}

DISTNAME2DIST: Dict[str, Distribution] = {
    BINOM: Binomial(),
    POISSON: Poisson(),
    GEOM: Geometric(),
    NBINOM: NegativeBinomial(),
    NORM: Normal(),
    BETA: Beta(),
    EXPON: Exponential(),
    GAMMA: Gamma(),
}



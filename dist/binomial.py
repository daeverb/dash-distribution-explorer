from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import binom
import numpy as np

# Description compiled through chatgpt
markdown_description = """
**What It Is:** The binomial distribution models the number of successes in a fixed number of independent trials, each with the same probability of success. It's like flipping a coin multiple times and counting how many times it lands on heads.

**Key Features:**
- **Type:** Discrete.
- **Trials:** Must be a fixed number, $n$.
- **Success or Failure:** Each trial has two possible outcomes (binary).
- **Constant Probability:** The probability of success, $p$, remains the same in each trial.
- **Independence:** The outcome of one trial doesn’t affect another.

**Real-life Example:** Consider a survey asking if people like ice cream. If you ask 100 people and 60% generally do, the binomial distribution can predict the likelihood of 70 people saying "yes".

**Parameters and PMF:**
- **Key Parameters:** Number of trials $n$, probability of success in each trial $p$.
- **PMF:** $P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}$ where $k$ is the number of successes and $\\binom{n}{k}=\\frac {n!}{k!(n-k)!}$, read as $n$ choose $k$.
  - *$n$ choose $k$:* In how many ways you can pick a group of $k$ items from a larger set of $n$ items, without caring about the order in which you pick them.
"""


class Binomial(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = binom
        self.parameters = dict(
            n=dict(
                min=1,
                max=100,
                value=20,
                step=1,
                type='integer',
            ),
            p=dict(
                min=0.0,
                max=1.0,
                value=0.5,
                step=0.01,
                type='float'
            )
        )

    def density_xy(self, **kwargs):
        """
        pmf(k, n, p, loc=0)
        :param kwargs:
            n <- number of trials
            p <- probability of success
        :return:
        """
        n = kwargs['n']
        p = kwargs['p']
        x = np.arange(0, n+1)
        y = self.fn.pmf(k=x, n=n, p=p)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(k, n, p, loc=0)
        :param kwargs:
        :return:
        """
        n = kwargs['n']
        p = kwargs['p']
        x = np.arange(0, n + 1)
        y = self.fn.cdf(k=x, n=n, p=p)
        return x, y

    def get_density_figure(self, **kwargs):
        # Setup based figure
        fig = go.Figure(
            layout=BASE_FIGURE_LAYOUT
        )

        # Add trace
        x, y = self.density_xy(**kwargs)
        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                #mode='lines'
            )
        )

        # Update layout
        fig.update_layout(
            title=dict(
                text='PMF',
                x=0.5,
                xanchor='center',
            ),
            xaxis=dict(
                range=[0, max(x)],
                title=dict(text=r'successes (k)')
            ),
            yaxis=dict(
                range=[0, max(y)*1.1],
                title=dict(text='density')
            )
        )

        # Return results
        return fig

    def get_cumulative_figure(self, **kwargs):
        # Setup based figure
        fig = go.Figure(
            layout=BASE_FIGURE_LAYOUT
        )

        # Add trace
        x, y = self.cdf_xy(**kwargs)
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode='lines'
            )
        )

        # Update layout
        fig.update_layout(
            title=dict(
                text='CDF',
                x=0.5,
                xanchor='center',
            ),
            xaxis=dict(
                range=[0, max(x)],
                title=dict(text="successes (k)")
            ),
            yaxis=dict(
                range=[0, max(y)*1.1],
                title=dict(text='probability')
            )
        )

        # Return results
        return fig

    def get_figures(self, **kwargs):
        density = self.get_density_figure(**kwargs)
        cumulative = self.get_cumulative_figure(**kwargs)
        return density, cumulative


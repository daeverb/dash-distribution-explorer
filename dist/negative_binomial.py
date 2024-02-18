from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import nbinom
import numpy as np

# Description compiled through chatgpt
markdown_description = """
## NOTE: Note fully implemented yet. I have no clue about this one yet.
**What It Is:** This distribution extends the geometric distribution by modeling the number of trials needed to achieve a specified number of successes, rather than just the first success.

**Key Features:**
- **Type:** Discrete.
- **Successes Required:** The target number of successes, $r$, is specified.
- **Success Probability:** Each trial has a constant probability of success, $p$.

**Real-life Example:** If a scientist needs 5 bacteria samples to exhibit a certain trait that has a 20% chance of occurring, the negative binomial distribution can predict how many samples they must observe on average.

**Parameters and PMF:**
- **Key Parameters:** Number of successes $r$, probability of success in each trial $p$.
- **PMF:** $P(X = k) = \\binom{k-1}{r-1} p^r (1-p)^{k-r}$ where $k$ is the total number of trials.
"""


class NegativeBinomial(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = nbinom
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

        # Setup x-range
        samples = np.arange(0, 1000)
        cdf: np.ndarray = self.fn.cdf(k=samples, n=n, p=p)
        msk = ~((1 - cdf) < 0.001)
        max_index = msk.sum()

        # Draw sampels
        x = np.arange(0, max_index)

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

        # Setup x-range
        samples = np.arange(0, 1000)
        cdf: np.ndarray = self.fn.cdf(k=samples, n=n, p=p)
        msk = ~((1 - cdf) < 0.001)
        max_index = msk.sum()

        # Draw samples
        x = np.arange(0, max_index)
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
                title=dict(text=r'successes (r)')
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
                title=dict(text="successes (r)")
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


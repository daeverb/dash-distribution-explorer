from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import geom
import numpy as np

# Description compiled through chatgpt
markdown_description = """
**What It Is:** The geometric distribution models the number of trials needed to achieve the first success in a series of independent Bernoulli trials, each with the same probability of success.

**Key Features:**
- **Type:** Discrete.
- **Success Probability:** Constant probability of success in each trial, $p$.
- **Trial Count:** Focuses on the count until the first success.

**Real-life Example:** If there's a 10% chance of raining each day, the geometric distribution can tell you the probability that the first rain will happen on the fifth day.

**Parameters and PMF:**
- **Key Parameters:** Probability of success in each trial $p$.
- **PMF:** $P(X = k) = (1-p)^{k-1}p$ where $k$ is the number of trials until the first success.
"""


class Geometric(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = geom
        self.parameters = dict(
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
        pmf(k, p, loc=0)
        :param kwargs:
            mu <- mean (lambda)
        :return:
        """
        p = kwargs['p']

        # Setup x-range
        samples = np.arange(0, 1000)
        cdf: np.ndarray = self.fn.cdf(k=samples, p=p)
        msk = ~((1 - cdf) < 0.001)
        max_index = msk.sum()

        # Draw sampels
        x = np.arange(0, max_index)
        y = self.fn.pmf(k=x, p=p)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(k, mu, loc=0)
        :param kwargs:
        :return:
        """
        p = kwargs['p']

        # Setup x-range
        samples = np.arange(0, 1000)
        cdf: np.ndarray = self.fn.cdf(k=samples, p=p)
        msk = ~((1 - cdf) < 0.001)
        max_index = msk.sum()

        # Draw samples
        x = np.arange(0, max_index)
        y = self.fn.cdf(k=x, p=p)
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
                title=dict(text=r'successes (k)')
            ),
            yaxis=dict(
                range=[0, max(y)*1.1],
                title=dict(text=r'probability (p)')
            )
        )

        # Return results
        return fig

    def get_figures(self, **kwargs):
        density = self.get_density_figure(**kwargs)
        cumulative = self.get_cumulative_figure(**kwargs)
        return density, cumulative


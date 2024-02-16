from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import poisson
import numpy as np

# Description compiled through chatgpt
markdown_description = """
**What It Is:** The Poisson distribution measures the probability of a given number of events happening in a fixed interval of time or space, assuming these events occur with a known average rate and independently of the time since the last event.

**Key Features:**
- **Type:** Discrete.
- **Interval:** Time or space where events occur.
- **Rate:** Average number of occurrences in a given interval, $\lambda$.
- **Independence:** Events occur independently.

**Real-life Example:** If a bakery sells an average of 30 cakes per day, the Poisson distribution can estimate the probability of selling exactly 25 cakes tomorrow.

**Parameters and PMF:**
- **Key Parameters:** Average rate of success $\lambda$ (mu, or $\mu$).
- **PMF:** $P(X = k) = \\frac{\lambda^k e^{-\lambda}}{k!}$ where $k$ is the number of events.
"""


class Poisson(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = poisson
        self.parameters = dict(
            mu=dict(
                min=0,
                max=100,
                value=4,
                step=1,
                type='integer'
            )
        )

    def density_xy(self, **kwargs):
        """
        pmf(k, mu, loc=0)
        :param kwargs:
            mu <- mean (lambda)
        :return:
        """
        mu = kwargs['mu']
        x = np.arange(0, mu * 2 + 10)
        y = self.fn.pmf(k=x, mu=mu)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(k, mu, loc=0)
        :param kwargs:
        :return:
        """
        mu = kwargs['mu']
        x = np.arange(0, mu * 2 + 10)
        y = self.fn.cdf(k=x, mu=mu)
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
                title=dict(text=r'$k$ successes')
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
                title=dict(text=r'$k$ successes')
            ),
            yaxis=dict(
                range=[0, max(y)*1.1],
                title=dict(text=r'probability $p$')
            )
        )

        # Return results
        return fig

    def get_figures(self, **kwargs):
        density = self.get_density_figure(**kwargs)
        cumulative = self.get_cumulative_figure(**kwargs)
        return density, cumulative


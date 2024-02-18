from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import beta
import numpy as np

# Description compiled through chatgpt
markdown_description = """
**What It Is:** The beta distribution models probabilities that vary within a 0 to 1 interval, useful for modeling events with uncertain probabilities, especially in Bayesian statistics.

**Key Features:**
- **Type:** Continuous.
- **Shape Parameters ($\\alpha$ and $\\beta$)**: Control the distribution's shape, allowing it to assume a variety of forms from uniform to skewed.
- **Versatility:** It can model a wide range of probability distributions on $[0, 1]$, making it particularly useful for representing proportions or percentages with uncertainty.

**Real-life Example:** When launching a new product, a company might use past launch data to model the probability of achieving different market share levels within the first year. The Beta distribution, with parameters shaped by prior successes ($\\alpha$) and failures ($\\beta$), can estimate the probability of capturing any specific percentage of the market: plot the pdf's from AB-testing (i.e. one with $\\alpha_A$ and $\\beta_A$, and one with $\\alpha_B$ and $\\beta_B$).

**Parameters and PDF:**
- **Key Parameters:** Shape parameters $\\alpha$ and $\\beta$, which determine the shape of the distribution.
- **PDF:** $f(x) = \\frac{x^{\\alpha-1}(1-x)^{\\beta-1}}{B(\\alpha, \\beta)}$ for $x$ in $[0, 1]$, where $B(\\alpha, \\beta)$ is the Beta function.
"""


class Beta(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = beta
        self.parameters = dict(
            a=dict(
                min=0.01,
                max=100.0,
                value=2.31,
                step=0.01,
                type='float',
            ),
            b=dict(
                min=0.01,
                max=100.0,
                value=0.627,
                step=0.01,
                type='float'
            )
        )

    def density_xy(self, **kwargs):
        """
        pdf(x, a, b, loc=0, scale=1)
        :param kwargs:
            a <- alpha
            b <- beta
        :return:
        """
        a = kwargs['a']
        b = kwargs['b']
        x = np.linspace(start=0, stop=1, num=1000)
        y = self.fn.pdf(x=x, a=a, b=b)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(x, loc=0, scale=1)
        :param kwargs:
        :return:
        """
        a = kwargs['a']
        b = kwargs['b']
        x = np.linspace(start=0, stop=1, num=1000)
        y = self.fn.cdf(x=x, a=a, b=b)
        return x, y

    def get_density_figure(self, **kwargs):
        # Setup based figure
        fig = go.Figure(
            layout=BASE_FIGURE_LAYOUT
        )

        # Add trace
        x, y = self.density_xy(**kwargs)
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
                text='PDF',
                x=0.5,
                xanchor='center',
            ),
            xaxis=dict(
                range=[0, 1.0],
                title=dict(text=r'x')
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
                range=[0, 1.0],
                title=dict(text="x")
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


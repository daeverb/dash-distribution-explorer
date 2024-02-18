from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import norm
import numpy as np

# Description compiled through chatgpt
markdown_description = """
**What It Is:** The normal distribution models a continuous variable where most observations cluster around a central mean value, with probabilities for values further from the mean decreasing symmetrically.

**Key Features:**
- **Type:** Continuous.
- **Mean ($\mu$) and Standard Deviation ($\sigma$):** Determine the distribution's center and width.
- **Symmetry:** The distribution is symmetric about the mean.
- **Bell Shape:** The characteristic "bell curve" shape.

**Real-life Example:** Adult heights within a specific gender and population tend to follow a normal distribution, with most people being of average height and fewer people being extremely tall or short.

**Parameters and PDF:**
- **Key Parameters:** Mean $\mu$ (loc), standard deviation $\sigma$ (scale).
- **PDF:** $f(x) = \\frac{1}{\sigma\sqrt{2\pi}} e^{-\\frac{1}{2}\left(\\frac{x-\mu}{\sigma}\\right)^2}$
"""


class Normal(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = norm
        self.parameters = dict(
            loc=dict(
                min=-3.0,
                max=3.0,
                value=0,
                step=0.01,
                type='float',
            ),
            scale=dict(
                min=0.0,
                max=3.0,
                value=1.0,
                step=0.01,
                type='float'
            )
        )

    def density_xy(self, **kwargs):
        """
        pdf(x, loc=0, scale=1)
        :param kwargs:
            loc <- mean
            scale <- std
        :return:
        """
        loc = kwargs['loc']
        scale = kwargs['scale']
        x = np.linspace(start=-6, stop=6, num=1000)
        y = self.fn.pdf(x=x, loc=loc, scale=scale)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(x, loc=0, scale=1)
        :param kwargs:
        :return:
        """
        loc = kwargs['loc']
        scale = kwargs['scale']
        x = np.linspace(start=loc - scale * 6, stop=loc + scale * 6, num=1000)
        y = self.fn.cdf(x=x, loc=loc, scale=scale)
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
                range=[-6, 6],
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
                showgrid=True,
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


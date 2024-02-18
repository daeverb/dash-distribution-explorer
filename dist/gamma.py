from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import gamma
import numpy as np

# Description compiled through chatgpt
markdown_description = """
## NOTE: Note fully implemented yet. I have no clue about this one yet.
**What It Is:** The Gamma distribution is a two-parameter family of continuous probability distributions that extends the exponential distribution for modeling waiting times over multiple events. It's particularly useful when the event rate ($\lambda$) varies.

**Key Features:**
- **Type:** Continuous.
- **Shape and Scale Parameters ($k$ and $\\theta$):** $k$ (or $\\alpha$) shapes the distribution, and $\theta$ (scale) stretches or compresses it horizontally. These parameters allow the Gamma distribution to adapt to different types of skewed data.
- **Flexibility:** Can model a wide range of processes, from skewed distributions like service times in a system to the amount of rainfall accumulated in a reservoir over time.

**Real-life Example:** In healthcare, the Gamma distribution can model the length of stay of patients in a hospital for different conditions. By adjusting the shape and scale parameters based on historical data, administrators can better predict patient flows and manage resources, such as bed availability and staffing needs.

**Parameters and PDF:**
- **Key Parameters:** shape parameter ($k$ or $\\alpha$) influences the form of the distribution, and scale parameter ($\\theta$) determines the stretch or compression of the distribution on the horizontal axis, affecting the dispersion of data points.
- **PDF:** $f(x; k, \\theta) = \\frac{x^{k-1}e^{-x/\\theta}}{\\theta^k \Gamma(k)}$ for $x \ge 0$, where $\Gamma(k)$ is the gamma function, a generalization of factorial that interpolates the factorial function for non-integer values of $k$. 
"""


class Gamma(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = gamma
        self.parameters = dict(
            a=dict(
                min=0.01,
                max=100.0,
                value=4,
                step=0.01,
                type='float',
            ),
            scale=dict(
                min=0.01,
                max=100.0,
                value=1.0,
                step=0.01,
                type='float',
            ),
        )

    def density_xy(self, **kwargs):
        """
        pdf(x, a, loc=0, scale=1)
        :param kwargs:
            a <- alpha
        :return:
        """
        a = kwargs['a']
        scale = kwargs['scale']
        x = np.linspace(start=0, stop=100, num=1000)
        y = self.fn.pdf(x=x, a=a, scale=scale)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(x, loc=0, scale=1)
        :param kwargs:
        :return:
        """
        a = kwargs['a']
        scale = kwargs['scale']
        x = np.linspace(start=0, stop=100, num=1000)
        y = self.fn.cdf(x=x, a=a, scale=scale)
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
                range=[min(x), max(x)],
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
                range=[min(x), max(x)],
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


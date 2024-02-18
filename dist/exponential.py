from . import Distribution, BASE_FIGURE_LAYOUT
import plotly.graph_objects as go
from scipy.stats import expon
import numpy as np

# Description compiled through chatgpt
markdown_description = """
## NOTE: Note fully implemented yet. I have no clue about this one yet.
**What It Is:** The exponential distribution models the time between events in a Poisson process, describing the intervals between independent events that happen at a constant average rate.

**Key Features:**
- **Type:** Continuous.
- **Rate Parameter ($\lambda$)**: Determines the average rate of events per time unit.
- **Memoryless Property:** The probability of an event occurring in the future is independent of how much time has already elapsed.

**Real-life Example:** The time between earthquakes in a given region can be modeled with an exponential distribution if they occur independently and at a constant average rate.

**Parameters and PDF:**
- **Key Parameters:** Rate parameter $\lambda$ (the reciprocal of the mean).
- **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.
"""


class Exponential(Distribution):
    def __init__(self):
        self.description = markdown_description
        self.fn = expon
        self.parameters = dict(
            rate=dict(
                min=0.01,
                max=1.0,
                value=0.05,
                step=0.01,
                type='float',
            ),
            loc=dict(
                min=-100,
                max=100.0,
                value=0,
                step=0.01,
                type='float',
            ),
            scale=dict(
                min=0.01,
                max=100.0,
                value=1,
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
        loc = kwargs['loc']
        scale = kwargs['scale']
        rate = kwargs['rate']
        x = np.linspace(start=-100, stop=100, num=1000)
        y = rate * self.fn.pdf(x=x, loc=loc, scale=scale)
        return x, y

    def cdf_xy(self, **kwargs):
        """
        cdf(x, loc=0, scale=1)
        :param kwargs:
        :return:
        """
        loc = kwargs['loc']
        scale = kwargs['scale']
        x = np.linspace(start=-100, stop=100, num=1000)
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
                range=[-100, 100],
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


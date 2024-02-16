from abc import ABC, abstractmethod


class Distribution(ABC):
    @abstractmethod
    def density_xy(self, **kwargs):
        """
        Returns the x and y values for the density plot.
        Either pdf or pmf

        :param kwargs: key-words arguments for density function
        :return:
        x : np.ndarray
        y : np.ndarray
        """
        raise NotImplementedError

    @abstractmethod
    def cdf_xy(self, **kwargs):
        """
        Returns the x and y values for the cumulative density ploy.
        Either pdf or pmf

        :param kwargs: key-words arguments for cumulative density function
        :return:
        x : np.ndarray
        y : np.ndarray
        """
        raise NotImplementedError

    @abstractmethod
    def get_density_figure(self, **kwargs):
        """
        return the density plot
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_cumulative_figure(self, **kwargs):
        """
        return the cumulative probability plot
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_figures(self, **kwargs):
        """
        Returns all figures based on kwargs
            1. Density plot
            2. Cumulative plot
        :param kwargs:
        :return:
        """
        raise NotImplementedError


"""
This script compute the VaR with linear model.
At the end there is an example.
"""
from scipy.stats import norm
import numpy as np
from BrownianMotion import BrownianMotion


class VaRLinear:
    """
    Class which compute the VaR with linear model form a list of spot and
    values of portfolio for each spot.
    """

    def __init__(self):
        "VaRLinear class constructor"
        self.__version__ = "1.0.0"

    def VaROne(self, X, T, alpha):
        stdX = np.std(X)
        var = norm(0, 1).ppf(alpha) * stdX * np.sqrt(T)
        return var

    def covarMatrix(self, spots: list = []):
        "Return the covariance matrix from the list of spots in paramater"
        return np.cov(spots)

    def VaR(self, spots: list = [], nbAssets: list = [], alpha: float = 0.99, T: int = 1):
        """
        Return the Value-at-risk (VaR) of the given spots.

        Inputs:
        - spots (list): mandatory, list of lists of spots
        - nbAssets (list): mandatory, list of number onwed assets
        - alpha (float): mandatory, the inverse of lossing probability

        Ouputs:
        - VaR (value at risk), the losing of the portfolio under 1 day horizon.
        """

        C = self.covarMatrix(spots)

        A = np.array(nbAssets)
        A = A.reshape(len(A), 1)

        sigP2 = np.sqrt(np.dot(np.dot(A.T, C), A))

        var = norm.ppf(alpha) * np.sqrt(T) * sigP2

        return var[0][0]

if __name__ == "__main__":

    bw = BrownianMotion()
    bw.T = 1
    bw.mu = 0
    bw.sigma = 0.2
    bw.S0 = 100
    bw.dt = 1/252

    S1 = bw()   # cac40 spot
    S2 = bw()   # oil brent spot
    S3 = bw()   # silver spot
    spots = np.array([S1, S2, S3])

    nb1 = 3
    nb2 = 100
    nb3 = 50

    nbAssets = [nb1, nb2, nb3]

    vl = VaRLinear()

    alpha = 0.99
    T = 1

    VaR = vl.VaR(nbAssets, spots, alpha, T)

    print("portfolio value: {0}".format(S1[-1] * nb1 + S2[-1] * nb2 + S3[-1] * nb3))
    print("VaR: {0}".format(VaR))

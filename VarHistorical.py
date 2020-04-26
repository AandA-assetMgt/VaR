"""
This script compute the historical VaR.
At the end there is an example.
"""
from BrownianMotion import BrownianMotion


class VaRHistorical:
    """
    Class which compute the historial VaR form a list of spot and
    values of portfolio for each spot.
    """
    def __init__(self):
        "VaRHistorical class constructor"
        self.__version__ = "1.0.0"

    def _selectVaR(self, vars, alpha):
        vars.sort()
        return vars[int(len(vars) * alpha)]

    def VaR(self, spots, values, alpha):
        """
        Return the Value-at-risk (VaR) of the given spots.

        Inputs:
        - spots (list): mandatory, list of lists of spots
        - values (list): mandatory, list of portfolio values for each spots
        - alpha (float): mandatory, the inverse of lossing probability

        Ouputs:
        - VaR (value at risk), the losing of the portfolio under 1 day horizon.
        """
        initalValue = sum([spots[i][-1] * values[i] for i in range(len(values))])
        deltas = []

        for i in range(len(spots[0])-1):

            newValue = initalValue + sum([values[j] * (spots[j][i+1] / spots[j][i]) for j in range(len(values))])

            deltas.append(sum(values) - (newValue - initalValue))

        vvar = self._selectVaR(deltas, alpha)

        return vvar

if __name__ == "__main__":

    # generate data
    bw = BrownianMotion()
    bw.T = 1
    bw.mu = 0
    bw.sigma = 0.2
    bw.S0 = 100
    bw.dt = 1/252

    S1 = bw()   # cac40 spot
    n1 = 300    # cac40 asset owned

    S2 = bw()   # oil brent spot
    n2 = 150    # oil asset owned

    S3 = bw()   # silver spot
    n3 = 500    # silver owned

    spots = [S1, S2, S3]

    spots = [S1, S2, S3]                              # spots
    values = [n1 * S1[-1], n2 * S2[-1], n3 * S3[-1]]  # current portfolio value
    alpha = 0.99                                      # confidence level

    #  compute curent VaR
    vh = VaRHistorical()
    var = vh.VaR(spots, values, alpha)

    print(var)

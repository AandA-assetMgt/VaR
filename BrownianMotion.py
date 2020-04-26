"""
This class generate a brownian motion vector.
It depend of some parameter.
"""

import numpy as np


class BrownianMotion:
    """
    Generate a brownian motion in function of paramters:
    - T (float): time in year.
    - mu (float): mean of the generate vector. A real brownian motion have mu = 0.
    - sigma (float): volatility of the motion.
    - S0 (float): start value.
    - dt (float): delta of time. If you want a motion onver 1 work year you must write : dt = 1/252

    Default values
    - T = 0
    - mu = 0
    - sigma = 0
    - S0 = 0
    - dt = 1

    Using:

    bw = BorwnianMotion()
    bw.T = 1
    bw.mu = 0
    bw.sigma = 0.2
    bw.S0 = 100
    bw.dt = 1/252

    S = bw()

    A.L - 19FEB20
    """

    def __init__(self, T: float = 0, mu: float = 0, sigma: float = 0, S0: float = 0, dt: float = 1):
        self.T = T
        self.mu = mu
        self.sigma = sigma
        self.S0 = S0
        self.dt = dt

    def __call__(self):
        """
        Return T/dt element which is the bronian motion depend of attributes.

        Inputs:
        - None

        Outputs:
        - the brownian motion as numpy array.
        """
        N = round(self.T / self.dt)
        X = np.random.normal(self.mu * self.dt, self.sigma * np.sqrt(self.dt), N)
        X = np.cumsum(X)
        S = self.S0 * np.exp(X)
        return S

if __name__ == "__main__":
    
    bw = BrownianMotion()
    bw.T = 1
    bw.mu = 0
    bw.sigma = 0.2
    bw.S0 = 100
    bw.dt = 1/252

    S1 = bw()
    S2 = bw()
    S3 = bw()

    print(S1)
    print(S2)
    print(S3)

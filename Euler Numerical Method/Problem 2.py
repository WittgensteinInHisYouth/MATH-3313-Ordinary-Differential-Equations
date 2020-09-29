import numpy as np
from EulerMethod import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # h = 0.5
    # for i in range(5):
    #     func1 = EulerNumericalSolution("h", h / 2**i, lambda x, t: np.sin(x+t), 0, 10, 1)
    #     func1.plot(f"h= {h / 2**i}")
    h = 0.03125
    func = EulerNumericalSolution("h", h, lambda x, t: np.sin(x + t), 0, 10, 1)
    func.plot(f"h= {h}")
    plt.legend()
    plt.savefig("Problem 2.png")
    plt.show()
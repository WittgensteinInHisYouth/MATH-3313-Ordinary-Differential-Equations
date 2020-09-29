import numpy as np
from EulerMethod import *
import matplotlib.pyplot as plt

def AnalyticSolution(x):
    return np.exp(2*x) - 5/2

if __name__ == "__main__":
    func1 = EulerNumericalSolution("h", 0.1, lambda x, t: 2*x+5, -1, 2, np.exp(-2)-5/2)
    func1.plot("a")
    func2 = EulerNumericalSolution("h", 0.05, lambda x, t: 2*x+5, -1, 2, np.exp(-2)-5/2)
    func2.plot("b")
    func3 = EulerNumericalSolution("N", 100, lambda x, t: 2*x+5, -1, 2, np.exp(-2)-5/2)
    func3.plot("c")
    ts = np.linspace(-1, 2, 1000)
    plt.plot(ts, list(map(AnalyticSolution, ts)), label="Analytic Solution")
    plt.legend()
    plt.savefig("Problem 1.png")
    plt.show()
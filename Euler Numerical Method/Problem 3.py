import numpy as np
from EulerMethod import *
import matplotlib.pyplot as plt
import os
my_path = os.path.abspath(__file__)  # Figures out the absolute path for you in case your working directory moves around.
if __name__ == "__main__":
    h = 0.1
    for x_init in [2, 1.5, 1]:
        func = EulerNumericalSolution("h", h, lambda x, t: np.cos(t)/x, 0, 10, x_init)
        func.plot(f"x(0)= {x_init}")
    plt.legend()
    plt.savefig("Problem 3.png")
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
class EulerNumericalSolution():
    def __init__(self, type, val, f, t_min, t_max, x_init):
        if type == "h":
            self.h = val
            self.n = int((t_max-t_min)/ self.h)
        elif type == "N":
            self.n = val
            self.h = (t_max - t_min) / self.n
        self.t_min = t_min
        self.t_max = t_max
        self.x_init = x_init
        self.f = f

    def simulate(self):
        ts, xs = [self.t_min], [self.x_init]
        cur_t = self.t_min
        cur_x = self.x_init

        for iteration in range(self.n):
            cur_x += self.f(cur_x, cur_t) * self.h
            cur_t += self.h
            ts.append(cur_t)
            xs.append(cur_x)

        return ts, xs

    def plot(self, legend):
        ts, xs = self.simulate()
        plt.plot(ts, xs, label=legend)
        plt.title("Comparison result")
        plt.xlabel("t")
        plt.ylabel("x")
        plt.grid()
        #plt.show()


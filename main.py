
import gaussian as g
import matplotlib.pyplot as plt
import numpy as np

ROI = 128

t0 = 256 - ROI
t1 = 258 + ROI

rng = t1 - t0

m1 = mu = Ex = 0
m2 = var = 1000
sigma = np.sqrt(var)

if __name__ == "__main__":

    signal = np.array(g.normal(mu, sigma, 512)[t0:t1])
    signal = signal / np.max(signal)
    m0 = np.sum(signal)
    mean = np.sum(signal * m0)
    output = g.normal(mean, sigma, 512)[t0:t1]
    output = output / np.max(output)

    print(f"OG mean = {mu}\nCalculated mean = {mean}")


    plt.figure()
    plt.plot(range(t0,t1), signal, label="input")
    plt.plot(range(t0, t1), output, label="output")
    plt.legend()
    plt.show()

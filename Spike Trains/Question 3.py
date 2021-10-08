import numpy as np
from matplotlib import pyplot as plt

#Define Functions
def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array

def autocorrelogram(x):
    result = np.correlate(x, x, mode='full')
    return result[int((result.size/2)-50):int((result.size/2)+50)]

#Define parameters
ms=0.001
spike_train = load_data("rho.dat", int)
interval = 100*ms
tau_ref = 2*ms


#Plot Output
plt.bar(np.linspace(0, 100, autocorrelogram(
    spike_train[:8000]).size), autocorrelogram(spike_train[:8000]))


plt.title("Spike train Autocorrelogram")

plt.ylabel("Number of spikes")
plt.xlabel("Interval (ms)")
plt.xticks(np.linspace(0, 100, 5), [-100, -50, 0, 50, 100])

plt.show()

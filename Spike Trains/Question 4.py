import numpy as np
import matplotlib.pyplot as plt

#Define Functions
def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array

def compute_sta(stim, rho, width,interval):
    num_timesteps = int(width/interval)
    sd = np.zeros(num_timesteps)
    spike_times = np.nonzero(rho)[0]           
    num = len(spike_times)
    for i in range(0, num_timesteps):
        x=0
        window=[]
        j=0
        while j<num:
            if spike_times[j]<i:
                x+=1
            window.append(stim[spike_times[j]-i])
            j+=1
        sd[i]=sum(window)/(num-x)
    return sd

#Load Input Data
spikes=load_data("rho.dat",int)
stimulus=load_data("stim.dat",float)

#Define parameters
ms=0.001
interval=2*ms
width = 100*ms

#Calculate Spike triggered Average
spike_avg = np.flip(compute_sta(stimulus, spikes, width, interval),axis=0)
time = np.linspace(0, 98, 50,  endpoint=True)

#PLot Data
plt.plot(time, spike_avg)
plt.xlabel('Window (ms)')
plt.ylabel('Spike Triggered Average')
plt.title('Spike Triggered Average over 100ms Window')
plt.show()
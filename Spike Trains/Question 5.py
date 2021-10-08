from numpy import zeros
import numpy as np
import matplotlib.pyplot as plt

#Define Functions
def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array

def calculate_stimulus_average(stim, rho, width,samprat,interval,flag):
    num_timesteps = int(width/samprat)
    stimulus_average = zeros(num_timesteps)
    spike_T = np.nonzero(rho)[0]           #non_zero spikes
    spike_times=[]
    if flag==1:   #spikes are not neccesarily adjacent
        m=0
        s = zeros(len(stim))
        while m < len(spike_T):
            s=spike_T[m]+interval
            if rho[int(s)]!=0:
                spike_times.append(spike_T[m])
            m+=1
    if flag==0:   #spikes are neccesarily adjacent
        m=0
        s = zeros(len(stim))
        while m < len(spike_T):
            s=spike_T[m]+interval
            if rho[int(s)]!=0:
                s1=rho[int(spike_T[m])+1:int(spike_T[m]+interval)]
                if sum(s1)== 0:
                    spike_times.append(spike_T[m])
            m+=1
    num = len(spike_times)
    for i in range(0, num_timesteps):
        x=0
        window=[]
        for j in range(0, num):
            if spike_times[j] - i < 0:
                x += 1
            window.append(stim[spike_times[j] - i])
        stimulus_average[i] = sum(window) / (num - x)
    return stimulus_average

#Load Input Data
stimulus=load_data("stim.dat",float)
spikes=load_data("rho.dat",int)

#Define parameters
ms=1
interval=[2*ms,10*ms,20*ms,50*ms,]
width = 100*ms



stimulus_average_1 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[0]/2,1)
stimulus_average_2 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[1]/2,1)
stimulus_average_3 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[2]/2,1)
stimulus_average_4 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[3]/2,1)
time = [i for i in range (2,101,2)]


#Plot Output for spikes not neccesarily adjacent
plt.plot(time, stimulus_average_1,color='red',label='2ms')
plt.plot(time, stimulus_average_2,color='green',label='10ms')
plt.plot(time, stimulus_average_3,color='black',label='20ms')
plt.plot(time, stimulus_average_4,color='yellow',label='50ms')
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus Average')
plt.title('Spikes are not neccesarily adjacent')
plt.show()

stimulus_average_5 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[0]/2,0)
stimulus_average_6 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[1]/2,0)
stimulus_average_7 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[2]/2,0)
stimulus_average_8 = calculate_stimulus_average(stimulus, spikes, width, 2,interval[3]/2,0)
time = [i for i in range (2,101,2)]

#Plot Output for spikes are adjacent
plt.plot(time, stimulus_average_5,color='red',label='2ms')
plt.plot(time, stimulus_average_6,color='green',label='10ms')
plt.plot(time, stimulus_average_7,color='black',label='20ms')
plt.plot(time, stimulus_average_8,color='yellow',label='50ms')

plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus Average')
plt.title('Spikes are adjacent')
plt.show()

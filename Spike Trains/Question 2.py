import numpy as np

#Define Functions
def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array


def get_fano_factor(data_array,width,interval,big_t):
    width_ = int(width/interval)
    spike_count = []
    k=0
    for i in range(0,int(big_t/width)):
        m=0
        for j in range(k,k+width_):
            if data_array[j] == 1:
                 m += 1
        spike_count.append(m)
        k += width_
    var = np.var(spike_count)
    avg = np.mean(spike_count)
    fano_factor=var/avg
    return fano_factor


def get_coeffcient(data_array,interval):
    k=0
    intervals=[]
    for i in range(0,len(data_array)):
        if data_array[i] == 0:
            k += 1
        else:
            k += 1
            n = k*interval
            intervals.append(n)
            k = 0
    sd=np.std(intervals)
    avg=np.mean(intervals)
    coeff=sd/avg
    return(coeff)

#Define parameters
sec=1.0
ms=0.001
interval=2*ms
big_t=20*60*sec
width = [10*ms,50*ms,100*ms]

#Print Output
spike_train=load_data("rho.dat",int)
print(len(spike_train)/big_t)
print('Data were collected for 20 minutes at a sampling rate of 500 Hz')
coeffcient = get_coeffcient(spike_train,interval)
print('coefficient',coeffcient)
Fano_factor = get_fano_factor(spike_train,width[0],interval,big_t)
print('Fano factor over windows of width 10ms ',Fano_factor)
Fano_factor2 = get_fano_factor(spike_train,width[1],interval,big_t)
print('Fano factor over windows of width 50ms ',Fano_factor2)
Fano_factor3 = get_fano_factor(spike_train,width[2],interval,big_t)
print('Fano factor over windows of width 100ms',Fano_factor3)
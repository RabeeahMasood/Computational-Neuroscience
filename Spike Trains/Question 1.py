import random as rnd
import numpy as np

#Define Functions
def get_spike_train(rate,big_t,tau_ref):
    if 1 <= rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []
    exp_rate = rate/(1-tau_ref*rate)
    spike_train = []
    t=rnd.expovariate(exp_rate)
    while t< big_t:
        spike_train.append(t) 
        t += tau_ref+rnd.expovariate(exp_rate)
    return spike_train


def get_fano_factor(spike_train,width,big_t):
    spike_count = np.zeros(int(big_t/width))
    print(spike_count)
    for i in range(len(spike_train)):
        j = int(spike_train[i]/width)
        spike_count[j] += 1
    var = np.var(spike_count)
    avg = np.mean(spike_count)
    fano_factor = var/avg
    return fano_factor


def get_coeffcient(spike_train):
    interval = []
    for i in range(len(spike_train)-1):
        diff = spike_train[i+1]-spike_train[i]
        interval.append(diff)
    sd = np.std(interval)
    avg = np.mean(interval)
    coeff = sd/avg
    return(coeff)


#Define parameters
sec=1.0
ms=0.001
Hz=1.0
rate=35.0 *Hz 
tau_ref1=5*ms
tau_ref2=0*ms
big_t=1000*sec  
width = [10*ms,50*ms,100*ms]


#Print Output
print('-------------------PART 1 (No refractory period)----------------------')
spike_train=get_spike_train(rate,big_t,tau_ref2)
print(len(spike_train)/big_t)

coeffcient = get_coeffcient(spike_train)
print('Coefficient of Variation: ',coeffcient)
Fano_factor1 = get_fano_factor(spike_train,width[0],big_t)
print('Fano factor over windows of width 10ms:',Fano_factor1)
Fano_factor2 = get_fano_factor(spike_train,width[1],big_t)
print('Fano factor over windows of width 50ms:',Fano_factor2)
Fano_factor3 = get_fano_factor(spike_train,width[2],big_t)
print('Fano factor over windows of width 100ms:',Fano_factor3)

print('----------------PART 2 (With refractory period of 5ms)----------------')
spike_train=get_spike_train(rate,big_t,tau_ref1)
print(len(spike_train)/big_t)

coeffcient = get_coeffcient(spike_train)
print('Coefficient of Variation: ',coeffcient)
Fano_factor1 = get_fano_factor(spike_train,width[0],big_t)
print('Fano factor over windows of width 10ms:',Fano_factor1)
Fano_factor2 = get_fano_factor(spike_train,width[1],big_t)
print('Fano factor over windows of width 150ms:',Fano_factor2)
Fano_factor3 = get_fano_factor(spike_train,width[2],big_t)
print('Fano factor over windows of width 100ms:',Fano_factor3)
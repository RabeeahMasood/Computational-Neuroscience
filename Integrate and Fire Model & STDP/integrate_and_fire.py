import matplotlib.pyplot as plt
import numpy as np
from random import uniform

s = 1             #second
ms = 0.001        #millisecond
mV = 0.001        #milliVolt
MOhm = 1000000
nA = 0.000000001

#Q1

tau_m = 10*ms    #time constant(msec)
E_l = -70*mV     #resting potential
V_t = -40*mV     #spike threshold
R_m = 10*MOhm    #resistance(mOhm)
I_e = 3.1*nA     #input current (A)
dt = 0.25*ms     #simulation time step
V_r = E_l

times = np.arange(0, 1, dt)
# times = np.arange(0, 0.4, dt)
Vs = [V_r]

def differential(V):
    dV = (E_l - V + R_m*I_e)/tau_m
    return dV

for i in times:
    prev = Vs[-1]
    next = prev + differential(prev)*ms
    if (next >= V_t):
        next = V_r

    Vs.append(next)

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)
ax.plot(times, Vs[:len(times)], color = "black", label = "voltage")
ax.axhline(-40*mV, linestyle = "--", alpha = 0.7, label = "threshold", color = "crimson")
ax.axhline(-70*mV, linestyle = "--", alpha = 0.7, label = "leak potential")
ax.legend()
plt.ylim(-75*mV, -20*mV)
plt.xlabel("Time (s)", fontsize = 14)
plt.ylabel("Voltage (V)", fontsize = 14)
ax.tick_params(labelsize=14)
plt.title('Integrate and Fire Model', fontsize=16)
plt.show()
fig.savefig("Int_Fire_1second")

#Q2

tau_m = 20*ms   #time constant (msec)
E_l = -70*mV    #resting potential
V_t = -54*mV    #spike threshold
R_m = 10*MOhm   #resistance
I_e = 3.1*nA    #input current
dt = 0.00025    #timestep
V_r = -80*mV    #reset potential
R_mI_e = 18*mV
Rmgs = 0.15
P = 0.5
ax.legend()
tau_s = 10*ms
s_1 = 0
s_2 = 0
E_excite = 0
E_inhibit = -80*mV

V1s = [uniform(V_r, V_t)]
V2s = [uniform(V_r, V_t)]
times = np.arange(0, 1, dt)

# Need a function for calculating s
def dS(s):
    return -s/tau_s


def neuron(V, s, E_s):
    dV = (E_l - V + R_mI_e + Rmgs*s*(E_s-V))/tau_m
    return dV

for t in times:
    prev_1 = V1s[-1]
    prev_2 = V2s[-1]

    next_1 = prev_1 + neuron(prev_1, s_2, E_excite)*dt
    next_2 = prev_2 + neuron(prev_2, s_1, E_excite)*dt

   # next_1 = prev_1 + neuron(prev_1, s_2, E_inhibit)*dt
   # next_2 = prev_2 + neuron(prev_2, s_1, E_inhibit)*dt

    s_1 = s_1 + dS(s_1) * dt
    s_2 = s_2 + dS(s_2) * dt

    if (next_1 >= V_t):
        next_1 = V_r
        s_1 += P
    V1s.append(next_1)

    if (next_2 >= V_t):
        next_2 = V_r
        s_2 += P
    V2s.append(next_2)

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)
ax.plot(times, V1s[:len(times)], color = "crimson", label = "Neuron 1 Voltage")
ax.plot(times, V2s[:len(times)], color = "mediumblue", label = "Neuron 2 Voltage")
ax.axhline(-54*mV, linestyle = "-.", alpha = 0.7, label = "Firing Threshold", color = "black")
ax.axhline(-80*mV, linestyle = "--", alpha = 0.7, label = "Leak Potential", color = "black")
ax.legend()
ax.tick_params(labelsize=14)
plt.xlabel("Time (seconds)", fontsize = 14)
plt.ylabel("Voltage (V)", fontsize = 14)
plt.ylim(-85*mV, -30*mV)
plt.title('Excitatory Synapse', fontsize=16)
plt.show()
fig.savefig("Int_Fire_Excitatory")

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111)
ax.plot(times, V1s[:len(times)], color = "crimson", label = "Neuron 1 Voltage")
ax.plot(times, V2s[:len(times)], color = "mediumblue", label = "Neuron 2 Voltage")
ax.axhline(-54*mV, linestyle = "-.", alpha = 0.7, label ="Firing Threshold", color = "black")
ax.axhline(-80*mV, linestyle = "--", alpha = 0.7, label = "Leak Potential", color = "black")
ax.legend()
ax.tick_params(labelsize=14)
plt.xlabel("Time (seconds)", fontsize = 14)
plt.ylabel("Voltage (V)", fontsize = 14)
plt.ylim(-85*mV, -30*mV)
plt.title('Inhibitory Synapse', fontsize=16)
plt.show()
fig.savefig("Int_Fire_Inhibitory")


# Q3-1

T = 1*s                        # total time to simulate
dt = 0.25*ms                      # simulation time step
time = np.arange(0, T+dt, dt)  # time array

tau_m = 10.0*ms                # time constant (msec)
El = -70.0*mV                  # resting potential (same as the reset)
Vr = -70.0*mV                  # reset value
Vt = -40.0*mV                  # spike threshold (V)
Rm = 10.0*MOhm                 # resistance (mOhm)

# Ie = 3.00000000000000333067*nA                      # input current (A)

Ie = (Vt-El) / Rm

print('Ie = (Vt-El) / Rm = ' + str(Ie) + '[nA]')

T = 1*s                        # total time to simulate
dt = 0.25*ms                      # simulation time step
time = np.arange(0, T+dt, dt)  # time array

tau_m = 10.0*ms                # time constant (msec)
El = -70.0*mV                  # resting potential (same as the reset)
Vr = -70.0*mV                  # reset value
Vt = -40.0*mV                  # spike threshold (V)
Rm = 10.0*MOhm                 # resistance (mOhm)
Ie = 2.9*nA                    # input current (A)

Vm = np.zeros(len(time))   # potential (V) trace over time
# iterate over each time step
for i, t in enumerate(time):
    Vm[i] = Vm[i-1] + (El - Vm[i-1] + Rm*Ie) * dt / tau_m
    if Vm[i] >= Vt:
        Vm[i] = Vr

# Q3-2

plt.figure(figsize=(10, 5))
plt.plot(time, Vm, label='I_e = 2.9[nA]')
plt.legend(loc='lower right', shadow=False, fontsize='medium')
plt.title('Integrate-and-Fire Model',fontsize=16)
plt.ylabel('Membrane Potential (V)')
plt.xlabel('Time (sec)')
plt.tight_layout()
plt.show()


T = 1*s                        # total time to simulate
dt = 0.25*ms                   # simulation time step
time = np.arange(0, T+dt, dt)  # time array

tau_m = 10.0*ms                # time constant (msec)
El = -70.0*mV                  # resting potential (same as the reset)
Vr = -70.0*mV                  # reset value
Vt = -40.0*mV                  # spike threshold (V)
Rm = 10.0*MOhm                 # resistance (mOhm)

Vm = np.zeros(len(time))   # potential (V) trace over time

countList = []
for Ie in np.arange(2, 5, 0.1):
    count = 0
    for i, t in enumerate(time):
        Vm[i] = Vm[i-1] + (El - Vm[i-1] + Rm*Ie*nA) * dt / tau_m
        if Vm[i] >= Vt:
            Vm[i] = Vr
            count += 1
    countList.append(count)

# Q3-3

plt.figure(figsize=(10, 5))
plt.plot(np.arange(2, 5, 0.1), countList)
plt.title('Firing Rate as a function of Input Current',fontsize=16)
plt.ylabel('the Number of Spikes')
plt.xlabel('Current Input (nA)')
plt.tight_layout()
plt.show()


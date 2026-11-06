import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

beta = 0.1 # The transmission/infection rate per time unit
gamma = 20 # The rate of people being removed from the infected population

# Return the derivatives dS/dt, dI/dt, dR/dt respectively 
def sir_model(y, t):
    S, I, R = y
    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

# Return the derivatives dS/dt, dI/dt, dR/dt, dS_H/dt, dI_H/dt, and dR_H/dt respectively
def sir_twopopulations(y, t):
    beta2 = 0.05
    beta3 = 0.5

    S, I, R, SH, IH, RH = y
    dS = -S * (beta * I + beta2 * IH)
    dI = S * (beta * I + beta2 * IH) - gamma * I
    dR = gamma * I
    dSH = -SH * (beta2 * I + beta3 * IH)
    dIH = SH * (beta2 * I  + beta3 * IH) - gamma * IH
    dRH = gamma * IH
    return [dS, dI, dR, dSH, dIH, dRH]


y_0 = [90, 10, 0, 100, 0, 0] # Initial values for S, I, R, S_H, I_H, R_H respectively

time = np.linspace(0, 1.2, 100) # Create 100 equally spaced points between 0 and 1.2

soln = odeint(sir_twopopulations, y_0, time) # Numerically solve the system of differential eqs

S_out = soln[:, 0] # The solution for the susceptible population
I_out = soln[:, 1] # The solution for the infected population
R_out = soln[:, 2] # The solution for the removed population
SH_out = soln[:, 3] # The solution for the second susectible population 
IH_out = soln[:, 4] # The solution for the second infected population
RH_out = soln[:, 5] # The solution for the second removed population

plt.plot(time, S_out, label="S(t)")
plt.plot(time, I_out, label="I(t)")
plt.plot(time, R_out, label="R(t)") 
plt.plot(time, SH_out, label="S_H(t)")
plt.plot(time, IH_out, label="I_H(t)")
plt.plot(time, RH_out, label="R_H(t)")# Plot all the solutions over the same time values
plt.xlabel("Time") # Label the x-axis as time
plt.ylabel("Population") # Label the y-axis as population
plt.title("SIR model over time two populations") # Title the plot
plt.legend(loc="upper right") # Show the plot legend
plt.show() # Show the plot

print(f"Last R(t) value: {R_out[-1]} | Last R_H(t) value: {RH_out[-1]}")

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint # Import the necesary libraries and functions

alpha = 1.5 # Natural growth rate of the rabbit population in abscence of predator population
gamma = 0.4  # Natural death rate of the fox population, how quickly foxes die without enough food
beta = 0.5  # Predation rate, how quickly foxes reduce the rabbit population when they interact
delta = 0.8 # The grow rate for the fox population, how much the population increases from eating rabbits

def deriv (pops,t):
	rabbits, foxes = pops
	dR = alpha * rabbits - beta * rabbits * foxes
	dF = -gamma * foxes + delta * rabbits * foxes
	return [dR, dF]
# Returns the resulting rates of change in the populations, dR/dt, dF/dt respectively

# Create an array of 1000 points equally spaced between 0-30 to represent time
time = np.linspace(0, 30, 1000)

initial_conds = [(0, 5), (10, 5), (10, 0)] # Create array of initial condition cases corresponding to (a), (b), and (c)

for conds in initial_conds:
	soln = odeint(deriv, conds, time) # Solve the system of diff. eqs. given the initial populations
	# Print the smallest and largest that both populations reach
	print("Rabbit pop. lowest:", min(soln[:, 0]), "| Fox pop. lowest:", min(soln[:, 1])) 
	print("Rabbit pop. largest:", max(soln[:, 0]), "| Fox pop. largest:", max(soln[:, 1]))
	plt.figure() # Create a new figure
	plt.plot(time, soln[:, 0], label="Rabbits")
	plt.plot(time, soln[:, 1], label="Foxes")
	plt.xlabel("Time") # Label the x-axis as time in weeks
	plt.ylabel("Population") # Label the y-axis as population
	plt.title(f"{conds[1]} foxes vs. {conds[0]} rabbits")
	plt.legend()
	plt.show() # Show the figure


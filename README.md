# Particle tango (Monte-Carlo simulation)

## Description

Solving the task about two particles on a square lattice. The certain potential is applied and the Metropolis-Hastings algorithm is used to  average properties over the trajectory.
Detailed description of the task, solution and thermodynamical description can be found in this [article](https://blog.sklad.observer/posts/particle-tango/).

The libraries used are: numpy, matplotlib, random.

## How to use this code

There are two main files: .py file and .ipnyb Jupyter Notebook. I recommend using the latter since it is easier to run simulation and analysis of the trajectory separately.
To start a new simulation you can create a cell and write:
```
new_run = Particles()
new_run.update()
```
This will start the simulation and write down the parameters as it goes (particle coordinates and corresponding energy).

### Potentials

Currently you can choose three potentials to play with: 
1. Classic (called so because it was in the original task back in the day): the interaction energy is -5.0 if the distance is equal to 1 (particles on the edge of a square unit), -3.5 if particles are located on the diagonal, and 0.0 otherwise.
2. Lennard-Jones. The depth of the well $\varepsilon=-5.0$, the $\sigma$ parameter is set so as to have $r_{min}=2^{1/6}\sigma=1$.
3. Coulomb potential (repulsivness or attractivness is curently hard-coded into the Energy function and you can change it if you want).
   
It should be noted that energies and temperatures are all measured in arbitrary dimentionless units. You can multiply it by physical factors and obtain real-world-like parameters.

I plan on adding some other potentials such as Morse potential later on.

### Inputs

At the start of every simulation you are prompted with the choice of the potential. Pick any of the above. You also have to choose the temperature of the system, feel free to play with this parameter 
and look your system behave diffrently. Potential inputs are number-coded, temperature should be a non-negative float (this is a thermodynamic temperature so it cannot go below zero).

### Averages

The function called *Average_value()* can calculate an average of any property over the simulation frames. Be sure to save the property values during the simulation or calculate them later on with the coordinate data. Ther is also a separate function for calculating distances from Cartesian coordinates 
and a function for the calculation of entropy (you can see some examples in the code). All the mathematical details can be found in the article (link above).

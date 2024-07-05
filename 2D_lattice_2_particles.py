import matplotlib.pyplot as plt
from math import exp as exp
from math import log as log
from math import sqrt as sqrt
import numpy as np

#calculate the energy of 2 particles on a lattice. Classic: It can be -5 if the distance is 1,
#  -3.5 if the distance is sqrt(2)
# and 0 if the distance is > sqrt(2)
def Energy(coord_1, coord_2, potential):
    if potential == '1':
        if sqrt((coord_1[0]-coord_2[0])**2+(coord_1[1]-coord_2[1])**2) == 1.0:
            E = -5
        elif sqrt((coord_1[0]-coord_2[0])**2+(coord_1[1]-coord_2[1])**2) == sqrt(2):
            E = -3.5
        else:
            E = 0
    #Lennard-Jones potential
    elif potential == '2':
        sigma = 0.890899
        epsilon = 5
        dist = sqrt((coord_1[0]-coord_2[0])**2+(coord_1[1]-coord_2[1])**2)
        E = 4*epsilon*(np.power((sigma/dist),12) - np.power((sigma/dist),6))
    #Coulomb potential for single-charged particles    
    elif potential == '3':
        dist_square = (coord_1[0]-coord_2[0])**2+(coord_1[1]-coord_2[1])**2
        E = -1/dist_square
    return E

#calculate distance for cordinate trek d = sqrt((x1-x2)^2+(y1-y2)^2)
def distance_calculator(arr_1, arr_2):
    distance_arr = []
    if len(arr_1)!=len(arr_2):
        print('Error, different path lengths')
    else:
        for i in range(len(arr_1)):
            distance_arr.append(sqrt((arr_1[i][0]-arr_2[i][0])**2+(arr_1[i][1]-arr_2[i][1])**2))
    return distance_arr


#Create particle class with the update option
class Particles():
    def __init__(self):
        #generate starting coordinates
        self.start_pos_1 = np.random.randint(low = 0, high = 10, size = 2)
        self.start_pos_2 = np.random.randint(low = 0, high = 10, size = 2)
        #cheking self-interference and hoping it won't generate the same 2 coords twice in a row
        while (self.start_pos_2 == self.start_pos_1).all():
            self.start_pos_2 = np.random.randint(low = 0, high = 10, size = 2)
        # selecting the potential to be applied to the system
        self.potential = input('Select the potential: 1 - standard, 2 - LJ, 3 - Coulomb')

        self.start_E = Energy(self.start_pos_1, self.start_pos_2, self.potential)
        #saving the treks to follow them later on
        self.coordinate_trek_1 = []
        self.coordinate_trek_2 = []
        self.Energy_trek = []
        self.Temp = float(input('Enter the temperature'))


    def update(self):
        old_pos_1 = self.start_pos_1
        old_pos_2 = self.start_pos_2
        counter = 0
        old_E = self.start_E
        # a somewhat working Metropolis-Hastings algorithm
        # randomly pick a particle 
        # randomly assign it to a new lattice vertex
        # generate a random number for comparison, then compare with the energy factor k = exp((E1-E2)/T)
        # compare the former and the latter, if u <= k then accept the new state, otherwise remain in the old state
        while (counter < 10000):
            particle_choice = rnd.randint(1,2)
            if particle_choice == 1:
                new_pos_1 = np.random.randint(low = 0, high = 10, size = 2)
                while (new_pos_1 == old_pos_2).all():
                    new_pos_1 = np.random.randint(low = 0, high = 10, size = 2)
                new_E = Energy(new_pos_1, old_pos_2, self.potential)
                k = exp((old_E - new_E)/self.Temp)
                u = rnd.uniform(0,1)
                if u <= k:
                    old_E = new_E
                    old_pos_1 = new_pos_1
                    print(old_pos_1, old_pos_2)
                    self.Energy_trek.append(old_E)
                    self.coordinate_trek_1.append(old_pos_1)
                    self.coordinate_trek_2.append(old_pos_2)
                else:
                    print(old_pos_1, old_pos_2)
                    self.Energy_trek.append(old_E)
                    self.coordinate_trek_1.append(old_pos_1)
                    self.coordinate_trek_2.append(old_pos_2)

            elif particle_choice == 2:
                new_pos_2 = np.random.randint(low = 0, high = 10, size = 2)
                while (new_pos_2 == old_pos_1).all():
                    new_pos_2 = np.random.randint(low = 0, high = 10, size = 2)
                new_E = Energy(new_pos_2, old_pos_1, self.potential)
                k = exp((old_E-new_E)/self.Temp)
                u = rnd.uniform(0,1)
                if u <= k:
                    old_E = new_E
                    old_pos_2 = new_pos_2
                    print(old_pos_1, old_pos_2)
                    self.Energy_trek.append(old_E)
                    self.coordinate_trek_1.append(old_pos_1)
                    self.coordinate_trek_2.append(old_pos_2)
                else:
                    print(old_pos_1, old_pos_2)
                    self.Energy_trek.append(old_E)
                    self.coordinate_trek_1.append(old_pos_1)
                    self.coordinate_trek_2.append(old_pos_2)
            counter +=1

test = Particles()
print(test.start_pos_1, test.start_pos_2)
test.update()
# calculate an average value for the physical parameter A
def Average_value(A_arr, E_arr, T):
    E_arr = E_arr[50:]
    A_arr = A_arr[50:]
    weights = [exp(E/T) for E in E_arr]
    weights_sum = sum(weights)
    A_avg = 0
    for i in range(len(A_arr)):
        A_avg += A_arr[i]*weights[i]
    A_avg = A_avg/weights_sum
    return A_avg
#calculate the entropy of the system   
def Entropy(E_arr, T):
    E_arr = E_arr[50:]
    weights = [exp(E/T) for E in E_arr]
    S = 0
    for i in weights:
        S+= -i*log(i)
    return S
distance = distance_calculator(test.coordinate_trek_1, test.coordinate_trek_2)
print('Average energy = ', Average_value(test.Energy_trek, test.Energy_trek, test.Temp))
print('Average distance = ', Average_value(distance, test.Energy_trek, test.Temp))
print('Ensemble entropy = ', Entropy(test.Energy_trek, test.Temp))

#plot distance and energy graph along the trek 
fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].plot(distance, label='distance, T = '+str(test.Temp))
axs[0].axhline(y = 1, color = 'r', linestyle = '-') 
axs[0].set_ylim([0, max(distance)+0.5])
axs[0].legend()
axs[1].plot(test.Energy_trek, label='Energy, T = '+str(test.Temp), color = 'orange')
axs[1].legend()

plt.show()

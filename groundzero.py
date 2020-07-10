"""
author: MARCOS FONTES VAZ
@twitter: sea_fontes
@github: seafontes
date: 06 JULY 2020

"""

"""----------------1. IMPORTS------------------------------
 this are the libraries used by the code
"""
import math
import random
import numpy as np
import os.path
import seaborn as sns
import matplotlib.pyplot as plt
import time
from PIL import Image
import glob

start_time = time.time()
sns.set()

""" --------------2. MATRIX ELEMENTS DEFINITION -------
 this values are used to represent the states below. changing may result in malfunctioning.
 mind the +1 steps between consecutive SEIR states.
"""

SUSCEPTIBLE = 0
EXPOSED = 1
INFECTED = 2
RECOVERED = 3
DEAD = -2
AUXILIARY = 77777

""" --------------3. GENERAL VARIABLES-----------------
 this values are the parameters in which the simulation is based on.
 changing this values will not result in malfunctioning, but in different disease behavior
"""
order = 100  # matrix order
beta = 0.1  # infectiousness
days = 100  # days of iteration
t_zero = 0.02  # tax of infestation in day one
days_incubated = 2  # days of incubation
i_incubation = 1.0 / (days_incubated + 1)  # daily increment on exposed people
days_infected = 7  # days until recovery
i_infected = 1.0 / (days_infected + 1)  # daily increment on infected people
death_prob = 0.005  # death probability

""" -------------4. FUNCTION DEFINITION---------------
 in this section, all the functions on which the model is based are defined.
 highly recommended not to change anything except the path used on save_* functions and write_data
 especially if you're on an unix based OS
"""


def count_elements(city, element):  # returns the number of a determined type of element,ex.: count_elements(city, DEAD)
    return np.count_nonzero(city.astype(int) == element)


def infected_neighbors(i, j, city):  # returns the number of infected neighbors for an specified cell
    count = 0
    if math.floor(city[i - 1][j]) == INFECTED: count += 1
    if math.floor(city[i][j - 1]) == INFECTED: count += 1
    if math.floor(city[i - 1][j - 1]) == INFECTED: count += 1

    if i == order - 1:
        if math.floor(city[0][j]) == INFECTED: count += 1
        if math.floor(city[0][j - 1]) == INFECTED: count += 1
        if j == order - 1:
            if math.floor(city[0][0]) == INFECTED: count += 1
            if math.floor(city[i][0]) == INFECTED: count += 1
            if math.floor(city[i - 1][0]) == INFECTED: count += 1
            return count
        if math.floor(city[i - 1][j + 1]) == INFECTED: count += 1
        if math.floor(city[i][j + 1]) == INFECTED: count += 1
        if math.floor(city[0][j + 1]) == INFECTED: count += 1
        return count
    elif j == order - 1:
        if math.floor(city[i - 1][0]) == INFECTED: count += 1
        if math.floor(city[i][0]) == INFECTED: count += 1
        if math.floor(city[i + 1][0]) == INFECTED: count += 1
        if math.floor(city[i + 1][j]) == INFECTED:  count += 1
        if math.floor(city[i + 1][j - 1]) == INFECTED: count += 1
        return count
    if math.floor(city[i - 1][j + 1]) == INFECTED: count += 1
    if math.floor(city[i][j + 1]) == INFECTED: count += 1
    if math.floor(city[i + 1][j + 1]) == INFECTED: count += 1
    if math.floor(city[i + 1][j]) == INFECTED: count += 1
    if math.floor(city[i + 1][j - 1]) == INFECTED: count += 1
    return count


def initialize_city():  # returns a numpy matrix of an order specified on section 2
    city = np.random.rand(order, order)
    for i in range(order):
        for j in range(order):
            if city[i][j] <= t_zero:
                city[i][j] = 2
            else:
                city[i][j] = 0
    city.astype(float)
    return city


def infection_test(i, j, city):  # boolean test if an cell got infected during an iteration
    cap = 1 - math.pow(1 - beta, infected_neighbors(i, j, city))
    luck = random.random()
    if luck <= cap:
        return True
    else:
        return False


def write_data(t, city) -> object:  # writes the data of each iteration on an .txt file for further analysis
    if not os.path.exists("data.txt"):
        file = open("data.txt", "w")
        file.write("TIME" + "\t" +
                   "SUS" + "\t" +
                   "EXP" + "\t" +
                   "INF" + "\t" +
                   "REC" + "\t" +
                   "DEAD" + "\n")
        file.close()
    file = open("data.txt", "a")
    file.write(str(t) + "\t" +
               count_elements(city, SUSCEPTIBLE) + '\t' +
               count_elements(city, EXPOSED) + '\t' +
               count_elements(city, INFECTED) + '\t' +
               count_elements(city, RECOVERED) + '\t' +
               count_elements(city, DEAD) + '\n')
    file.close()
    return


def death_test():  # boolean test if an infected cell died this iteration
    if random.random() <= death_prob: return True
    return False


def save_heatmap(t, city):  # plots and saves the color schemed heatmap, easier to visualize
    hm = sns.heatmap(city, center=0, vmin=-2, vmax=3, cmap='Dark2', yticklabels=False, xticklabels=False)
    plt.savefig("heatmaps\\{}.png".format(t))
    plt.clf()


def save_graph():  # plots and saves a graph presenting curves of the number of people x iteration for each state
    plt.style.use('seaborn')
    t, sus, exp, inf, rec, dead = np.loadtxt('data.txt', delimiter='\t', unpack=True, skiprows=1)
    plt.plot(t, sus, label='Suscetíveis', color='g')
    plt.plot(t, exp, label='Expostos', color='y')
    plt.plot(t, inf, label='Infectados', color='m')
    plt.plot(t, rec, label='Recuperados', color='b')
    plt.plot(t, dead, label='Fatalidades', color='k')
    plt.title('Evolução Temporal')
    plt.xlabel('Tempo')
    plt.ylabel('Quantidade de Habitantes')
    plt.legend()
    figure = plt.gcf()
    figure.set_size_inches(16, 8)
    plt.savefig("graphs\\evolucao.png", dpi=96)
    return


def save_gif():  # append every heatmap into a gif, pretty simple
    frames = []
    imgs = sorted(glob.glob("heatmaps\\*.png"), key=os.path.getmtime)
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    frames[0].save('evolucao.gif', format='GIF',
                   append_images=frames[1:], save_all=True, duration=200, loop=0)


""" ------------5. INITIALIZING CITY----------------
 here, the first iteration is manual.
 the city is initialized on day one and it's data is written and saved.
"""
city = initialize_city()
tempo = 0
write_data(tempo, city)
save_heatmap(tempo, city)
tempo += 1

"""" -------------6. ITERATIONS-----------------------
 in this while block the simulation will go on using the functions defined above.
"""
while tempo < days:
    for i in range(order):  # iterations for infection
        for j in range(order):
            if city[i][j] == 0 and infection_test(i, j, city): city[i][j] = AUXILIARY

    for i in range(order):  # iteration for states updates
        for j in range(order):
            if math.floor(city[i][j]) == EXPOSED:
                city[i][j] += i_incubation
                if city[i][j] >= EXPOSED + 1: city[i][j] = INFECTED

            if math.floor(city[i][j]) == INFECTED:
                if not death_test():
                    city[i][j] += i_infected
                    if city[i][j] >= INFECTED + 1: city[i][j] = RECOVERED
                else:
                    city[i][j] = DEAD

            if city[i][j] == AUXILIARY: city[i][j] = EXPOSED
    write_data(tempo, city)
    save_heatmap(tempo, city)
    tempo += 1

save_graph()
save_gif()
print("-----{} secs-----".format(time.time() - start_time))

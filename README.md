# Groundzero
A basic SEIR(D) epidemic modeling scheme using Python
## Introduction


   The main goal of this project is, to some degree, simulate how would a made-up disease spread in a city, if this city was a 100x100 "square circular" matrix and the residents could only interact with their 8 neighbors. The condition is based on the SEIR model which divides the population into four different stages. First, the fellows are considered *Susceptible*, i.e., not yet exposed to the agent and able to get sick. Once they're exposed, they become *Exposed* (who saw that coming?) and the disease starts it's incubation period, but it can't be spread yet. After this period, the resident becomes *Infected*, the sickness starts showing it's symptoms and now they have a chance to infect neighbors. In addition to the well-known model, there's *Death*. While the residents are Infected, they have a determined chance of dying. If they survive a preset number of days, they get better and considered *Recovered*.
  
  
## The Code
   I find it easier to explain the general idea of the code and the differences betweeen the versions going through it's steps. So, if you find yourself comfortable enough to just read the *.py* files and understand it without a detailed explanation, feel free to jump into it. It's valid to point out that the verions are in fact so similiar that it's not worthy writing another README, and I'll be able to discuss the difference in further topics. 
### The Imports
   This section will be used to justify each one of the imports, even the ones that may seem obvious.
  
  
   * **math**: simplificate some expressions;
   * **random**: generate random numbers to comparare to determinated probability;
   * **numpy**: easily create and manipulate the matrix;
   * **os.path**: file tests;
   * **seaborn**: generate heatmaps;
   * **mathplotlib.pyplot**: plot and save the graphs and heatmap;
   * **PIL** and **glob**: generate a GIF from the heatmaps;
   * **time**: measure the execution time;
   
   
### SEIR Elements Definitions
   Each element of the SEIR(D) model will be represented by the integer part of a real number, and the decimal part can be interpreted as how far is the resident at determined stage.
   * *SUSCEPTIBLE = 0*
   * *EXPOSED = 1*
   * *INFECTED = 2*
   * *RECOVERED = 3*
   * *DEAD = -2*
   * *AUXILIARY = 77777*
   
   
   The choice of *-2* for Death is due only to the color scale, which will be explained in some sections after. The AUXILIARy value is totally arbitrary.

### General Parameters
   This parameters will define the disease beahavior.
   * *order*: the matrix order;
   * *beta*: the infectiousness;
   * *days*: how many days there'll be in the simulation;
   * *t_zero*: tax of infestation in day one;
   * *days_incubated*: how many days the agent takes to become active;
   * *i_incubated*: value of the daily increment of the stage *Exposed*;
   * *days_infected*: how many days the agent takes to become inative again or be exterminated by the organism;
   * *i_infected*: value of the dayly increment of the stage *Infected*;
   * *death_prob*: the death probability in each day/iteration;
### Funcition Definition

# Groundzero
A basic SEIR(D) epidemic modeling scheme using Python
## Introduction


   The main goal of this project is, to some degree, simulate how would a made-up disease spread in a city, if this city was a 100x100 "square circular" matrix and the residents could only interact with their 8 neighbors. The condition is based on the SEIR model which divides the population into four different stages. First, the fellows are considered *Susceptible*, i.e., not yet exposed to the agent and able to get sick. Once they're exposed, they become *Exposed* (who saw that coming?) and the disease starts it's incubation period, but it can't be spread yet. After this period, the resident becomes *Infected*, the sickness starts showing it's symptoms and now they have a chance to infect neighbors. In addition to the well-known model, there's *Death*. While the residents are Infected, they have a determined chance of dying. If they survive a preset number of days, they get better and considered *Recovered*.
  
  
## The Code
   I find it easier to explain the general idea of the code going through its steps. So, if you find yourself comfortable enough to just read the *.py* and understand it without a detailed explanation, feel free to jump into it.
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

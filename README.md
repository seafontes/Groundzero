# Groundzero
A basic SEIR(D) epidemic modeling scheme using Python
## Introduction


  The main goal of this project is, to some degree, simulate how would a made-up disease spread in a city, if this city was a 100x100 "square circular" matrix and the residents could only interact with their 8 neighbors. The condition is based on the SEIR model which divides the population into four different stages. First, the fellows are considered Susceptible, i.e., not yet exposed to the agent and able to get sick. Once they're exposed, they become Exposed (who saw that coming?) and the disease starts it's incubation period, but it can't be spread yet. After this period, the resident becomes Infected, the sickness starts showing it's symptoms and now they have a chance to infect neighbors. In addition to the well-known model, there's Death. While the residents are Infected, they have a determined chance of dying. If they survive a preset number of days, they get better and considered Recovered.
  
  
## The Idea


  

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:52:51 2019

@author: Administrator
"""

import tkinter
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import csv
import matplotlib
import agentframework
matplotlib.use('TkAgg')

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

environment = []
with open('in.txt', newline='') as csvfile: # open the data file
    reader = csv.reader(csvfile, delimiter=',') # read the data and seperate the data with comma
    for row in reader: # A list of rows
       
        rowlist = []# A list of rows
        for value in row: # A list of value
            rowlist.append(int(value))
        environment.append(rowlist)
            
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,20))

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents):        
        agents[i].move()
        agents[i].eat()       
        agents[i].share_with_neighbours()

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i][0],agents[i][1])
    matplotlib.pyplot.imshow(environment)
		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()

root = tkinter.Tk() # Main window.
root.wm_title("Model") # named the title of the windouws
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()
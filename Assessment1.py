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


###### Set the variables ########
num_of_agents = 10  
num_of_iterations = 100 
agents = [] # A list named 'agents'

fig = matplotlib.pyplot.figure(figsize=(7, 7)) # set the size of the windows
ax = fig.add_axes([0, 0, 1, 1])


######### Read the data #########
environment = [] # A list name 'environment'
with open('in.txt', newline='') as csvfile: # open the data file named in.txt
    reader = csv.reader(csvfile, delimiter=',') # read the data and seperate the data with comma
    for row in reader: # A list of rows
        rowlist = []
        for value in row: 
            rowlist.append(int(value)) # add the data value into rowlist
        environment.append(rowlist) # add the 'rowlist' into 'environmrnt'

            
######### Make the agents #######
for i in range(num_of_agents): # add 10 elements into the list
    agents.append(agentframework.Agent(environment,agents,20)) 

carry_on = True	


##### Defined the functions #####	
def update(frame_number): # update the images for each 'sheeps' move
    
    fig.clear()   # clear the value in fig
    global carry_on # call the global variable
    
    for i in range(num_of_agents):  # call the functions that we create in the agnetframework aim to update the value of each agents      
        agents[i].move() 
        agents[i].eat()       
        agents[i].share_with_neighbourhoods()

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents): # assign the value to the scatter plots
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i][0],agents[i][1])
    matplotlib.pyplot.imshow(environment)
		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# define the function aims to run the animation
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()
    

######## Create the Windows #########  
root = tkinter.Tk() # Main window.
root.wm_title("Model") 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


######## Create 'Run' botton #########
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()
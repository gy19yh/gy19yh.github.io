# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:40:22 2019

@author: gy19yh
"""

import random

class Agent():
    def __init__ (self,environment,agents,neighbourhood):
        self.y = random.randint(0,299)
        self.x = random.randint(0,299)
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300        
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
                       
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def calcutalte_distance(self, environment):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= environment:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave

    def distance_between(self, agent):
        return (((self.x - agent.x)**2)+((self.y - agent.y)**2))**0.05

    def share_with_neighbours(self):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= self.neighbourhood:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave
                print("sharing" + str(dist) + "" + str(ave))
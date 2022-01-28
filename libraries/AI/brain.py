import random
import time
import os

class AI:
    def __init__(self, name, goal):
        # punishment variables telling the AI what and what not to do
        self.punishment = []
        self.best = []
        self.name = name
        self.goal = goal

    # sends a punishment to the AI adding to the list of punishments
    def sendCorrection(self, correction):
        self.punishment += correction

    # This is the actual AI 
    def action(self, generations):
        self.results = {}
        # runs all generations
        for a in range(1, generations + 1):
            current = 0
            value = random.randrange(current, self.goal)
            if value > current:
                if value in self.punishment:
                      pass
                else:
                    current = value
            self.results[f"gen{str(a)}"] = current
        return self.results

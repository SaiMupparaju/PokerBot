from typing import List, Dict
import random
import numpy as np
import sys

Actions = ["B", "C"]

class InformationSet():
    def __init__(self):
        self.cumulative_regrets = np.zeros(shape=len(Actions))
        self.strategy_sum = np.zeros(shape=len(Actions))
        self.num_actions = len(Actions)

    def normalize(self, strategy: np.array) -> np.array:
        """Normalize a strategy. If there are no positive regrets,
        use a uniform random strategy"""
        if sum(strategy) > 0:
            strategy /= sum(strategy)
        else:
            strategy = np.array([1.0 / self.num_actions] * self.num_actions)
        return strategy

    def get_strategy(self, reach_probability: float) -> np.array:
        """Return regret-matching strategy"""
        strategy = np.maximum(0, self.cumulative_regrets)
        strategy = self.normalize(strategy)

        self.strategy_sum += reach_probability * strategy
        return strategy

    def get_average_strategy(self) -> np.array:
        return self.normalize(self.strategy_sum.copy())

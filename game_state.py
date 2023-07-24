from abc import ABC, abstractmethod
from typing import List, Dict
import random
import numpy as np
import sys

class GameState(ABC):
    @abstractmethod
    def is_terminal(self) -> bool:
        pass

    @abstractmethod
    def get_payoffs(self) -> List[int]:
        pass

    @abstractmethod
    def get_actions(self) -> List[str]:
        pass


from dataclasses import dataclass
from typing import List


@dataclass
class PromRow:
    X_name: str
    X_Apr: str
    X_1: List[int]
    X_2: str
    X_2_lst: List[int]
    Key: bool = True

from dataclasses import dataclass
from typing import Optional


@dataclass
class CreationRule:
    regex: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    precision: Optional[int] = None
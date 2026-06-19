from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class Task:
    goal: str
    action: str = ""
    status: str = "pending"
    result: Any = None
    id: str = field(default_factory=lambda: str(uuid4()))

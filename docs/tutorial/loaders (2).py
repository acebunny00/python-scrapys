from dataclasses import dataclass, field
from typing import Optional

@dataclass
class InventoryItem:
	name: Optional[str] = field(default=None)
	price: Optional[float] = field(default=None)
	stock: Optional[int] = field(default=None)

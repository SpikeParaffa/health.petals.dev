from typing import Optional
from urllib.parse import urlparse
import petals
from pydantic import BaseModel, Field
from pydantic.v1 import dataclasses as pydantic_v1_dataclasses

@pydantic_v1_dataclasses.dataclass
class ModelInfo(petals.data_structures.ModelInfo):
    dht_prefix: Optional[str] = None
    official: bool = True
    limited: bool = False

    @property
    def name(self) -> str:
        return urlparse(self.repository).path.lstrip("/")

    @property
    def short_name(self) -> str:
        return self.name.split("/")[-1]

class ModelInfoV2(BaseModel):
    model: ModelInfo

    class Config:
        arbitrary_types_allowed = True

    @property
    def dht_prefix(self) -> Optional[str]:
        return self.model.dht_prefix

    @property
    def official(self) -> bool:
        return self.model.official

    @property
    def limited(self) -> bool:
        return self.model.limited

    @property
    def name(self) -> str:
        return self.model.name

    @property
    def short_name(self) -> str:
        return self.model.short_name

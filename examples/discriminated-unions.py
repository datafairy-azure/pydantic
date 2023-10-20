from typing import Union, Literal, List

from pydantic import BaseModel, Field


class ModelA(BaseModel):
    d_type: Literal["single"]
    value: int = Field(default=0)


class ModelB(ModelA):
    """Inherits from ModelA, making the union challenging"""

    d_type: Literal["many"]
    values: List[int] = Field(default_factory=list)


class ModelC(BaseModel):
    v: Union[ModelA, ModelB] = Field(discriminator="d_type")


# Populate with extra fields, see what happens
m_1 = ModelC(v={"value": 123, "values": [123], "d_type": "single"})
m_2 = ModelC(v={"value": 123, "values": [123], "d_type": "many"})

print(m_1, m_2, sep="\n")
# v=ModelA(d_type='single', value=123)
# v=ModelB(d_type='many', value=123, values=[123])

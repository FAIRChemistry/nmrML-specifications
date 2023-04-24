import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Temperature(sdRDM.DataModel):

    """A temperature and references to a unit from the unit ontology."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("temperatureINDEX"),
        xml="@id",
    )

    temperature: float = Field(
        ...,
        description="none given",
        xml="@temperature",
    )

    temperature_uni_name: str = Field(
        ...,
        description="none given",
        xml="@temperatureUnitName",
    )

    temperature_unit_id: Optional[str] = Field(
        default=None,
        description="none given",
        xml="@temperatureUnitID",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

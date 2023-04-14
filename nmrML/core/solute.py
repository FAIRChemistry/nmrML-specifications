import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .valuewithunit import ValueWithUnit


@forge_signature
class Solute(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("soluteINDEX"),
        xml="@id",
    )

    concentration_in_sample: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="concentrationInSample",
    )

    name: str = Field(
        ...,
        description="none given",
        xml="@name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

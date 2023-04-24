import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .valuewithunit import ValueWithUnit
from .cvterm import CVTerm


@forge_signature
class ConcentrationStandard(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("concentrationstandardINDEX"),
        xml="@id",
    )

    type: CVTerm = Field(
        ...,
        description="none given",
        xml="type",
    )

    concentration_in_sample: ValueWithUnit = Field(
        ...,
        description=(
            "This element holds a value that also has a unit. Only controlled values"
            " are allowed for the unit."
        ),
        xml="concentrationInSample",
    )

    name: CVTerm = Field(
        ...,
        description="none given",
        xml="name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from typing import Any

from .elementtype import ElementType


@forge_signature
class Atom(sdRDM.DataModel):

    """Must have an id attribute unique to the file only, so that it can be referenced by the bond elements as well as by the spectrum annotations. Most people use 'a1', 'a2', ... , 'aN'."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("atomINDEX"),
        xml="@id",
    )

    element_type: ElementType = Field(
        ...,
        description="The symbol for the element. For example: 'H','C' or 'Fe'.",
        xml="@elementType",
    )

    x: Any = Field(
        ...,
        description=(
            "The x position of the element in cartesian coordinates. The cordinates"
            " along with the bond information in the bond list should allow for"
            " software to draw a 2D representation of the chemical structure."
        ),
        xml="@x",
    )

    y: Any = Field(
        ...,
        description=(
            "The y position of the element in cartesian coordinates. The cordinates"
            " along with the bond information in the bond list should allow for"
            " software to draw a 2D representation of the chemical structure."
        ),
        xml="@y",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

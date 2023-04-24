
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .parametergroup import ParameterGroup


@forge_signature
class PulseSequence(ParameterGroup):

    """A list of references to the source files that define the pulse sequence including pulse shape files, pulse sequence source code, pulse sequence parameter files, etc."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("pulsesequenceINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Peak(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("peakINDEX"),
        xml="@id",
    )

    _: float = Field(
        ...,
        description="none given",
        xml="@center",
    )

    amplitude: Optional[float] = Field(
        default=None,
        description="none given",
        xml="@amplitude",
    )

    width: Optional[float] = Field(
        default=None,
        description="none given",
        xml="@width",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

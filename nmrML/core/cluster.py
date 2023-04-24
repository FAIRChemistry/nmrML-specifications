import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .peaklist import PeakList


@forge_signature
class Cluster(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("clusterINDEX"),
        xml="@id",
    )

    peak_list: PeakList = Field(
        ...,
        description=(
            "A list of the positions and amplitudes of the peaks in the multiplet."
            " Optional if the peaks are not identified. In which case the 'center'"
            " attribute offers a hint for annotation."
        ),
        xml="peakList",
    )

    center: Optional[float] = Field(
        default=None,
        description="none given",
        xml="@center",
    )

    shift: Optional[float] = Field(
        default=None,
        description="none given",
        xml="@shift",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

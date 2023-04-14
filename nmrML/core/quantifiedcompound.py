
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .chemicalcompound import ChemicalCompound
from .valuewithunit import ValueWithUnit
from .peaklist import PeakList
from .clusterlist import ClusterList


@forge_signature
class QuantifiedCompound(ChemicalCompound):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("quantifiedcompoundINDEX"),
        xml="@id",
    )

    concentration: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="concentration",
    )

    cluster_list: Optional[ClusterList] = Field(
        default=None,
        description=(
            "A list of clusters of peaks that are aligned with the spectrum for"
            " quantification."
        ),
        xml="clusterList",
    )

    peak_list: Optional[PeakList] = Field(
        default=None,
        description=(
            "A list of the positions and amplitudes of the peaks that are associated"
            " with the compound. This is an alternative to the cluster list for the"
            " case where you want to record a fit but discard some of the information"
            " about the library you used to fit the spectrum."
        ),
        xml="peakList",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

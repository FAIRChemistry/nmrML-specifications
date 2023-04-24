
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .clusterlist import ClusterList
from .valuewithunit import ValueWithUnit
from .peaklist import PeakList
from .chemicalcompound import ChemicalCompound


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
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

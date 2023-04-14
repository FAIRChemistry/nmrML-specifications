import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisition1d import Acquisition1D
from .acquisitionmultid import AcquisitionMultiD


@forge_signature
class Acquisition(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionINDEX"),
        xml="@id",
    )

    acquisition_1d: Optional[Acquisition1D] = Field(
        default=None,
        description="",
        xml="acquisition1D",
    )

    acquisition_multi_d: Optional[AcquisitionMultiD] = Field(
        default=None,
        description="",
        xml="acquisitionMultiD",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

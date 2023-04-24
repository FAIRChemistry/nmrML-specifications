import sdRDM

from typing import Optional, Union
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitionmultid import AcquisitionMultiD
from .acquisition1d import Acquisition1D


@forge_signature
class Acquisition(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionINDEX"),
        xml="@id",
    )

    acquisition: Union[Acquisition1D, AcquisitionMultiD] = Field(
        ...,
        description="none given",
        xml="{Acquisition1D: acquisition1D, AcquisitionMultiD: acquisitionMultiD}",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

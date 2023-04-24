import sdRDM

from typing import Optional, Union
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

    acquisition: Union[Acquisition1D, AcquisitionMultiD] = Field(
        ...,
        description="none given",
        xml="{Acquisition1D: acquisition1D, AcquisitionMultiD: acquisitionMultiD}",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

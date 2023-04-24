
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .binarydataarray import BinaryDataArray


@forge_signature
class FIDData(BinaryDataArray):

    """sdRDM-conform implementation of the [BinaryDataArray](#BinaryDataArray) in fidData."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("fiddataINDEX"),
        xml="@id",
    )

    binary_data_array: str = Field(
        ...,
        description="Binary data given as base64-encoded string.",
        xml="fidData",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

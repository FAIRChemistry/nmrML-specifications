
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .binarydataarray import BinaryDataArray


@forge_signature
class SamplingTimePoints(BinaryDataArray):

    """sdRDM-conform implementation of the [BinaryDataArray](#BinaryDataArray) in samplingTimePoints."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("samplingtimepointsINDEX"),
        xml="@id",
    )

    binary_data_array: str = Field(
        ...,
        description="Binary data given as base64-encoded string.",
        xml="samplingTimePoints",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

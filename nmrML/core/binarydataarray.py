import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveInt


@forge_signature
class BinaryDataArray(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("binarydataarrayINDEX"),
        xml="@id",
    )

    compressed: bool = Field(
        ...,
        description=(
            "True if the binary data was compressed with zlib before encoding as"
            " base64."
        ),
        xml="@compressed",
    )

    encoded_length: PositiveInt = Field(
        ...,
        description=(
            "The number of characters in the base64 string. This is useful for skipping"
            " over the string in high throughput applications."
        ),
        xml="encodedLength",
    )

    byte_format: str = Field(
        ...,
        description=(
            "TODO format as little endian 64 bit pairs of floats, or 32 bit pairs of"
            " floats. See online documentation for decoding examples."
        ),
        xml="byteFormat",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

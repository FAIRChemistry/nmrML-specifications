import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl


@forge_signature
class CompoundDatabaseIdentifier(sdRDM.DataModel):

    """Captures a database identifier and reference via URI."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("compounddatabaseidentifierINDEX"),
        xml="@id",
    )

    identifier: str = Field(
        ...,
        description="none given",
        xml="@identifier",
    )

    uri: AnyUrl = Field(
        ...,
        description="none given",
        xml="@URI",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

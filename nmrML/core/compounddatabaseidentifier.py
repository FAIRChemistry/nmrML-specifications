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
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

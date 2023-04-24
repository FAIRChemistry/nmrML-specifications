
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cvterm import CVTerm


@forge_signature
class Software(CVTerm):

    """Software information."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwareINDEX"),
        xml="@id",
    )

    id: str = Field(
        ...,
        description=(
            "An identifier for this software that is unique across all SoftwareTypes."
        ),
        xml="@id",
    )

    version: Optional[str] = Field(
        default=None,
        description="The software version.",
        xml="@version",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

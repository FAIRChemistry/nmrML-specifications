import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl


@forge_signature
class CV(sdRDM.DataModel):

    """Information about an ontology or CV source and a short 'lookup' tag to refer to. Must have an id attribute to be used as a reference tag with which to refer to this particular Controlled Vocabulary source description (e.g., from the cvLabel attribute, in CVParamType elements)."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    full_name: str = Field(
        ...,
        description=(
            "The usual name for the resource (e.g. The MSI-NMR Controlled Vocabulary)."
        ),
        xml="@fullName",
    )

    version: Optional[str] = Field(
        default=None,
        description="The version of the CV from which the referred-to terms are drawn.",
        xml="@version",
    )

    uri: AnyUrl = Field(
        ...,
        description="The URI for the resource.",
        xml="@URI",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

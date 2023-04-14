import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV


@forge_signature
class CVList(sdRDM.DataModel):

    """Container for one or more controlled vocabulary definitions."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvlistINDEX"),
        xml="@id",
    )

    cv: CV = Field(
        ...,
        description=(
            "Information about an ontology or CV source and a short 'lookup' tag to"
            " refer to."
        ),
        xml="cv",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

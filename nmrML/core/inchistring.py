import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class InChiString(sdRDM.DataModel):

    """Captures the compound structure as an InChI, which allows for capturing a chemical structure as a string example: InChI=1S/C7H11N3O2/c1-10-3-5(9-4-10)2-6(8)7(11)12/h3-4,6H,2,8H2,1H3,(H,11,12)/t6-/m0/s1."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("inchistringINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

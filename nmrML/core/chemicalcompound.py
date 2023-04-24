import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .compoundstructure import CompoundStructure
from .compoundidentifierlist import CompoundIdentifierList


@forge_signature
class ChemicalCompound(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("chemicalcompoundINDEX"),
        xml="@id",
    )

    identifier_list: Optional[CompoundIdentifierList] = Field(
        default=None,
        description="none given",
        xml="identifierList",
    )

    structure: Optional[CompoundStructure] = Field(
        default=None,
        description="none given",
        xml="structure",
    )

    name: Optional[str] = Field(
        default=None,
        description="none given",
        xml="@name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

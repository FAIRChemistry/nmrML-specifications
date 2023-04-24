import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .bondlist import BondList
from .atomlist import AtomList


@forge_signature
class CompoundStructure(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("compoundstructureINDEX"),
        xml="@id",
    )

    atom_list: AtomList = Field(
        ...,
        description="none given",
        xml="atomList",
    )

    bond_list: BondList = Field(
        ...,
        description="none given",
        xml="bondList",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

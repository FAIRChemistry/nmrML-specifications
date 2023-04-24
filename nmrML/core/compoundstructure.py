import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .atomlist import AtomList
from .bondlist import BondList


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
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

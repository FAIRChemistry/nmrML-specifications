import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .bond import Bond
from .bondorder import BondOrder


@forge_signature
class BondList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("bondlistINDEX"),
        xml="@id",
    )

    bond: List[Bond] = Field(
        description="none given",
        multiple=True,
        xml="bond",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

    def add_to_bond(
        self,
        order: BondOrder,
        atom_references: List[str] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Bond' to attribute bond

        Args:
            id (str): Unique identifier of the 'Bond' object. Defaults to 'None'.
            order (): The order of the bond connecting two atoms. A single bond should be "1", a double bond should be "2", a triple bond should be "3"..
            atom_references (): Contains a list of atom IDs seperated by a space. The atom ids are the atoms connected by the bond. For example: "a1 a2". Defaults to ListPlus()
        """

        params = {
            "order": order,
            "atom_references": atom_references,
        }

        if id is not None:
            params["id"] = id

        self.bond.append(Bond(**params))

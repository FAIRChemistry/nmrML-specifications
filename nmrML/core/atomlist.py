import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from typing import Any

from .atom import Atom
from .elementtype import ElementType


@forge_signature
class AtomList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("atomlistINDEX"),
        xml="@id",
    )

    atom: List[Atom] = Field(
        description="none given",
        multiple=True,
        xml="atom",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

    def add_to_atom(
        self,
        id: str,
        element_type: ElementType,
        x: Any,
        y: Any,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Atom' to attribute atom

        Args:
            id (str): Unique identifier of the 'Atom' object. Defaults to 'None'.
            id (): An identifier unique to the file only, so that it can be referenced by the bond elements as well as by the spectrum annotations. Most people use 'a1', 'a2', ... , 'aN'..
            element_type (): The symbol for the element. For example: 'H','C' or 'Fe'..
            x (): The x position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure..
            y (): The y position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure..
        """

        params = {
            "id": id,
            "element_type": element_type,
            "x": x,
            "y": y,
        }

        if id is not None:
            params["id"] = id

        self.atom.append(Atom(**params))

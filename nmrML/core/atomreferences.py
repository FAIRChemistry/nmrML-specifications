import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from typing import Any

from .elementtype import ElementType
from .atom import Atom


@forge_signature
class AtomReferences(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("atomreferencesINDEX"),
        xml="@id",
    )

    atom_references: List[Union[Atom, str]] = Field(
        reference="Atom.id",
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="@atomRefs",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    def add_to_atom_references(
        self, element_type: ElementType, x: Any, y: Any, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Atom' to attribute atom_references

        Args:
            id (str): Unique identifier of the 'Atom' object. Defaults to 'None'.
            element_type (): The symbol for the element. For example: 'H','C' or 'Fe'..
            x (): The x position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure..
            y (): The y position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure..
        """

        params = {
            "element_type": element_type,
            "x": x,
            "y": y,
        }

        if id is not None:
            params["id"] = id

        self.atom_references.append(Atom(**params))

    @validator("atom_references")
    def get_atom_references_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .atom import Atom

        if isinstance(value, Atom):
            return value.id
        elif isinstance(value, str):
            return value
        elif value is None:
            return value
        else:
            raise TypeError(
                f"Expected types [Atom, str] got '{type(value).__name__}' instead."
            )

import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .solute import Solute
from .valuewithunit import ValueWithUnit


@forge_signature
class AdditionalSoluteList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("additionalsolutelistINDEX"),
        xml="@id",
    )

    solute: List[Solute] = Field(
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="solute",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_solute_to_solute(
        self,
        concentration_in_sample: ValueWithUnit,
        name: str,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Solute' to attribute solute

        Args:
            id (str): Unique identifier of the 'Solute' object. Defaults to 'None'.
            concentration_in_sample (): none given.
            name (): none given.
        """

        params = {
            "concentration_in_sample": concentration_in_sample,
            "name": name,
        }

        if id is not None:
            params["id"] = id

        self.solute.append(Solute(**params))

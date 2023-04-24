import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .atomreferences import AtomReferences
from .cvterm import CVTerm
from .peaklist import PeakList
from .multiplet import Multiplet


@forge_signature
class AtomAssignmentList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("atomassignmentlistINDEX"),
        xml="@id",
    )

    multiplet: List[Multiplet] = Field(
        description=(
            "A cluster of 1 or more peaks that corresponds to specific atoms in a"
            " chemical structure."
        ),
        multiple=True,
        xml="multiplet",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

    def add_to_multiplet(
        self,
        atoms: AtomReferences,
        multiplicity: CVTerm,
        center: float,
        peak_list: Optional[PeakList] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Multiplet' to attribute multiplet

        Args:
            id (str): Unique identifier of the 'Multiplet' object. Defaults to 'None'.
            atoms (): Lists the atomRefs for atoms in the chemical structure that contribute to the multiplet. If the corresponding atoms are unknown than the list can be blank..
            multiplicity (): A description of the type of multiplet that is annotated. For exmample a singlet, a doublet, a doublet of doublets, etc..
            center (): The center of the multiplet in ppm..
            peak_list (): A list of the positions and amplitudes of the peaks in the multiplet. Optional if the peaks are not identified. In which case the 'center' attribute offers a hint for annotation.. Defaults to None
        """

        params = {
            "atoms": atoms,
            "multiplicity": multiplicity,
            "center": center,
            "peak_list": peak_list,
        }

        if id is not None:
            params["id"] = id

        self.multiplet.append(Multiplet(**params))

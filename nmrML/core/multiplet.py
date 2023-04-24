import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cvterm import CVTerm
from .peaklist import PeakList
from .atomreferences import AtomReferences


@forge_signature
class Multiplet(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("multipletINDEX"),
        xml="@id",
    )

    atoms: AtomReferences = Field(
        ...,
        description=(
            "Lists the atomRefs for atoms in the chemical structure that contribute to"
            " the multiplet. If the corresponding atoms are unknown than the list can"
            " be blank."
        ),
        xml="atoms",
    )

    multiplicity: CVTerm = Field(
        ...,
        description=(
            "A description of the type of multiplet that is annotated. For exmample a"
            " singlet, a doublet, a doublet of doublets, etc."
        ),
        xml="multiplicity",
    )

    peak_list: Optional[PeakList] = Field(
        default=None,
        description=(
            "A list of the positions and amplitudes of the peaks in the multiplet."
            " Optional if the peaks are not identified. In which case the 'center'"
            " attribute offers a hint for annotation."
        ),
        xml="peakList",
    )

    center: float = Field(
        ...,
        description="The center of the multiplet in ppm.",
        xml="@center",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

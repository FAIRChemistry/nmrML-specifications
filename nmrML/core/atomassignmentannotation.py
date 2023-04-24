import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .atomassignmentlist import AtomAssignmentList
from .chemicalcompound import ChemicalCompound
from .spectrum import Spectrum


@forge_signature
class AtomAssignmentAnnotation(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("atomassignmentannotationINDEX"),
        xml="@id",
    )

    chemical_compound: ChemicalCompound = Field(
        ...,
        description="none given",
        xml="chemicalCompound",
    )

    atom_assignment_list: Optional[AtomAssignmentList] = Field(
        default=None,
        description=(
            "A list of annotated peak clusters in the spectrum and the atoms that they"
            " correspond to."
        ),
        xml="atomAssignmentList",
    )

    spectrum_reference: Union[Spectrum, str] = Field(
        ...,
        reference="Spectrum.id",
        description=(
            "A reference to the id of the spectrum that this annotation is for."
        ),
        xml="@spectrumRef",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

    @validator("spectrum_reference")
    def get_spectrum_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .spectrum import Spectrum

        if isinstance(value, Spectrum):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Spectrum, str] got '{type(value).__name__}' instead."
            )

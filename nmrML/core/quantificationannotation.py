import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .cvterm import CVTerm
from .spectrum import Spectrum
from .quantifiedcompoundlist import QuantifiedCompoundList


@forge_signature
class QuantificationAnnotation(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("quantificationannotationINDEX"),
        xml="@id",
    )

    quantification_method: CVTerm = Field(
        ...,
        description="none given",
        xml="quantificationMethod",
    )

    quantification_compound_list: QuantifiedCompoundList = Field(
        ...,
        description=(
            "A list of the quantified chemical compounds and the associated information"
            " about clusters of peaks in the spectrum."
        ),
        xml="quantifiedCompoundList",
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
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
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

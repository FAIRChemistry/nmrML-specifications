import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV


@forge_signature
class CVTerm(sdRDM.DataModel):

    """This element holds additional data or annotation as a simple CV term with nofurther values (Parameters) associated with it. Only controlled CV terms values are allowed here."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvtermINDEX"),
        xml="@id",
    )

    cv_reference: Union[CV, str] = Field(
        ...,
        reference="CV.id",
        description=(
            "A reference to the CV 'id' attribute as defined in the cvList in this"
            " nmrML file."
        ),
        xml="@cvRef",
    )

    accession: str = Field(
        ...,
        description=(
            "The accession number of the referred-to term in the named resource (e.g.:"
            " NMR:000012)."
        ),
        xml="@accession",
    )

    name: str = Field(
        ...,
        description=(
            "The actual name for the parameter, from the referred-to controlled"
            " vocabulary. This should be the preferred name associated with the"
            " specified accession number."
        ),
        xml="@name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    @validator("cv_reference")
    def get_cv_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .cv import CV

        if isinstance(value, CV):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [CV, str] got '{type(value).__name__}' instead."
            )

import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV


@forge_signature
class CVParameter(sdRDM.DataModel):

    """This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvparameterINDEX"),
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

    value: Optional[str] = Field(
        default=None,
        description=(
            "The value for the parameter; may be absent if not appropriate, or a"
            " numeric or symbolic value, or may itself be CV (legal values for a"
            " parameter should be enumerated and defined in the ontology)."
        ),
        xml="@value",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
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

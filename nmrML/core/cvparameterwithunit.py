import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV


@forge_signature
class CVParameterWithUnit(sdRDM.DataModel):

    """This element holds additional data or annotation. Only controlled values are allowed here."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvparameterwithunitINDEX"),
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

    unit_cv_reference: Union[CV, str, None] = Field(
        default=None,
        reference="CV.id",
        description=(
            "If a unit term is referenced, this attribute must refer to the CV 'id'"
            " attribute defined in the cvList in this nmrML file."
        ),
        xml="@unitCvRef",
    )

    unit_accession: Optional[str] = Field(
        default=None,
        description=(
            "An optional CV accession number for the unit term associated with the"
            " value, if any (e.g., 'UO:0000266' for 'electron volt')."
        ),
        xml="@unitAccession",
    )

    unit_name: Optional[str] = Field(
        default=None,
        description=(
            "An optional CV name for the unit accession number, if any (e.g., 'electron"
            " volt' for 'UO:0000266' )."
        ),
        xml="@unitName",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
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

    @validator("unit_cv_reference")
    def get_unit_cv_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .cv import CV

        if isinstance(value, CV):
            return value.id
        elif isinstance(value, str):
            return value
        elif value is None:
            return value
        else:
            raise TypeError(
                f"Expected types [CV, str] got '{type(value).__name__}' instead."
            )

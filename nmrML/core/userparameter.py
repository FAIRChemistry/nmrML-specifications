import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV


@forge_signature
class UserParameter(sdRDM.DataModel):

    """Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("userparameterINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="The name for the parameter.",
        xml="@name",
    )

    value_type: Optional[str] = Field(
        default=None,
        description=(
            "The datatype of the parameter, where appropriate (e.g.: xsd:float)."
        ),
        xml="@valueType",
    )

    value: Optional[str] = Field(
        default=None,
        description="The value for the parameter, where appropriate.",
        xml="@value",
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

    unit_cv_reference: Union[CV, str, None] = Field(
        default=None,
        reference="CV.id",
        description=(
            "If a unit term is referenced, this attribute must refer to the CV 'id'"
            " attribute defined in the cvList in this nmrML file."
        ),
        xml="@unitCvRef",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
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

import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator

from typing import Any

from .cv import CV


@forge_signature
class AxisWithUnit(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("axiswithunitINDEX"),
        xml="@id",
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
            " volt' for 'UO:0000266')."
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

    start_value: Optional[Any] = Field(
        default=None,
        description="none given",
        xml="@startValue",
    )

    end_value: Optional[Any] = Field(
        default=None,
        description="none given",
        xml="@endValue",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
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

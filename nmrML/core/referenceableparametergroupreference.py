import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .referenceableparametergroup import ReferenceableParameterGroup


@forge_signature
class ReferenceableParameterGroupReference(sdRDM.DataModel):

    """A reference to a previously defined ParamGroup, which is a reusable container of one or more cvParams."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("referenceableparametergroupreferenceINDEX"),
        xml="@id",
    )

    reference: Union[ReferenceableParameterGroup, str] = Field(
        ...,
        reference="ReferenceableParameterGroup.id",
        description="Reference to the id attribute in a referenceableParamGroup.",
        xml="@ref",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

    @validator("reference")
    def get_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .referenceableparametergroup import ReferenceableParameterGroup

        if isinstance(value, ReferenceableParameterGroup):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                "Expected types [ReferenceableParameterGroup, str] got"
                f" '{type(value).__name__}' instead."
            )

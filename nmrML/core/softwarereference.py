import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software


@forge_signature
class SoftwareReference(sdRDM.DataModel):

    """Reference to a previously defined software element."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwarereferenceINDEX"),
        xml="@id",
    )

    reference: Union[Software, str] = Field(
        ...,
        reference="Software.id",
        description=(
            "This attribute must be used to reference the 'id' attribute of a software"
            " element."
        ),
        xml="@ref",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

    @validator("reference")
    def get_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .software import Software

        if isinstance(value, Software):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Software, str] got '{type(value).__name__}' instead."
            )

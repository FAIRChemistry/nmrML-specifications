import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .contact import Contact


@forge_signature
class ContactReference(sdRDM.DataModel):

    """Reference to a previously defined sourceFile."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactreferenceINDEX"),
        xml="@id",
    )

    reference: Union[Contact, str] = Field(
        ...,
        reference="Contact.id",
        description=(
            "This attribute must reference the 'id' of the contact node in the"
            " contactList."
        ),
        xml="@ref",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    @validator("reference")
    def get_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .contact import Contact

        if isinstance(value, Contact):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Contact, str] got '{type(value).__name__}' instead."
            )

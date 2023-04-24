
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .parametergroup import ParameterGroup


@forge_signature
class Contact(ParameterGroup):

    """A person's name and information on how to communicate with them. Must have an id attribute."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactINDEX"),
        xml="@id",
    )

    full_name: str = Field(
        ...,
        description="Name of the contact person.",
        xml="@fullname",
    )

    url: Optional[AnyUrl] = Field(
        default=None,
        description=(
            "Uniform Resource Locator related to the contact person or organization."
        ),
        xml="@url",
    )

    address: Optional[str] = Field(
        default=None,
        description="Postal address of the contact person or organization.",
        xml="@address",
    )

    organization: Optional[str] = Field(
        default=None,
        description="Home institution of the contact person.",
        xml="@organization",
    )

    email: str = Field(
        ...,
        description="Email address of the contact person or organization.",
        xml="@email",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

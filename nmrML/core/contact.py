
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl
from pydantic import EmailStr

from .parametergroup import ParameterGroup


@forge_signature
class Contact(ParameterGroup):

    """A person's name and information on how to communicate with them."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactINDEX"),
        xml="@id",
    )

    id: str = Field(
        ...,
        description="An identifier for this contact.",
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

    email: EmailStr = Field(
        ...,
        description="Email address of the contact person or organization.",
        xml="@email",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

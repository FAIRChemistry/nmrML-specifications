import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import EmailStr
from pydantic import AnyUrl

from .contact import Contact


@forge_signature
class ContactList(sdRDM.DataModel):

    """A list containing one or more person's name and information on how to communicate with them."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactlistINDEX"),
        xml="@id",
    )

    contact: List[Contact] = Field(
        description="A person's name and information on how to communicate with them.",
        multiple=True,
        xml="contact",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

    def add_to_contact(
        self,
        id: str,
        full_name: str,
        email: EmailStr,
        url: Optional[AnyUrl] = None,
        address: Optional[str] = None,
        organization: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Contact' to attribute contact

        Args:
            id (str): Unique identifier of the 'Contact' object. Defaults to 'None'.
            id (): An identifier for this contact..
            full_name (): Name of the contact person..
            email (): Email address of the contact person or organization..
            url (): Uniform Resource Locator related to the contact person or organization.. Defaults to None
            address (): Postal address of the contact person or organization.. Defaults to None
            organization (): Home institution of the contact person.. Defaults to None
        """

        params = {
            "id": id,
            "full_name": full_name,
            "email": email,
            "url": url,
            "address": address,
            "organization": organization,
        }

        if id is not None:
            params["id"] = id

        self.contact.append(Contact(**params))

import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .contact import Contact
from .contactreference import ContactReference


@forge_signature
class ContactReferenceList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactreferencelistINDEX"),
        xml="@id",
    )

    contact_reference: List[ContactReference] = Field(
        description="Reference to a previously defined sourceFile.",
        multiple=True,
        xml="contactRef",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

    def add_to_contact_reference(
        self, reference: Contact, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'ContactReference' to attribute contact_reference

        Args:
            id (str): Unique identifier of the 'ContactReference' object. Defaults to 'None'.
            reference (): This attribute must reference the 'id' of the contact node in the contactList..
        """

        params = {
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.contact_reference.append(ContactReference(**params))

import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .contactreference import ContactReference
from .contact import Contact


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
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
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

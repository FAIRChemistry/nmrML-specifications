import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .softwarereference import SoftwareReference
from .software import Software


@forge_signature
class SoftwareReferenceList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwarereferencelistINDEX"),
        xml="@id",
    )

    software_reference: List[SoftwareReference] = Field(
        description="Reference to a previously defined sourceFile.",
        default_factory=ListPlus,
        multiple=True,
        xml="softwareRef",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

    def add_software_reference_to_software_reference(
        self, reference: Software, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'SoftwareReference' to attribute software_reference

        Args:
            id (str): Unique identifier of the 'SoftwareReference' object. Defaults to 'None'.
            reference (): This attribute must be used to reference the 'id' attribute of a software element..
        """

        params = {
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.software_reference.append(SoftwareReference(**params))
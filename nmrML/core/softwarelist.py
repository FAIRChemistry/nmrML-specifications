import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software


@forge_signature
class SoftwareList(sdRDM.DataModel):

    """List and descriptions of software used to acquire and/or process the data in this nmrML file."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwarelistINDEX"),
        xml="@id",
    )

    software: List[Software] = Field(
        description=(
            "A software program used during the acquisition of the spectra or"
            " processing of the FID."
        ),
        multiple=True,
        xml="software",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_software_to_software(
        self, id: str, version: Optional[str] = None, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Software' to attribute software

        Args:
            id (str): Unique identifier of the 'Software' object. Defaults to 'None'.
            id (): An identifier for this software that is unique across all SoftwareTypes..
            version (): The software version.. Defaults to None
        """

        params = {
            "id": id,
            "version": version,
        }

        if id is not None:
            params["id"] = id

        self.software.append(Software(**params))

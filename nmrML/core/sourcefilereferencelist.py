import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .sourcefile import SourceFile
from .sourcefilereference import SourceFileReference


@forge_signature
class SourceFileReferenceList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sourcefilereferencelistINDEX"),
        xml="@id",
    )

    source_file_reference: List[SourceFileReference] = Field(
        description="Reference to a previously defined sourceFile.",
        default_factory=ListPlus,
        multiple=True,
        xml="sourceFileRef",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    def add_to_source_file_reference(
        self, reference: SourceFile, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'SourceFileReference' to attribute source_file_reference

        Args:
            id (str): Unique identifier of the 'SourceFileReference' object. Defaults to 'None'.
            reference (): This attribute must reference the 'id' of the appropriate sourceFile..
        """

        params = {
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.source_file_reference.append(SourceFileReference(**params))

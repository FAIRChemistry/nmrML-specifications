import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .sourcefile import SourceFile
from .processingparameterfilereference import ProcessingParameterFileReference


@forge_signature
class ProcessingParameterFileReferenceList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processingparameterfilereferencelistINDEX"),
        xml="@id",
    )

    processing_parameter_file_reference: List[ProcessingParameterFileReference] = Field(
        description="Reference to a previously defined sourceFile.",
        multiple=True,
        xml="processingParameterFileRef",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    def add_to_processing_parameter_file_reference(
        self, reference: SourceFile, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'ProcessingParameterFileReference' to attribute processing_parameter_file_reference

        Args:
            id (str): Unique identifier of the 'ProcessingParameterFileReference' object. Defaults to 'None'.
            reference (): This attribute must reference the 'id' of the sourceFile node in the sourceFileList..
        """

        params = {
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.processing_parameter_file_reference.append(
            ProcessingParameterFileReference(**params)
        )

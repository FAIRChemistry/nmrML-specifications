import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .processingparameterfilereference import ProcessingParameterFileReference
from .sourcefile import SourceFile


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
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
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

import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .sourcefile import SourceFile
from .acquisitionparameterfilereference import AcquisitionParameterFileReference


@forge_signature
class AcquisitionParameterFileReferenceList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionparameterfilereferencelistINDEX"),
        xml="@id",
    )

    acquisition_parameter_file_reference: List[AcquisitionParameterFileReference] = (
        Field(
            description="Reference to a previously defined sourceFile.",
            multiple=True,
            xml="acquisitionParameterFileRef",
            default_factory=ListPlus,
        )
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    def add_to_acquisition_parameter_file_reference(
        self, reference: SourceFile, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'AcquisitionParameterFileReference' to attribute acquisition_parameter_file_reference

        Args:
            id (str): Unique identifier of the 'AcquisitionParameterFileReference' object. Defaults to 'None'.
            reference (): This attribute must reference the 'id' of the sourceFile node in the sourceFileList.
        """

        params = {
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.acquisition_parameter_file_reference.append(
            AcquisitionParameterFileReference(**params)
        )

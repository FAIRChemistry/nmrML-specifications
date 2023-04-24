import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator


from .sourcefile import SourceFile


@forge_signature
class ProcessingParameterFileReference(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processingparameterfilereferenceINDEX"),
        xml="@id",
    )

    reference: Union[SourceFile, str] = Field(
        ...,
        reference="SourceFile.id",
        description=(
            "This attribute must reference the 'id' of the sourceFile node in the"
            " sourceFileList."
        ),
        xml="@ref",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

    @validator("reference")
    def get_reference_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .sourcefile import SourceFile

        if isinstance(value, SourceFile):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [SourceFile, str] got '{type(value).__name__}'"
                " instead."
            )

import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .parametergroup import ParameterGroup


@forge_signature
class FileDescription(sdRDM.DataModel):

    """Information pertaining to the entire nmrML file (i.e. not specific to any part of the data set) is stored here. The FileDescriptionType element is intended to contain a summary description of the current nmrML file, for example it could say that the file has a 1D FID, a processed spectra, and a peak picked spectra. It does not point to source files or anything like that. It is intended to make it easy to determine what is inside a file without having to look for different element types etc and build a summary yourself. RawSpectrumFile would not be a good name. nmrMLInstanceSummary might be a more intuitive name."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("filedescriptionINDEX"),
        xml="@id",
    )

    file_content: ParameterGroup = Field(
        ...,
        description=(
            "This summarizes the different types of spectra that can be expected in the"
            " file. This is expected to aid processing software in skipping files that"
            " do not contain appropriate spectrum types for it. It should also describe"
            " the nativeID format used in the file by referring to an appropriate CV"
            " term."
        ),
        xml="fileContent",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

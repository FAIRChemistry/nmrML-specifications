
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .parametergroup import ParameterGroup


@forge_signature
class SourceFile(ParameterGroup):

    """Description of the source file, including location and type. The SourceFileType element is intended to be a generic element that points to a file that was used to produce the spectrum or the nmrML file. It could point to an FID file, a procpar file, a pulse program file etc. nmrExperimentSourceFile could be a good name but I personally think that SourceFile is an intuitive name already. Requied to have an id attribute."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sourcefileINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description=(
            "Name of the source file, without reference to location (either URI or"
            " local path)."
        ),
        xml="@name",
    )

    location: AnyUrl = Field(
        ...,
        description="URI-formatted location where the file was retrieved.",
        xml="@location",
    )

    sha1: Optional[str] = Field(
        default=None,
        description="sha1 of the file.",
        xml="@sha1",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

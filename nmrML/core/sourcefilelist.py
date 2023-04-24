import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .sourcefile import SourceFile


@forge_signature
class SourceFileList(sdRDM.DataModel):

    """List and descriptions of the source files this nmrML document was generated or derived from."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sourcefilelistINDEX"),
        xml="@id",
    )

    source_file: List[SourceFile] = Field(
        description=(
            "Description of the source file, including location and type. The"
            " SourceFileType element is intended to be a generic element that points to"
            " a file that was used to produce the spectrum or the nmrML file. It could"
            " point to an FID file, a procpar file, a pulse program file etc."
            " nmrExperimentSourceFile could be a good name but I personally think that"
            " SourceFile is an intuitive name already."
        ),
        multiple=True,
        xml="sourceFile",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

    def add_to_source_file(
        self,
        name: str,
        location: AnyUrl,
        sha1: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SourceFile' to attribute source_file

        Args:
            id (str): Unique identifier of the 'SourceFile' object. Defaults to 'None'.
            name (): Name of the source file, without reference to location (either URI or local path)..
            location (): URI-formatted location where the file was retrieved..
            sha1 (): sha1 of the file.. Defaults to None
        """

        params = {
            "name": name,
            "location": location,
            "sha1": sha1,
        }

        if id is not None:
            params["id"] = id

        self.source_file.append(SourceFile(**params))

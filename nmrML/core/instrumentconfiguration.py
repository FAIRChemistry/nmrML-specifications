
from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .parametergroup import ParameterGroup
from .softwarereference import SoftwareReference
from .software import Software


@forge_signature
class InstrumentConfiguration(ParameterGroup):

    """Description of a particular hardware configuration of a NMR spectrometer. For software configuration, use a ReferenceableParamGroup element."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("instrumentconfigurationINDEX"),
        xml="@id",
    )

    software_reference: List[SoftwareReference] = Field(
        description="Reference to a previously defined software element.",
        default_factory=ListPlus,
        multiple=True,
        xml="softwareRef",
    )

    id: str = Field(
        ...,
        description="An identifier for this instrument configuration.",
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

    def add_to_software_reference(
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

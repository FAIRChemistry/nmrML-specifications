
from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software
from .parametergroup import ParameterGroup
from .softwarereference import SoftwareReference


@forge_signature
class InstrumentConfiguration(ParameterGroup):

    """Description of a particular hardware configuration of a NMR spectrometer. For software configuration, use a ReferenceableParamGroup element. Required to have an id attribute."""

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

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
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

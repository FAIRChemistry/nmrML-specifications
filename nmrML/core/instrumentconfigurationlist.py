import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .softwarereference import SoftwareReference
from .instrumentconfiguration import InstrumentConfiguration


@forge_signature
class InstrumentConfigurationList(sdRDM.DataModel):

    """List and descriptions of instrument configurations. At least one instrument configuration must be specified, even if it is only to specify that the instrument is unknown. In that case, the "instrument model" term is used to indicate the unknown instrument in the instrumentConfiguration."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("instrumentconfigurationlistINDEX"),
        xml="@id",
    )

    instrument_configuration: List[InstrumentConfiguration] = Field(
        description=(
            "Description of a particular hardware configuration of a NMR spectrometer."
            " For software configuration, use a ReferenceableParamGroup element."
        ),
        multiple=True,
        xml="instrumentConfiguration",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

    def add_to_instrument_configuration(
        self,
        id: str,
        software_reference: List[SoftwareReference] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'InstrumentConfiguration' to attribute instrument_configuration

        Args:
            id (str): Unique identifier of the 'InstrumentConfiguration' object. Defaults to 'None'.
            id (): An identifier for this instrument configuration..
            software_reference (): Reference to a previously defined software element.. Defaults to ListPlus()
        """

        params = {
            "id": id,
            "software_reference": software_reference,
        }

        if id is not None:
            params["id"] = id

        self.instrument_configuration.append(InstrumentConfiguration(**params))

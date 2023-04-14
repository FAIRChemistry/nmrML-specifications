import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .peak import Peak


@forge_signature
class PeakList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("peaklistINDEX"),
        xml="@id",
    )

    peak: List[Peak] = Field(
        description="none given",
        multiple=True,
        xml="peak",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_peak_to_peak(
        self,
        _: float,
        amplitude: Optional[float] = None,
        width: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Peak' to attribute peak

        Args:
            id (str): Unique identifier of the 'Peak' object. Defaults to 'None'.
            _ (): none given.
            amplitude (): none given. Defaults to None
            width (): none given. Defaults to None
        """

        params = {
            "_": _,
            "amplitude": amplitude,
            "width": width,
        }

        if id is not None:
            params["id"] = id

        self.peak.append(Peak(**params))

import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .valuewithunit import ValueWithUnit
from .peaklist import PeakList
from .clusterlist import ClusterList
from .quantifiedcompound import QuantifiedCompound


@forge_signature
class QuantifiedCompoundList(sdRDM.DataModel):

    """Caputures information about analytes that have been quantified in a mixture. The infromation is about quantification and identification of the analytes."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("quantifiedcompoundlistINDEX"),
        xml="@id",
    )

    quantified_compound: List[QuantifiedCompound] = Field(
        description="none given",
        multiple=True,
        xml="quantifiedCompound",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

    def add_to_quantified_compound(
        self,
        concentration: ValueWithUnit,
        cluster_list: Optional[ClusterList] = None,
        peak_list: Optional[PeakList] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'QuantifiedCompound' to attribute quantified_compound

        Args:
            id (str): Unique identifier of the 'QuantifiedCompound' object. Defaults to 'None'.
            concentration (): none given.
            cluster_list (): A list of clusters of peaks that are aligned with the spectrum for quantification.. Defaults to None
            peak_list (): A list of the positions and amplitudes of the peaks that are associated with the compound. This is an alternative to the cluster list for the case where you want to record a fit but discard some of the information about the library you used to fit the spectrum.. Defaults to None
        """

        params = {
            "concentration": concentration,
            "cluster_list": cluster_list,
            "peak_list": peak_list,
        }

        if id is not None:
            params["id"] = id

        self.quantified_compound.append(QuantifiedCompound(**params))

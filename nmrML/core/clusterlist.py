import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cluster import Cluster
from .peaklist import PeakList


@forge_signature
class ClusterList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("clusterlistINDEX"),
        xml="@id",
    )

    cluster: List[Cluster] = Field(
        description="none given",
        multiple=True,
        xml="cluster",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

    def add_to_cluster(
        self,
        peak_list: PeakList,
        center: Optional[float] = None,
        shift: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Cluster' to attribute cluster

        Args:
            id (str): Unique identifier of the 'Cluster' object. Defaults to 'None'.
            peak_list (): A list of the positions and amplitudes of the peaks in the multiplet. Optional if the peaks are not identified. In which case the 'center' attribute offers a hint for annotation..
            center (): none given. Defaults to None
            shift (): none given. Defaults to None
        """

        params = {
            "peak_list": peak_list,
            "center": center,
            "shift": shift,
        }

        if id is not None:
            params["id"] = id

        self.cluster.append(Cluster(**params))

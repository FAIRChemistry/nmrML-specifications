
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitiondimensionparameterset import AcquisitionDimensionParameterSet
from .acquisitionparameterset import AcquisitionParameterSet


@forge_signature
class AcquisitionParameterSet1D(AcquisitionParameterSet):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionparameterset1dINDEX"),
        xml="@id",
    )

    direct_dimension_parameter_set: Optional[AcquisitionDimensionParameterSet] = Field(
        default=None,
        description="none given",
        xml="DirectDimensionParameterSet",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

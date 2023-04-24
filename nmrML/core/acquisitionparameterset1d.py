
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitionparameterset import AcquisitionParameterSet
from .acquisitiondimensionparameterset import AcquisitionDimensionParameterSet


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
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

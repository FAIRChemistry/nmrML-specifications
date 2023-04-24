
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .firstdimensionprocessingparameterset import FirstDimensionProcessingParameterSet


@forge_signature
class HigherDimensionProcessingParameterSet(FirstDimensionProcessingParameterSet):

    """Parameters recorded when raw data set is processed to create a spectra that are specific to the second dimension."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("higherdimensionprocessingparametersetINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

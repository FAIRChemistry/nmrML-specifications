
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .spectrum import Spectrum
from .firstdimensionprocessingparameterset import FirstDimensionProcessingParameterSet


@forge_signature
class Spectrum1D(Spectrum):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spectrum1dINDEX"),
        xml="@id",
    )

    first_dimension_processing_parameter_set: Optional[
        FirstDimensionProcessingParameterSet
    ] = Field(
        default=None,
        description=(
            "Optional additional information about processing that was used to create"
            " the frequency domain spectrum. This information is relevant to the first"
            " dimension of data only."
        ),
        xml="firstDimensionProcessingParameterSet",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )


from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .firstdimensionprocessingparameterset import FirstDimensionProcessingParameterSet
from .spectrum import Spectrum


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
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )


from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .projected3dprocessingparameterset import Projected3DProcessingParameterSet
from .spectrum import Spectrum
from .firstdimensionprocessingparameterset import FirstDimensionProcessingParameterSet
from .higherdimensionprocessingparameterset import HigherDimensionProcessingParameterSet


@forge_signature
class SpectrumMultiD(Spectrum):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spectrummultidINDEX"),
        xml="@id",
    )

    first_dimension_processing_parameter_set: FirstDimensionProcessingParameterSet = (
        Field(
            ...,
            description="none given",
            xml="firstDimensionProcessingParameterSet",
        )
    )

    higher_dimension_processing_parameter_set: List[
        HigherDimensionProcessingParameterSet
    ] = Field(
        description="none given",
        multiple=True,
        xml="higherDimensionProcessingParameterSet",
        default_factory=ListPlus,
    )

    projected_3d_processing_parameter_set: Optional[
        Projected3DProcessingParameterSet
    ] = Field(
        default=None,
        description="none given",
        xml="projected3DProcessingParameterSet",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_higher_dimension_processing_parameter_set_to_higher_dimension_processing_parameter_set(
        self, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'HigherDimensionProcessingParameterSet' to attribute higher_dimension_processing_parameter_set

        Args:
            id (str): Unique identifier of the 'HigherDimensionProcessingParameterSet' object. Defaults to 'None'.
        """

        params = {}

        if id is not None:
            params["id"] = id

        self.higher_dimension_processing_parameter_set.append(
            HigherDimensionProcessingParameterSet(**params)
        )

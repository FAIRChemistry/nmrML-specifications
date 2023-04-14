import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .projected3dprocessingparameterset import Projected3DProcessingParameterSet
from .firstdimensionprocessingparameterset import FirstDimensionProcessingParameterSet
from .spectrummultid import SpectrumMultiD
from .higherdimensionprocessingparameterset import HigherDimensionProcessingParameterSet
from .spectrum1d import Spectrum1D


@forge_signature
class SpectrumList(sdRDM.DataModel):

    """List and descriptions of spectra."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spectrumlistINDEX"),
        xml="@id",
    )

    spectrum_1d: List[Spectrum1D] = Field(
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="spectrum1D",
    )

    spectrum_multi_d: List[SpectrumMultiD] = Field(
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="spectrumMultiD",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_spectrum1_d_to_spectrum_1d(
        self,
        first_dimension_processing_parameter_set: Optional[
            FirstDimensionProcessingParameterSet
        ] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Spectrum1D' to attribute spectrum_1d

        Args:
            id (str): Unique identifier of the 'Spectrum1D' object. Defaults to 'None'.
            first_dimension_processing_parameter_set (): Optional additional information about processing that was used to create the frequency domain spectrum. This information is relevant to the first dimension of data only.. Defaults to None
        """

        params = {
            "first_dimension_processing_parameter_set": (
                first_dimension_processing_parameter_set
            ),
        }

        if id is not None:
            params["id"] = id

        self.spectrum_1d.append(Spectrum1D(**params))

    def add_spectrum_multi_d_to_spectrum_multi_d(
        self,
        first_dimension_processing_parameter_set: FirstDimensionProcessingParameterSet,
        higher_dimension_processing_parameter_set: List[
            HigherDimensionProcessingParameterSet
        ] = ListPlus(),
        projected_3d_processing_parameter_set: Optional[
            Projected3DProcessingParameterSet
        ] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SpectrumMultiD' to attribute spectrum_multi_d

        Args:
            id (str): Unique identifier of the 'SpectrumMultiD' object. Defaults to 'None'.
            first_dimension_processing_parameter_set (): none given.
            higher_dimension_processing_parameter_set (): none given. Defaults to ListPlus()
            projected_3d_processing_parameter_set (): none given. Defaults to None
        """

        params = {
            "first_dimension_processing_parameter_set": (
                first_dimension_processing_parameter_set
            ),
            "higher_dimension_processing_parameter_set": (
                higher_dimension_processing_parameter_set
            ),
            "projected_3d_processing_parameter_set": (
                projected_3d_processing_parameter_set
            ),
        }

        if id is not None:
            params["id"] = id

        self.spectrum_multi_d.append(SpectrumMultiD(**params))

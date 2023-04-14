
from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitionparameterset import AcquisitionParameterSet
from .hadamardparameterset import HadamardParameterSet
from .valuewithunit import ValueWithUnit
from .acquisitiondimensionparameterset import AcquisitionDimensionParameterSet
from .cvparameter import CVParameter
from .binarydataarray import BinaryDataArray
from .cvterm import CVTerm


@forge_signature
class AcquisitionParameterSetMultiD(AcquisitionParameterSet):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionparametersetmultidINDEX"),
        xml="@id",
    )

    hadamard_parameter_set: Optional[HadamardParameterSet] = Field(
        default=None,
        description=(
            "TODO needs to be a list of frequencies, but could allow for other"
            " parameters."
        ),
        xml="hadamardParameterSet",
    )

    direct_dimension_parameter_set: AcquisitionDimensionParameterSet = Field(
        ...,
        description="none given",
        xml="directDimensionParameterSet",
    )

    encoding_scheme: CVParameter = Field(
        ...,
        description="Quadrature detection method.",
        xml="encodingScheme",
    )

    indirect_dimension_parameter_set: List[AcquisitionDimensionParameterSet] = Field(
        description="Required once for each indirect dimension that is measured.",
        multiple=True,
        xml="indirectDimensionParameterSet",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

    def add_acquisition_dimension_parameter_set_to_indirect_dimension_parameter_set(
        self,
        acquisition_nucleus: CVTerm,
        effective_excitation_field: ValueWithUnit,
        sweep_width: ValueWithUnit,
        pulse_width: ValueWithUnit,
        irradiation_frequency: ValueWithUnit,
        irradiation_frequency_offset: ValueWithUnit,
        sampling_strategy: CVTerm,
        decoupled: bool,
        number_of_data_points: int,
        decoupling_method: Optional[CVTerm] = None,
        decoupling_nucleus: Optional[CVTerm] = None,
        sampling_time_points: Optional[BinaryDataArray] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'AcquisitionDimensionParameterSet' to attribute indirect_dimension_parameter_set

        Args:
            id (str): Unique identifier of the 'AcquisitionDimensionParameterSet' object. Defaults to 'None'.
            acquisition_nucleus (): none given.
            effective_excitation_field (): Replacing the hardPulse parameter, would be automatically calculated from the pulse width in the procs file. If you say the pulse width you also have to specify the excitation angle so this way is more compact/useful. Should be recorded in Tesla.
            sweep_width (): Should be in ppm and Hz..
            pulse_width (): 90° pulse width, measured in µs.
            irradiation_frequency (): none given.
            irradiation_frequency_offset (): none given.
            sampling_strategy (): none given.
            decoupled (): none given.
            number_of_data_points (): none given.
            decoupling_method (): none given. Defaults to None
            decoupling_nucleus (): none given. Defaults to None
            sampling_time_points (): The time domain for the samples. Allows for capturing off grid points and non-uniform sampling.. Defaults to None
        """

        params = {
            "acquisition_nucleus": acquisition_nucleus,
            "effective_excitation_field": effective_excitation_field,
            "sweep_width": sweep_width,
            "pulse_width": pulse_width,
            "irradiation_frequency": irradiation_frequency,
            "irradiation_frequency_offset": irradiation_frequency_offset,
            "sampling_strategy": sampling_strategy,
            "decoupled": decoupled,
            "number_of_data_points": number_of_data_points,
            "decoupling_method": decoupling_method,
            "decoupling_nucleus": decoupling_nucleus,
            "sampling_time_points": sampling_time_points,
        }

        if id is not None:
            params["id"] = id

        self.indirect_dimension_parameter_set.append(
            AcquisitionDimensionParameterSet(**params)
        )

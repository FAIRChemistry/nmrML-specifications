import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cvterm import CVTerm
from .valuewithunit import ValueWithUnit
from .samplingtimepoints import SamplingTimePoints


@forge_signature
class AcquisitionDimensionParameterSet(sdRDM.DataModel):

    """Descriptions of the acquisition parameters set prior to the start of data acquisition specific to each NMR analysis dimension."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitiondimensionparametersetINDEX"),
        xml="@id",
    )

    decoupling_method: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="decouplingMethod",
    )

    acquisition_nucleus: CVTerm = Field(
        ...,
        description="none given",
        xml="acquisitionNucleus",
    )

    effective_excitation_field: ValueWithUnit = Field(
        ...,
        description=(
            "Replacing the hardPulse parameter, would be automatically calculated from"
            " the pulse width in the procs file. If you say the pulse width you also"
            " have to specify the excitation angle so this way is more compact/useful."
            " Should be recorded in Tesla"
        ),
        xml="effectiveExcitationField",
    )

    sweep_width: ValueWithUnit = Field(
        ...,
        description="Should be in ppm and Hz.",
        xml="sweepWidth",
    )

    pulse_width: ValueWithUnit = Field(
        ...,
        description="90° pulse width, measured in µs",
        xml="pulseWidth",
    )

    irradiation_frequency: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="irradiationFrequency",
    )

    irradiation_frequency_offset: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="irradiationFrequencyOffset",
    )

    decoupling_nucleus: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="decouplingNucleus",
    )

    sampling_strategy: CVTerm = Field(
        ...,
        description="none given",
        xml="samplingStrategy",
    )

    sampling_time_points: Optional[SamplingTimePoints] = Field(
        default=None,
        description=(
            "The time domain for the samples. Allows for capturing off grid points and"
            " non-uniform sampling."
        ),
        xml="samplingTimePoints",
    )

    decoupled: bool = Field(
        ...,
        description="none given",
        xml="@decoupled",
    )

    number_of_data_points: int = Field(
        ...,
        description="none given",
        xml="@numberOfDataPoints",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

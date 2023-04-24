import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .contactreferencelist import ContactReferenceList
from .valuewithunit import ValueWithUnit
from .softwarereference import SoftwareReference
from .acquisitionparameterfilereferencelist import AcquisitionParameterFileReferenceList
from .sourcefilereference import SourceFileReference
from .cvterm import CVTerm
from .pulsesequence import PulseSequence
from .cvparameter import CVParameter


@forge_signature
class AcquisitionParameterSet(sdRDM.DataModel):

    """Base type for the list with the descriptions of the acquisition settings applied prior to the start of data acquisition."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionparametersetINDEX"),
        xml="@id",
    )

    contact_reference_list: Optional[ContactReferenceList] = Field(
        default=None,
        description="none given",
        xml="contactRefList",
    )

    software_reference: Optional[SoftwareReference] = Field(
        default=None,
        description="none given",
        xml="softwareRef",
    )

    sample_container: CVTerm = Field(
        ...,
        description=(
            "The container used to introduc the sample into the autosampler. Example:"
            " tube, flow probe, rotor. Must reference a CV term."
        ),
        xml="sampleContainer",
    )

    sample_acquisition_temperature: ValueWithUnit = Field(
        ...,
        description="The temperature of the sample during the acquisition.",
        xml="sampleAcquisitionTemperature",
    )

    solvent_suppression_method: Optional[CVParameter] = Field(
        default=None,
        description=(
            "This tag captures the instrument inherent solvent (usually water)"
            " suppression method used during acquisition."
        ),
        xml="solventSuppressionMethod",
    )

    spinning_rate: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="spinningRate",
    )

    relaxation_delay: ValueWithUnit = Field(
        ...,
        description="none given",
        xml="relaxationDelay",
    )

    pulse_sequence: PulseSequence = Field(
        ...,
        description=(
            "A description of the pulse sequence using CV params/terms, and reference"
            " to the pulse sequence file if the source is available."
        ),
        xml="pulseSequence",
    )

    shaped_pulse_file: Optional[SourceFileReference] = Field(
        default=None,
        description=(
            "A reference to the pulse shape file, from the power section of the Bruker"
            " acquisition software. Example: gauss"
        ),
        xml="shapedPulseFile",
    )

    group_delay: Optional[ValueWithUnit] = Field(
        default=None,
        description=(
            "In the case of Bruker spectra a dead time or group delay can be observed"
            " in the FID: it starts with very small values and then, after some points"
            " (usually between 60-80 points) the normal FID starts. It can be a number"
            " with decimal value."
        ),
        xml="groupDelay",
    )

    acquisition_parameter_reference_list: Optional[
        AcquisitionParameterFileReferenceList
    ] = Field(
        default=None,
        description="none given",
        xml="acquisitionParameterRefList",
    )

    number_of_steady_state_scans: int = Field(
        ...,
        description=(
            "Steady state scans taken in an NMR acquisition without collecting data."
            " Also known as dummy scans. The pulse sequence is the same for a steady"
            " state scan, the only difference is that data is not collected. (More info"
            " here: http://u-of-o-nmr-facility.blogspot.ca/2010/04/dummy-scans.html)"
        ),
        xml="@numberOfSteadyStateScans",
    )

    number_of_scans: int = Field(
        ...,
        description="The number of transients/scans.",
        xml="@numberOfScans",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

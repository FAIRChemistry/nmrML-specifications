import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .binarydataarray import BinaryDataArray
from .axiswithunit import AxisWithUnit
from .softwarereferencelist import SoftwareReferenceList
from .processingparameterset import ProcessingParameterSet
from .processingparameterfilereferencelist import ProcessingParameterFileReferenceList


@forge_signature
class Spectrum(sdRDM.DataModel):

    """A spectrum that is the result of processing the acquisition and a description of the process used to create it."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spectrumINDEX"),
        xml="@id",
    )

    processing_software_reference_list: Optional[SoftwareReferenceList] = Field(
        default=None,
        description="none given",
        xml="processingSoftwareRefList",
    )

    processing_parameter_file_reference_list: Optional[
        ProcessingParameterFileReferenceList
    ] = Field(
        default=None,
        description="none given",
        xml="processingParameterFileRefList",
    )

    spectrum_data_array: BinaryDataArray = Field(
        ...,
        description=(
            "The 1D spectrum is represented as either a set of y-axis values at equal"
            " x-axis intervals or a set of (x,y) pairs."
        ),
        xml="spectrumDataArray",
    )

    x_axis: AxisWithUnit = Field(
        ...,
        description="none given",
        xml="xAxis",
    )

    processing_parameter_set: Optional[ProcessingParameterSet] = Field(
        default=None,
        description=(
            "Optional information about processing that was used to create the"
            " frequency domain spectrum."
        ),
        xml="processingParameterSet",
    )

    number_of_data_points: int = Field(
        ...,
        description=(
            "The number of (x,y) points in the spectrum. This is needed to read the"
            " binary data."
        ),
        xml="@numberOfDataPoints",
    )

    id: str = Field(
        ...,
        description=(
            "An ID for the spectrum so that it can be referenced within the file for"
            " spectrum annotations."
        ),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description=(
            "An (optional) name so that it can be differentiated other than by its rank"
            " if multiple spectra are embedded within the file."
        ),
        xml="@name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

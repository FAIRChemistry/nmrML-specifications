import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cvterm import CVTerm


@forge_signature
class ProcessingParameterSet(sdRDM.DataModel):

    """Optional information about processing that was used to create the frequency domain spectrum."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processingparametersetINDEX"),
        xml="@id",
    )

    post_acquisition_solvent_suppression_method: Optional[CVTerm] = Field(
        default=None,
        description="The method used for post acquisition solvent suppression.",
        xml="postAcquisitionSolventSuppressionMethod",
    )

    calibration_compound: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="calibrationCompound",
    )

    data_transformation_method: Optional[CVTerm] = Field(
        default=None,
        description=(
            "The method used for time-based to frequency-based data transformation."
        ),
        xml="dataTransformationMethod",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e3f5163276869b6a63cd09beffbe1786e5fcf7a8"
    )

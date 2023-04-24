import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV
from .valuewithunit import ValueWithUnit
from .cvterm import CVTerm
from .cvparameter import CVParameter


@forge_signature
class FirstDimensionProcessingParameterSet(sdRDM.DataModel):

    """Parameters recorded when raw data set is processed to create a spectra that are specific to a dimension."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("firstdimensionprocessingparametersetINDEX"),
        xml="@id",
    )

    zero_order_phase_correction: Optional[ValueWithUnit] = Field(
        default=None,
        description="none given",
        xml="zeroOrderPhaseCorrection",
    )

    first_order_phase_correction: Optional[ValueWithUnit] = Field(
        default=None,
        description="none given",
        xml="firstOrderPhaseCorrection",
    )

    calibration_reference_shift: Optional[ValueWithUnit] = Field(
        default=None,
        description="none given",
        xml="calibrationReferenceShift",
    )

    spectral_denoising_method: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="spectralDenoisingMethod",
    )

    window_function_method: CVTerm = Field(
        ...,
        description="none given",
        xml="windowFunctionMethod",
    )

    window_function_parameter: List[CVParameter] = Field(
        description="The parameters used in the window function method.",
        multiple=True,
        xml="windowFunctionParameter",
        default_factory=ListPlus,
    )

    baseline_correction_method: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="baselineCorrectionMethod",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

    def add_to_window_function_parameter(
        self,
        cv_reference: CV,
        accession: str,
        name: str,
        value: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CVParameter' to attribute window_function_parameter

        Args:
            id (str): Unique identifier of the 'CVParameter' object. Defaults to 'None'.
            cv_reference (): A reference to the CV 'id' attribute as defined in the cvList in this nmrML file..
            accession (): The accession number of the referred-to term in the named resource (e.g.: NMR:000012)..
            name (): The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number..
            value (): The value for the parameter; may be absent if not appropriate, or a numeric or symbolic value, or may itself be CV (legal values for a parameter should be enumerated and defined in the ontology).. Defaults to None
        """

        params = {
            "cv_reference": cv_reference,
            "accession": accession,
            "name": name,
            "value": value,
        }

        if id is not None:
            params["id"] = id

        self.window_function_parameter.append(CVParameter(**params))

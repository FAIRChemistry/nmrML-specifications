import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .fieldfrequencylock import FieldFrequencyLock
from .additionalsolutelist import AdditionalSoluteList
from .cvparameterwithunit import CVParameterWithUnit
from .concentrationstandard import ConcentrationStandard
from .cv import CV
from .cvparameter import CVParameter
from .cvterm import CVTerm


@forge_signature
class Sample(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    original_biological_sample_ph: Optional[float] = Field(
        default=None,
        description="none given",
        xml="originalBiologicalSamplepH",
    )

    post_buffer_ph: Optional[float] = Field(
        default=None,
        description="none given",
        xml="postBufferpH",
    )

    buffer: Optional[CVTerm] = Field(
        default=None,
        description="none given",
        xml="buffer",
    )

    field_frequency_lock: FieldFrequencyLock = Field(
        ...,
        description="none given",
        xml="fieldFrequencyLock",
    )

    chemical_shift_standard: CVParameter = Field(
        ...,
        description="none given",
        xml="chemicalShiftStandard",
    )

    solvent_type: List[CVParameterWithUnit] = Field(
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="solventType",
    )

    additional_solute_list: Optional[AdditionalSoluteList] = Field(
        default=None,
        description="none given",
        xml="additionalSoluteList",
    )

    concentration_standard: Optional[ConcentrationStandard] = Field(
        default=None,
        description="none given",
        xml="concentrationStandard",
    )

    original_biological_sample_reference: AnyUrl = Field(
        ...,
        description="none given",
        xml="@originalBiologicalSampleReference",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

    def add_to_solvent_type(
        self,
        cv_reference: CV,
        accession: str,
        name: str,
        value: Optional[str] = None,
        unit_cv_reference: Optional[CV] = None,
        unit_accession: Optional[str] = None,
        unit_name: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CVParameterWithUnit' to attribute solvent_type

        Args:
            id (str): Unique identifier of the 'CVParameterWithUnit' object. Defaults to 'None'.
            cv_reference (): A reference to the CV 'id' attribute as defined in the cvList in this nmrML file..
            accession (): The accession number of the referred-to term in the named resource (e.g.: NMR:000012)..
            name (): The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number..
            value (): The value for the parameter; may be absent if not appropriate, or a numeric or symbolic value, or may itself be CV (legal values for a parameter should be enumerated and defined in the ontology).. Defaults to None
            unit_cv_reference (): If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.. Defaults to None
            unit_accession (): An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').. Defaults to None
            unit_name (): An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266' ).. Defaults to None
        """

        params = {
            "cv_reference": cv_reference,
            "accession": accession,
            "name": name,
            "value": value,
            "unit_cv_reference": unit_cv_reference,
            "unit_accession": unit_accession,
            "unit_name": unit_name,
        }

        if id is not None:
            params["id"] = id

        self.solvent_type.append(CVParameterWithUnit(**params))

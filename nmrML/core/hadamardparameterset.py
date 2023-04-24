import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV
from .valuewithunit import ValueWithUnit


@forge_signature
class HadamardParameterSet(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("hadamardparametersetINDEX"),
        xml="@id",
    )

    hadamard_frequency: List[ValueWithUnit] = Field(
        description="Required if and only if the encoding type is Hadamard.",
        default_factory=ListPlus,
        multiple=True,
        xml="hadamardFrequency",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

    def add_to_hadamard_frequency(
        self,
        value: Optional[str] = None,
        unit_accession: Optional[str] = None,
        unit_name: Optional[str] = None,
        unit_cv_reference: Optional[CV] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ValueWithUnit' to attribute hadamard_frequency

        Args:
            id (str): Unique identifier of the 'ValueWithUnit' object. Defaults to 'None'.
            value (): none given. Defaults to None
            unit_accession (): An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').. Defaults to None
            unit_name (): An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266').. Defaults to None
            unit_cv_reference (): If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.. Defaults to None
        """

        params = {
            "value": value,
            "unit_accession": unit_accession,
            "unit_name": unit_name,
            "unit_cv_reference": unit_cv_reference,
        }

        if id is not None:
            params["id"] = id

        self.hadamard_frequency.append(ValueWithUnit(**params))

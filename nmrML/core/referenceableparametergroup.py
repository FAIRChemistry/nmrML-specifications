import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .userparameter import UserParameter
from .cvparameter import CVParameter
from .cv import CV


@forge_signature
class ReferenceableParameterGroup(sdRDM.DataModel):

    """A collection of CVParam and UserParam elements that can be referenced from elsewhere in this nmrML document by using the 'paramGroupRef' element in that location to reference the required 'id' attribute value of this element."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("referenceableparametergroupINDEX"),
        xml="@id",
    )

    cv_parameter: List[CVParameter] = Field(
        description=(
            "This element holds additional data or annotation. In contrast to"
            " CVTermType, here a pair of CV term plus a value (=Parameter) is captured."
            " Only controlled values are allowed here."
        ),
        default_factory=ListPlus,
        multiple=True,
        xml="cvParam",
    )

    user_parameter: List[UserParameter] = Field(
        description=(
            "Uncontrolled user parameters (essentially allowing free text). Before"
            " using these, one should verify whether there is an appropriate CV term"
            " available, and if so, use the CV term instead."
        ),
        default_factory=ListPlus,
        multiple=True,
        xml="userParam",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

    def add_to_cv_parameter(
        self,
        cv_reference: CV,
        accession: str,
        name: str,
        value: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CVParameter' to attribute cv_parameter

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

        self.cv_parameter.append(CVParameter(**params))

    def add_to_user_parameter(
        self,
        name: str,
        value_type: Optional[str] = None,
        value: Optional[str] = None,
        unit_accession: Optional[str] = None,
        unit_name: Optional[str] = None,
        unit_cv_reference: Optional[CV] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'UserParameter' to attribute user_parameter

        Args:
            id (str): Unique identifier of the 'UserParameter' object. Defaults to 'None'.
            name (): The name for the parameter..
            value_type (): The datatype of the parameter, where appropriate (e.g.: xsd:float).. Defaults to None
            value (): The value for the parameter, where appropriate.. Defaults to None
            unit_accession (): An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').. Defaults to None
            unit_name (): An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266' ).. Defaults to None
            unit_cv_reference (): If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.. Defaults to None
        """

        params = {
            "name": name,
            "value_type": value_type,
            "value": value,
            "unit_accession": unit_accession,
            "unit_name": unit_name,
            "unit_cv_reference": unit_cv_reference,
        }

        if id is not None:
            params["id"] = id

        self.user_parameter.append(UserParameter(**params))

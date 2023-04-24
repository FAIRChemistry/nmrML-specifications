import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .userparameter import UserParameter
from .referenceableparametergroup import ReferenceableParameterGroup
from .cvparameter import CVParameter


@forge_signature
class ReferenceableParameterGroupList(sdRDM.DataModel):

    """Container for a list of referenceableParamGroups."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("referenceableparametergrouplistINDEX"),
        xml="@id",
    )

    referenceable_parameter_group: List[ReferenceableParameterGroup] = Field(
        description=(
            "A collection of CVParam and UserParam elements that can be referenced from"
            " elsewhere in this nmrML document by using the 'paramGroupRef' element in"
            " that location to reference the 'id' attribute value of this element."
        ),
        multiple=True,
        xml="referenceableParamGroup",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

    def add_to_referenceable_parameter_group(
        self,
        cv_parameter: List[CVParameter] = ListPlus(),
        user_parameter: List[UserParameter] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ReferenceableParameterGroup' to attribute referenceable_parameter_group

        Args:
            id (str): Unique identifier of the 'ReferenceableParameterGroup' object. Defaults to 'None'.
            cv_parameter (): This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here.. Defaults to ListPlus()
            user_parameter (): Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead.. Defaults to ListPlus()
        """

        params = {
            "cv_parameter": cv_parameter,
            "user_parameter": user_parameter,
        }

        if id is not None:
            params["id"] = id

        self.referenceable_parameter_group.append(ReferenceableParameterGroup(**params))

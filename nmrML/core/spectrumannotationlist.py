import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .quantificationannotation import QuantificationAnnotation
from .atomassignmentannotation import AtomAssignmentAnnotation


@forge_signature
class SpectrumAnnotationList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spectrumannotationlistINDEX"),
        xml="@id",
    )

    atom_assignment: Optional[AtomAssignmentAnnotation] = Field(
        default=None,
        description=(
            "An annotation for assigning atoms in a chemical structure to peaks in a"
            " spectrum."
        ),
        xml="atomAssignment",
    )

    quantification: Optional[QuantificationAnnotation] = Field(
        default=None,
        description=(
            "An annotation for capturing the quantification of a complex mixture in an"
            " NMR experiment. The annotation captures the alighnment of clusters of"
            " peaks to the spectrum, the associated chemical compounds, and the"
            " quantification information."
        ),
        xml="quantification",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

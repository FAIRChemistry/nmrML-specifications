import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .cvterm import CVTerm
from .sample import Sample
from .fieldfrequencylock import FieldFrequencyLock
from .cvparameter import CVParameter
from .cvparameterwithunit import CVParameterWithUnit
from .concentrationstandard import ConcentrationStandard
from .additionalsolutelist import AdditionalSoluteList


@forge_signature
class SampleList(sdRDM.DataModel):

    """List and descriptions of samples."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("samplelistINDEX"),
        xml="@id",
    )

    sample: List[Sample] = Field(
        description="none given",
        multiple=True,
        xml="sample",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2ebd8fdd8a0250af187f7adce763035c7e18d071"
    )

    def add_sample_to_sample(
        self,
        field_frequency_lock: FieldFrequencyLock,
        chemical_shift_standard: CVParameter,
        original_biological_sample_reference: AnyUrl,
        original_biological_sample_ph: Optional[float] = None,
        post_buffer_ph: Optional[float] = None,
        buffer: Optional[CVTerm] = None,
        solvent_type: List[CVParameterWithUnit] = ListPlus(),
        additional_solute_list: Optional[AdditionalSoluteList] = None,
        concentration_standard: Optional[ConcentrationStandard] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:
            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.
            field_frequency_lock (): none given.
            chemical_shift_standard (): none given.
            original_biological_sample_reference (): none given.
            original_biological_sample_ph (): none given. Defaults to None
            post_buffer_ph (): none given. Defaults to None
            buffer (): none given. Defaults to None
            solvent_type (): none given. Defaults to ListPlus()
            additional_solute_list (): none given. Defaults to None
            concentration_standard (): none given. Defaults to None
        """

        params = {
            "field_frequency_lock": field_frequency_lock,
            "chemical_shift_standard": chemical_shift_standard,
            "original_biological_sample_reference": (
                original_biological_sample_reference
            ),
            "original_biological_sample_ph": original_biological_sample_ph,
            "post_buffer_ph": post_buffer_ph,
            "buffer": buffer,
            "solvent_type": solvent_type,
            "additional_solute_list": additional_solute_list,
            "concentration_standard": concentration_standard,
        }

        if id is not None:
            params["id"] = id

        self.sample.append(Sample(**params))

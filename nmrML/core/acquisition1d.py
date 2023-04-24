import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitionparameterset1d import AcquisitionParameterSet1D
from .fiddata import FIDData


@forge_signature
class Acquisition1D(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisition1dINDEX"),
        xml="@id",
    )

    acquisition_parameter_set: AcquisitionParameterSet1D = Field(
        ...,
        description="Note, steady state scan is also know as dummy scan.",
        xml="acquisitionParameterSet",
    )

    fidData: Optional[FIDData] = Field(
        default=None,
        description=(
            "The FID is stored here as a binary blob. Byte ordering is always little"
            " endian (Intel style). Computers using a different endian style must"
            " convert to/from little endian when writing/reading nmrML. The FID should"
            " be converted into a Complex64 array before encoding. The base64 encoded"
            " binary data. The byte order is always 'little endian'."
        ),
        xml="fidData",
    )

    id: Optional[str] = Field(
        default=None,
        description=(
            "An ID for the spectrum so that it can be referenced within the file for"
            " spectrum annotations."
        ),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description=(
            "A (optional) name so that it can be differentiated other than by its rank"
            " if multiple spectra are embedded within the file"
        ),
        xml="@name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="86966ee3cfc9fa75941388f3d759adb484a881f7"
    )

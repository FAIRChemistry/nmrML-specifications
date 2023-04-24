import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .acquisitionparametersetmultid import AcquisitionParameterSetMultiD
from .fiddata import FIDData


@forge_signature
class AcquisitionMultiD(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("acquisitionmultidINDEX"),
        xml="@id",
    )

    acquisition_parameter_set: AcquisitionParameterSetMultiD = Field(
        ...,
        description="none given",
        xml="acquisitionParameterSet",
    )

    fid_data: FIDData = Field(
        ...,
        description=(
            "The FID is stored here as a binary blob. Byte ordering is always little"
            " endian (Intel style). Computers using a different endian style must"
            " convert to/from little endian when writing/reading nmrML. The FID should"
            " be converted into a Complex64 array before encoding. The base64 encoded"
            " binary data. The byte order is always 'little endian'."
        ),
        xml="fidData",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .binarydataarray import BinaryDataArray
from .acquisitionparametersetmultid import AcquisitionParameterSetMultiD


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

    fid_data: BinaryDataArray = Field(
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
        default="git://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fb3af02b2009219cecf14787bd4869cf16c181a9"
    )

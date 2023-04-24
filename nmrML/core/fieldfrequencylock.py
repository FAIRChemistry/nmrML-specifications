import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class FieldFrequencyLock(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("fieldfrequencylockINDEX"),
        xml="@id",
    )

    field_frequency_lock_name: str = Field(
        ...,
        description="none given",
        xml="@fieldFrequencyLockName",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="59a674b3af38dd54e849336756c049f42e0b18bf"
    )

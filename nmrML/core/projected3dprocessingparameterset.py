import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Projected3DProcessingParameterSet(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("projected3dprocessingparametersetINDEX"),
        xml="@id",
    )

    projection_angle: Optional[float] = Field(
        default=None,
        description="none given",
        xml="@projectionAngle",
    )

    positive_projection_method: Optional[bool] = Field(
        default=None,
        description="none given",
        xml="@positiveProjectionMethod",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="03764412e456b4c22b9b0a9f4e2784fcfd450402"
    )

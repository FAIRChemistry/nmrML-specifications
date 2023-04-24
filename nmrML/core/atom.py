import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from typing import Any

from .elementtype import ElementType

@forge_signature
class Atom(sdRDM.DataModel):

                
    """no documentation given"""
    
    id: str = Field(
            description="Unique identifier of the given object.",
            default_factory=IDGenerator("atomINDEX"),
            xml="@id"
    )
    
    id: str = Field(
    ...,
    
    description="An identifier unique to the file only, so that it can be referenced by the bond elements as well as by the spectrum annotations. Most people use "a1", "a2", ... , "aN".",
    
    xml="@id",
    
    )

    element_type: ElementType = Field(
    ...,
    
    description="The symbol for the element. For example: "H","C" or "Fe".",
    
    xml="@elementType",
    
    )

    x: Any = Field(
    ...,
    
    description="The x position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure.",
    
    xml="@x",
    
    )

    y: Any = Field(
    ...,
    
    description="The y position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure.",
    
    xml="@y",
    
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/FAIRChemistry/nmrML-specifications.git")
    __commit__: Optional[str] = PrivateAttr(default="fb3af02b2009219cecf14787bd4869cf16c181a9")
    


import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .bondorder import BondOrder

@forge_signature
class Bond(sdRDM.DataModel):

                
    """no documentation given"""
    
    id: str = Field(
            description="Unique identifier of the given object.",
            default_factory=IDGenerator("bondINDEX"),
            xml="@id"
    )
    
    atom_references: List[str] = Field(
    
    
    description="Contains a list of atom IDs seperated by a space. The atom ids are the atoms connected by the bond. For example: "a1 a2"",
    
    multiple=True,
    
    xml="@atomRefs",
    
    default_factory=ListPlus,
    
    )

    order: BondOrder = Field(
    ...,
    
    description="The order of the bond connecting two atoms. A single bond should be "1", a double bond should be "2", a triple bond should be "3".",
    
    xml="@order",
    
    )

    __repo__: Optional[str] = PrivateAttr(default="https://github.com/FAIRChemistry/nmrML-specifications.git")
    __commit__: Optional[str] = PrivateAttr(default="7c335cd7f4514607a6424461701c24ad7bd5d549")
    


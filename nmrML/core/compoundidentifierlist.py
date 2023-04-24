import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .cvterm import CVTerm
from .cv import CV
from .compounddatabaseidentifier import CompoundDatabaseIdentifier


@forge_signature
class CompoundIdentifierList(sdRDM.DataModel):

    """no documentation given"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("compoundidentifierlistINDEX"),
        xml="@id",
    )

    identifier: List[CVTerm] = Field(
        description=(
            "Captures compound identifiers coming from an ontology. Usually CHEBI."
        ),
        default_factory=ListPlus,
        multiple=True,
        xml="identifier",
    )

    database_identifier: List[CompoundDatabaseIdentifier] = Field(
        description="none given",
        default_factory=ListPlus,
        multiple=True,
        xml="databaseIdentifier",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7c335cd7f4514607a6424461701c24ad7bd5d549"
    )

    def add_to_identifier(
        self, cv_reference: CV, accession: str, name: str, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'CVTerm' to attribute identifier

        Args:
            id (str): Unique identifier of the 'CVTerm' object. Defaults to 'None'.
            cv_reference (): A reference to the CV 'id' attribute as defined in the cvList in this nmrML file..
            accession (): The accession number of the referred-to term in the named resource (e.g.: NMR:000012)..
            name (): The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number..
        """

        params = {
            "cv_reference": cv_reference,
            "accession": accession,
            "name": name,
        }

        if id is not None:
            params["id"] = id

        self.identifier.append(CVTerm(**params))

    def add_to_database_identifier(
        self, identifier: str, uri: AnyUrl, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'CompoundDatabaseIdentifier' to attribute database_identifier

        Args:
            id (str): Unique identifier of the 'CompoundDatabaseIdentifier' object. Defaults to 'None'.
            identifier (): none given.
            uri (): none given.
        """

        params = {
            "identifier": identifier,
            "uri": uri,
        }

        if id is not None:
            params["id"] = id

        self.database_identifier.append(CompoundDatabaseIdentifier(**params))

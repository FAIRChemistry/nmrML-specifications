import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import AnyUrl

from .acquisition import Acquisition
from .contactlist import ContactList
from .spectrumannotationlist import SpectrumAnnotationList
from .filedescription import FileDescription
from .referenceableparametergrouplist import ReferenceableParameterGroupList
from .softwarelist import SoftwareList
from .spectrumlist import SpectrumList
from .cvlist import CVList
from .sourcefilelist import SourceFileList
from .instrumentconfigurationlist import InstrumentConfigurationList
from .samplelist import SampleList


@forge_signature
class nmrML(sdRDM.DataModel):

    """This is the root element for the COordination Of Standards In MetabOlomicS nmrML schema, which is intended to capture the use of a nuclear magnetic resonance spectrometer, the data generated, and the initial processing of that data (to the level of the peak list). May have an id attribute."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("nmrmlINDEX"),
        xml="@id",
    )

    cv_list: CVList = Field(
        ...,
        description="Container for one or more controlled vocabulary definitions.",
        xml="cvList",
    )

    file_description: FileDescription = Field(
        ...,
        description=(
            "Information pertaining to the entire nmrML file (i.e. not specific to any"
            " part of the data set) is stored here. The FileDescriptionType element is"
            " intended to contain a summary description of the current nmrML file, for"
            " example it could say that the file has a 1D FID, a processed spectra, and"
            " a peak picked spectra. It does not point to source files or anything like"
            " that. It is intended to make it easy to determine what is inside a file"
            " without having to look for different element types etc and build a"
            " summary yourself. RawSpectrumFile would not be a good name."
            " nmrMLInstanceSummary might be a more intuitive name."
        ),
        xml="fileDescription",
    )

    contact_list: Optional[ContactList] = Field(
        default=None,
        description=(
            "A list containing one or more person's name and information on how to"
            " communicate with them."
        ),
        xml="contactList",
    )

    referenceable_parameter_group_list: Optional[ReferenceableParameterGroupList] = (
        Field(
            default=None,
            description="Container for a list of referenceableParamGroups",
            xml="referenceableParamGroupList",
        )
    )

    source_file_list: Optional[SourceFileList] = Field(
        default=None,
        description=(
            "List and descriptions of the source files this nmrML document was"
            " generated or derived from."
        ),
        xml="sourceFileList",
    )

    software_list: Optional[SoftwareList] = Field(
        default=None,
        description=(
            "List and descriptions of software used to acquire and/or process the data"
            " in this nmrML file."
        ),
        xml="softwareList",
    )

    instrument_configuration_list: InstrumentConfigurationList = Field(
        ...,
        description=(
            "List and descriptions of instrument configurations. At least one"
            " instrument configuration must be specified, even if it is only to specify"
            " that the instrument is unknown. In that case, the 'instrument model' term"
            " is used to indicate the unknown instrument in the"
            " instrumentConfiguration."
        ),
        xml="instrumentConfigurationList",
    )

    sample_list: Optional[SampleList] = Field(
        default=None,
        description="List and descriptions of samples.",
        xml="sampleList",
    )

    acquisition: Acquisition = Field(
        ...,
        description="none given",
        xml="acquisition",
    )

    spectrum_list: Optional[SpectrumList] = Field(
        default=None,
        description=(
            "A list of frequency domain spectrum data as well as information about how"
            " the spectrum was processed. There can be more than one do to different"
            " techniques for processing the FID data."
        ),
        xml="spectrumList",
    )

    spectrum_annotation_list: Optional[SpectrumAnnotationList] = Field(
        default=None,
        description="none given",
        xml="spectrumAnnotationList",
    )

    version: str = Field(
        ...,
        description="The nmrML version used to create the document.",
        xml="@version",
    )

    accession: Optional[str] = Field(
        default=None,
        description=(
            "Optional accession number for the nmrML document. Used for storage (for"
            " example MetaboLights)"
        ),
        xml="@accession",
    )

    accession_url: Optional[AnyUrl] = Field(
        default=None,
        description=(
            "Optional attribute for retrieva of an nmrML document. Usefull when the"
            " document has been retrieved from a public database."
        ),
        xml="@accession_url",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/nmrML-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c180290a7871a8ebb547eb0570a2443ecee151d0"
    )

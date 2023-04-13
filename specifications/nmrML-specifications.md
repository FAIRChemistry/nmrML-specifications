# nmrML specification

Translation of the nmrML XSD schema v1.0-rc1 to Python object model based on sdRDM.


## Core elements


### nmrML

This is the root element for the COordination Of Standards In MetabOlomicS nmrML schema, which is intended to capture the use of a nuclear magnetic resonance spectrometer, the data generated, and the initial processing of that data (to the level of the peak list).

- __cv_list__
  - Type: [CVList](#CVList)
  - Description: Container for one or more controlled vocabulary definitions.
  - XML: cvList
- __file_description__
  - Type: [FileDescription](#FileDescription)
  - Description: Information pertaining to the entire nmrML file (i.e. not specific to any part of the data set) is stored here. The FileDescriptionType element is intended to contain a summary description of the current nmrML file, for example it could say that the file has a 1D FID, a processed spectra, and a peak picked spectra. It does not point to source files or anything like that. It is intended to make it easy to determine what is inside a file without having to look for different element types etc and build a summary yourself. RawSpectrumFile would not be a good name. nmrMLInstanceSummary might be a more intuitive name.
  - XML: fileDescription
- __contact_list__
  - Type: [ContactList](#ContactList)
  - Description: A list containing one or more person's name and information on how to communicate with them.
  - XML: contactList
- __referenceable_parameter_group_list__
  - Type: [ReferenceableParameterGroupList](#ReferenceableParameterGroupList)
  - Description: Container for a list of referenceableParamGroups
  - XML: referenceableParamGroupList
- __source_file_list__
  - Type: [SourceFileList](#SourceFileList)
  - Description: List and descriptions of the source files this nmrML document was generated or derived from.
  - XML: sourceFileList
- __software_list__
  - Type: [SoftwareList](#SoftwareList)
  - Description: List and descriptions of software used to acquire and/or process the data in this nmrML file.
  - XML: softwareList
- __instrument_configuration_list__
  - Type: [InstrumentConfigurationList](#InstrumentConfigurationList)
  - Description: List and descriptions of instrument configurations. At least one instrument configuration must be specified, even if it is only to specify that the instrument is unknown. In that case, the "instrument model" term is used to indicate the unknown instrument in the instrumentConfiguration.
  - XML: instrumentConfigurationList
- __sample_list__
  - Type: [SampleList](#SampleList)
  - Description: List and descriptions of samples.
  - XML sampleList
- __acquisition__
  - Type: [Acquisition](#Acquisition)
  - Description: none given
  - XML: acquisition
- __spectrum_list__
  - Type: [SpectrumList](#SpectrumList)
  - Description: A list of frequency domain spectrum data as well as information about how the spectrum was processed. There can be more than one do to different techniques for processing the FID data.
  - XML: spectrumList
- __spectrum_annotation_list__
  - Type: [SpectrumAnnotationList](#SpectrumAnnotationList)
  - Description: none given
  - XML: spectrumAnnotationList
- __version*__
  - Type: string
  - Description: The nmrML version used to create the document.
  - XML: @version
- __accession__
  - Type: string
  - Description: Optional accession number for the nmrML document. Used for storage (for example MetaboLights) 
  - XML: @accession
- __accession_url__
  - Type: xsAnyURI
  - Description: Optional attribute for retrieva of an nmrML document. Usefull when the document has been retrieved from a public database.
  - XML: @accession_url
- __id__
  - Type: string
  - Description: An optional ID for the nmrML document.
  - XML: @id


### QuantifiedCompound(ChemicalCompound)

no documentation given

- __concentration*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: concentration
- __cluster_list__
  - Type: [ClusterList](#ClusterList)
  - Description: A list of clusters of peaks that are aligned with the spectrum for quantification.
  - XML: clusterList
- __peak_list__
  - Type: [PeakList](#PeakList)
  - Description: A list of the positions and amplitudes of the peaks that are associated with the compound. This is an alternative to the cluster list for the case where you want to record a fit but discard some of the information about the library you used to fit the spectrum.
  - XML: peakList


### ClusterList

no documentation given

- __cluster*__
  - Type: [Cluster](#Cluster)
  - Description: none given
  - Multiple: True
  - XML: cluster


### Cluster

no documentation given

- __peak_list*__
  - Type: [PeakList](#PeakList)
  - Description: A list of the positions and amplitudes of the peaks in the multiplet. Optional if the peaks are not identified. In which case the 'center' attribute offers a hint for annotation.
  - XML: peakList
- __center__
  - Type: float
  - Description: none given
  - XML: @center
- __shift__
  - Type: float
  - Description: none given
  - XML: @shift


### ChemicalCompound

no documentation given

- __identifier_list__
  - Type: [CompoundIdentifierList](#CompoundIdentifierList)
  - Description: none given
  - XML: identifierList
- __structure__
  - Type: [CompoundStructure](#CompoundStructure)
  - Description: none given
  - XML: structure
- __name__
  - Type: str
  - Description: none given
  - XML: @name


### CompoundStructure

no documentation given

- __atom_list*__
  - Type: [AtomList](#AtomList)
  - Description: none given
  - XML: atomList
- __bond_list*__
  - Type: [BondList](#BondList)
  - Description: none given
  - XML: bondList


### AtomList

no documentation given

- __atom*__
  - Type: [Atom](#Atom)
  - Description: none given
  - Multiple: True
  - XML: atom


### Atom

no documentation given

- __id*__
  - Type: xsID
  - Description: An identifier unique to the file only, so that it can be referenced by the bond elements as well as by the spectrum annotations. Most people use "a1", "a2", ... , "aN".
  - XML: @id
- __element_type*__
  - Type: [ElementType](#ElementType)
  - Description: The symbol for the element. For example: "H","C" or "Fe".
  - XML: @elementType
- __x*__
  - Type: any
  - Description: The x position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure.
  - XML: @x
- __y*__
  - Type: any
  - Description: The y position of the element in cartesian coordinates. The cordinates along with the bond information in the bond list should allow for software to draw a 2D representation of the chemical structure.
  - XML: @y


### BondList

no documentation given

- __bond*__
  - Type: [Bond](#Bond)
  - Description: none given
  - Multiple: True
  - XML: bond


### Bond

no documentation given

- __atom_references*__
  - Type: list[str]
  - Description: Contains a list of atom IDs seperated by a space. The atom ids are the atoms connected by the bond. For example: "a1 a2"
  - XML: @atomRefs
- __order*__
  - Type: [BondOrder](#BondOrder)
  - Description: The order of the bond connecting two atoms. A single bond should be "1", a double bond should be "2", a triple bond should be "3".
  - XML: @order


### AtomAssignmentList

no documentation given

- __multiplet*__
  - Type: [Multiplet](#Multiplet)
  - Description: A cluster of 1 or more peaks that corresponds to specific atoms in a chemical structure.
  - Multiple: True
  - XML: multiplet


### Multiplet

no documentation given

- __atoms*__
  - Type: [AtomReferences](#AtomReferences)
  - Description: Lists the atomRefs for atoms in the chemical structure that contribute to the multiplet. If the corresponding atoms are unknown than the list can be blank.
  - XML: atoms
- __multiplicity*__
  - Type: [CVTerm](#CVTerm)
  - Description: A description of the type of multiplet that is annotated. For exmample a singlet, a doublet, a doublet of doublets, etc.
  - XML: multiplicity
- __peak_list__
  - Type: [PeakList](#PeakList)
  - Description: A list of the positions and amplitudes of the peaks in the multiplet. Optional if the peaks are not identified. In which case the 'center' attribute offers a hint for annotation.
  - XML: peakList
- __center*__
  - Type: float
  - Description: The center of the multiplet in ppm.
  - XML: @center


### AtomReferences

no documentation given

- __atom_references__
  - Type: List[str] 
  - Description: none given
  - XML: @atomRefs


### Peak

no documentation given

- __center*__
  - Type: float
  - Description: none given
  - XML: @center
- __amplitude__
  - Type: float
  - Description: none given
  - XML: @amplitude
- __width__
  - Type: float
  - Description: none given
  - XML: @width


### PeakList

no documentation given

- __peak*__
  - Type: [Peak](#Peak)
  - Description: none given
  - Multiple: True
  - XML: peak


### AtomAssignmentAnnotation

no documentation given

- __chemical_compound*__
  - Type: [ChemicalCompound](#ChemicalCompound)
  - Description: none given
  - XML: chemicalCompound
- __atom_assignment_list__
  - Type: [AtomAssignmentList](#AtomAssignmentList)
  - Description: A list of annotated peak clusters in the spectrum and the atoms that they correspond to.
  - XML: atomAssignmentList
- __spectrum_reference*__
  - Type: xsIDREF
  - Description: A reference to the id of the spectrum that this annotation is for.
  - XML: @spectrumRef


### CompoundIdentifierList

no documentation given

- __identifier__
  - Type: [CVTerm](#CVTerm)
  - Description: Captures compound identifiers coming from an ontology. Usually CHEBI.
  - Multiple: True
  - XML: identifier
- __database_identifier__
  - Type: [CompoundDatabaseIdentifier](#CompoundDatabaseIdentifier)
  - Description: none given
  - Multiple: True
  - XML: databaseIdentifier


### CompoundDatabaseIdentifier

Captures a database identifier and reference via URI.

- __identifier*__
  - Type: any
  - Description: none given
  - XML: @identifier
- __uri*__
  - Type: any
  - Description: none given
  - XML: @URI


### QuantificationAnnotation

no documentation given

- __quantification_method*__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: quantificationMethod
- __quantification_compound_list*__
  - Type: [QuantifiedCompoundList](#QuantifiedCompoundList)
  - Description: A list of the quantified chemical compounds and the associated information about clusters of peaks in the spectrum.
  - XML: quantifiedCompoundList
- __spectrum_reference*__
  - Type: xsIDREF
  - Description: A reference to the id of the spectrum that this annotation is for.
  - XML: @spectrumRef


### QuantifiedCompoundList

Caputures information about analytes that have been quantified in a mixture. The infromation is about quantification and identification of the analytes.

- __quantified_compound*__
  - Type: [QuantifiedCompound](#QuantifiedCompound)
  - Description: none given
  - Multiple: True
  - XML: quantifiedCompound


### SpectrumAnnotationList

no documentation given

- __atom_assignment__
  - Type: [AtomAssignmentAnnotation](#AtomAssignmentAnnotation)
  - Description: An annotation for assigning atoms in a chemical structure to peaks in a spectrum.
  - XML: atomAssignment
- __quantification__
  - Type: [QuantificationAnnotation](#QuantificationAnnotation)
  - Description: An annotation for capturing the quantification of a complex mixture in an NMR experiment. The annotation captures the alighnment of clusters of peaks to the spectrum, the associated chemical compounds, and the quantification information.
  - XML: quantification


### CVList

Container for one or more controlled vocabulary definitions.

- __cv__
  - Type: [CV](#CV)
  - Description: Information about an ontology or CV source and a short 'lookup' tag to refer to.
  - XML: cv


### CV

Information about an ontology or CV source and a short 'lookup' tag to refer to.

- __id*__
  - Type: xsID
  - Description: The short label to be used as a reference tag with which to refer to this particular Controlled Vocabulary source description (e.g., from the cvLabel attribute, in CVParamType elements).
  - XML: @id
- __full_name*__
  - Type: string
  - Description: The usual name for the resource (e.g. The MSI-NMR Controlled Vocabulary).
  - XML: @fullName
- __version__
  - Type: string
  - Description: The version of the CV from which the referred-to terms are drawn.
  - XML: @version
- __uri*__
  - Type: xsAnyURI
  - Description: The URI for the resource.
  - XML: @URI


### ContactList

A list containing one or more person's name and information on how to communicate with them.

- __contact*__
  - Type: [Contact](#Contact)
  - Description: A person's name and information on how to communicate with them.
  - Multiple: True
  - XML: contact


### Contact(ParameterGroup)

A person's name and information on how to communicate with them.

- __id*__
  - Type: xsID
  - Description: An identifier for this contact.
  - XML: @id
- __full_name*__
  - Type: string
  - Description: Name of the contact person.
  - XML: @fullname
- __url__
  - Type: xsAnyURI
  - Description: Uniform Resource Locator related to the contact person or organization.
  - XML: @url
- __address__
  - Type: string
  - Description: Postal address of the contact person or organization.
  - XML: @address
- __organization__
  - Type: string
  - Description: Home institution of the contact person.
  - XML: @organization
- __email*__
  - Type: string
  - Description: Email address of the contact person or organization.
  - XML: @email


### ContactReference

Reference to a previously defined sourceFile.

- __reference*__
  - Type: xsIDREF
  - Description: This attribute must reference the 'id' of the contact node in the contactList.
  - XML: @ref


### ContactReferenceList

no documentation given

- __contact_reference__
  - Type: [ContactReference](#ContactReference)
  - Description: Reference to a previously defined sourceFile.
  - Multiple: True
  - XML: contactRef


### AcquisitionParameterFileReference

no documentation given

- __reference*__
  - Type: xsIDREF
  - Description: This attribute must reference the 'id' of the sourceFile node in the sourceFileList
  - XML: @ref


### AcquisitionParameterFileReferenceList

no documentation given

- __acquisition_parameter_file_reference__
  - Type: [AcquisitionParameterFileReference](#AcquisitionParameterFileReference)
  - Description: Reference to a previously defined sourceFile.
  - Multiple: True
  - XML: acquisitionParameterFileRef


### FileDescription

Information pertaining to the entire nmrML file (i.e. not specific to any part of the data set) is stored here. The FileDescriptionType element is intended to contain a summary description of the current nmrML file, for example it could say that the file has a 1D FID, a processed spectra, and a peak picked spectra. It does not point to source files or anything like that. It is intended to make it easy to determine what is inside a file without having to look for different element types etc and build a summary yourself. RawSpectrumFile would not be a good name. nmrMLInstanceSummary might be a more intuitive name.

- __file_content__
  - Type: [ParameterGroup](#ParameterGroup)
  - Description: This summarizes the different types of spectra that can be expected in the file. This is expected to aid processing software in skipping files that do not contain appropriate spectrum types for it. It should also describe the nativeID format used in the file by referring to an appropriate CV term.
  - XML: fileContent


### CVTerm

This element holds additional data or annotation as a simple CV term with nofurther values (Parameters) associated with it. Only controlled CV terms values are allowed here.

- __cv_reference*__
  - Type: xsIDREF
  - Description: A reference to the CV 'id' attribute as defined in the cvList in this nmrML file.
  - XML: @cvRef
- __accession*__
  - Type: string
  - Description: The accession number of the referred-to term in the named resource (e.g.: NMR:000012).
  - XML: @accession
- __name*__
  - Type: string
  - Description: The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number.
  - XML: @name


### CVParameter

This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here.

- __cv_reference*__
  - Type: xsIDREF
  - Description: A reference to the CV 'id' attribute as defined in the cvList in this nmrML file.
  - XML: @cvRef
- __accession*__
  - Type: string
  - Description: The accession number of the referred-to term in the named resource (e.g.: NMR:000012).
  - XML: @accession
- __name*__
  - Type: string
  - Description: The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number.
  - XML: @name
- __value__
  - Type: string
  - Description: The value for the parameter; may be absent if not appropriate, or a numeric or symbolic value, or may itself be CV (legal values for a parameter should be enumerated and defined in the ontology).
  - XML: @value


### CVParameterWithUnit

This element holds additional data or annotation. Only controlled values are allowed here.

- __cv_reference*__
  - Type: xsIDREF
  - Description: A reference to the CV 'id' attribute as defined in the cvList in this nmrML file.
  - XML: @cvRef
- __accession*__
  - Type: string
  - Description: The accession number of the referred-to term in the named resource (e.g.: NMR:000012).
  - XML: @accession
- __name*__
  - Type: string
  - Description: The actual name for the parameter, from the referred-to controlled vocabulary. This should be the preferred name associated with the specified accession number.
  - XML: @name
- __value__
  - Type: string
  - Description: The value for the parameter; may be absent if not appropriate, or a numeric or symbolic value, or may itself be CV (legal values for a parameter should be enumerated and defined in the ontology).
  - XML: @value
- __unit_cv_reference__
  - Type: xsIDREF
  - Description: If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.
  - XML: @unitCvRef
- __unit_accession__
  - Type: string
  - Description: An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').
  - XML: @unitAccession
- __unit_name__
  - Type: string
  - Description: An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266' ).
  - XML: @unitName


### ValueWithUnit

This element holds a value that also has a unit. Only controlled values are allowed for the unit.

- __value__
  - Type: string
  - Description: none given
  - XML: @value
- __unit_accession__
  - Type: string
  - Description: An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').
  - XML: @unitAccession
- __unit_name__
  - Type: string
  - Description: An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266').
  - XML: @unitName
- __unit_cv_reference__
  - Type: xsIDREF
  - Description: If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.
  - XML: @unitCvRef


### UserParameter

Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead.

- __name*__
  - Type: string
  - Description: The name for the parameter.
  - XML: @name
- __value_type__
  - Type: string
  - Description: The datatype of the parameter, where appropriate (e.g.: xsd:float).
  - XML: @valueType
- __value__
  - Type: string
  - Description: The value for the parameter, where appropriate.
  - XML: @value
- __unit_accession__
  - Type: string
  - Description: An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').
  - XML: @unitAccession
- __unit_name__
  - Type: string
  - Description: An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266' ).
  - XML: @unitName
- __unit_cv_reference__
  - Type: xsIDREF
  - Description: If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.
  - XML: @unitCvRef


### ParameterGroup

Structure allowing the use of a controlled (cvParam) or uncontrolled vocabulary (userParam), or a reference to a predefined set of these in this nmrML file (paramGroupRef).

- __referenceable_parameter_group_reference__
  - Type: [ReferenceableParameterGroupReference](#ReferenceableParameterGroupReference)
  - Description: A collection of CVParam and UserParam elements that can be referenced from elsewhere in this nmrML document by using the 'paramGroupRef' element in that location to reference the 'id' attribute value of this element.
  - Multiple: True
  - XML: referenceableParamGroupRef
- __cv_parameter__
  - Type: [CVParameter](#CVParameter)
  - Description: This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here.
  - Multiple: True
  - XML: cvParam
- __cv_parameter_with_unit__
  - Type: [CVParameterWithUnit](#CVParameterWithUnit)
  - Description: This element holds additional data or annotation. Only controlled values are allowed here.
  - Multiple: True
  - XML: cvParamWithUnit
- __cv_term__
  - Type: [CVTerm](#CVTerm)
  - Description: This element holds additional data or annotation as a simple CV term with nofurther values (Parameters) associated with it. Only controlled CV terms values are allowed here.
  - Multiple: True
  - XML: cvTerm
- __user_parameter__
  - Type: [UserParameter](#UserParameter)
  - Description: Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead.
  - Multiple: True
  - XML: userParam


### ReferenceableParameterGroup

A collection of CVParam and UserParam elements that can be referenced from elsewhere in this nmrML document by using the 'paramGroupRef' element in that location to reference the 'id' attribute value of this element.

- __cv_parameter__
  - Type: [CVParameter](#CVParameter)
  - Description: This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here.
  - Multiple: True
  - XML: cvParam
- __user_parameter__
  - Type: [UserParameter](#UserParameter)
  - Description: Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead.
  - Multiple: True
  - XML: userParam
- __id*__
  - Type: xsID
  - Description: The identifier with which to reference this ReferenceableParamGroup.
  - XML: @id


### ReferenceableParameterGroupReference

A collection of CVParam and UserParam elements that can be referenced from elsewhere in this nmrML document by using the 'paramGroupRef' element in that location to reference the 'id' attribute value of this element.

- __cv_parameter__
  - Type: [CVParameter](#CVParameter)
  - Description: This element holds additional data or annotation. In contrast to CVTermType, here a pair of CV term plus a value (=Parameter) is captured. Only controlled values are allowed here.
  - Multiple: True
  - XML: cvParam
- __user_parameter__
  - Type: [UserParameter](#UserParameter)
  - Description: Uncontrolled user parameters (essentially allowing free text). Before using these, one should verify whether there is an appropriate CV term available, and if so, use the CV term instead.
  - Multiple: True
  - XML: userParam
- __id*__
  - Type: xsID
  - Description: The identifier with which to reference this ReferenceableParamGroup.
  - XML: id


### ReferenceableParameterGroupList

Container for a list of referenceableParamGroups.

- __referenceable_parameter_group__
  - Type: [ReferenceableParameterGroup](#ReferenceableParameterGroup)
  - Description: A collection of CVParam and UserParam elements that can be referenced from elsewhere in this nmrML document by using the 'paramGroupRef' element in that location to reference the 'id' attribute value of this element.
  - Multiple: True
  - XML: referenceableParamGroup


### SourceFileList

List and descriptions of the source files this nmrML document was generated or derived from.

- __source_file*__
  - Type: [SourceFile](#SourceFile)
  - Description: Description of the source file, including location and type. The SourceFileType element is intended to be a generic element that points to a file that was used to produce the spectrum or the nmrML file. It could point to an FID file, a procpar file, a pulse program file etc. nmrExperimentSourceFile could be a good name but I personally think that SourceFile is an intuitive name already.
  - Multiple: True
  - XML: sourceFile


### SampleList

List and descriptions of samples.

- __sample__
  - Type: Sample
  - Description: none given
  - Multiple: True
  - XML: sample


### FieldFrequencyLock

no documentation given

- __field_frequency_lock_name*__
  - Type: string
  - Description: none given
  - XML: @fieldFrequencyLockName


### ConcentrationStandard

no documentation given

- __type__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: type
- __concentration_in_sample__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: This element holds a value that also has a unit. Only controlled values are allowed for the unit.
  - XML: concentrationInSample
- __name__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: name


### Sample

no documentation given

- __original_biological_sample_ph__
  - Type: float
  - Description: none given
  - XML: originalBiologicalSamplepH
- __post_buffer_ph__
  - Type: float
  - Description: none given
  - XML: postBufferpH
- __buffer__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: buffer
- __field_frequency_lock*__
  - Type: [FieldFrequencyLock](#FieldFrequencyLock)
  - Description: none given
  - XML: fieldFrequencyLock
- __chemical_shift_standard*__
  - Type: [CVParameter](#CVParameter)
  - Description: none given
  - XML: chemicalShiftStandard
- __solvent_type__
  - Type: [CVParameterWithUnit](#CVParameterWithUnit)
  - Description: none given
  - Multiple: True
  - XML: solventType
- __additional_solute_list__
  - Type: [AdditionalSoluteList](#AdditionalSoluteList)
  - Description: none given
  - XML: additionalSoluteList
- __concentration_standard__
  - Type: [ConcentrationStandard](#ConcentrationStandard)
  - Description: none given
  - XML: concentrationStandard
- __original_biological_sample_reference*__
  - Type: xsAnyURI
  - Description: none given
  - XML: @originalBiologicalSampleReference


### SoftwareList

List and descriptions of software used to acquire and/or process the data in this nmrML file.

- __software__
  - Type: [Software](#Software)
  - Description: A software program used during the acquisition of the spectra or processing of the FID.
  - Multiple: True
  - XML: software


### Software(CVTerm)

Software information.

- __id*__
  - Type: xsID
  - Description: An identifier for this software that is unique across all SoftwareTypes.
  - XML: @id
- __version__
  - Type: string
  - Description: The software version.
  - XML: @version


### SoftwareReference

Reference to a previously defined software element.

- __reference*__
  - Type: xsIDREF
  - Description: This attribute must be used to reference the 'id' attribute of a software element.
  - XML: @ref


### SoftwareReferenceList

no documentation given

- __software_reference__
  - Type: [SoftwareReference](#SoftwareReference)
  - Description: Reference to a previously defined sourceFile.
  - Multiple: True
  - XML: softwareRef


### SourceFile(ParameterGroup)

Description of the source file, including location and type. The SourceFileType element is intended to be a generic element that points to a file that was used to produce the spectrum or the nmrML file. It could point to an FID file, a procpar file, a pulse program file etc. nmrExperimentSourceFile could be a good name but I personally think that SourceFile is an intuitive name already.

- __id*__
  - Type: xsID
  - Description: An identifier for this file.
  - XML: @id
- __name*__
  - Type: string
  - Description: Name of the source file, without reference to location (either URI or local path).
  - XML: @name
- __location*__
  - Type: xsAnyURI
  - Description: URI-formatted location where the file was retrieved.
  - XML: @location
- __sha1__
  - Type: string
  - Description: sha1 of the file.
  - XML: @sha1


### SourceFileReference

no documentation given

- __reference*__
  - Type: xsIDREF
  - Description: This attribute must reference the 'id' of the appropriate sourceFile.
  - XML: @ref


### InstrumentConfiguration(ParameterGroup)

Description of a particular hardware configuration of a NMR spectrometer. For software configuration, use a ReferenceableParamGroup element.

- __software_reference__
  - Type: [SoftwareReference](#SoftwareReference)
  - Description: Reference to a previously defined software element.
  - Multiple: True
  - XML: softwareRef
- __id*__
  - Type: xsID
  - Description: An identifier for this instrument configuration.
  - XML: @id


### InstrumentConfigurationList

List and descriptions of instrument configurations. At least one instrument configuration must be specified, even if it is only to specify that the instrument is unknown. In that case, the "instrument model" term is used to indicate the unknown instrument in the instrumentConfiguration.

- __instrument_configuration__
  - Type: [InstrumentConfiguration](#InstrumentConfiguration)
  - Description: Description of a particular hardware configuration of a NMR spectrometer. For software configuration, use a ReferenceableParamGroup element.
  - Multiple: True
  - XML: instrumentConfiguration


### BinaryDataArray(xsBase64Binary)

no documentation given

- __compressed*__
  - Type: bool
  - Description: True if the binary data was compressed with zlib before encoding as base64
  - XML: @compressed
- __encoded_length*__
  - Type: PositiveInt
  - Description: The number of characters in the base64 string. This is useful for skipping over the string in high throughput applications.
  - XML: encodedLength
- __byte_format*__
  - Type: string
  - Description: TODO format as little endian 64 bit pairs of floats, or 32 bit pairs of floats. See online documentation for decoding examples.
  - XML: byteFormat


### AcquisitionDimensionParameterSet

Descriptions of the acquisition parameters set prior to the start of data acquisition specific to each NMR analysis dimension.

- __decoupling_method__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: decouplingMethod
- __acquisition_nucleus*__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: acquisitionNucleus
- __effective_excitation_field*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: Replacing the hardPulse parameter, would be automatically calculated from the pulse width in the procs file. If you say the pulse width you also have to specify the excitation angle so this way is more compact/useful. Should be recorded in Tesla
  - XML: effectiveExcitationField
- __sweep_width*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: Should be in ppm and Hz.
  - XML: sweepWidth
- __pulse_width*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: 90° pulse width, measured in µs
  - XML: pulseWidth
- __irradiation_frequency*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: irradiationFrequency
- __irradiation_frequency_offset*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: irradiationFrequencyOffset
- __decoupling_nucleus__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: decouplingNucleus
- __sampling_strategy*__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: samplingStrategy
- __sampling_time_points__
  - Type: [BinaryDataArray](#BinaryDataArray)
  - Description: The time domain for the samples. Allows for capturing off grid points and non-uniform sampling.
  - XML: samplingTimePoints
- __decoupled*__
  - Type: bool
  - Description: none given
  - XML: @decoupled
- __number_of_data_points*__
  - Type: int
  - Description: none given
  - XML: @numberOfDataPoints


### AcquisitionParameterSet

Base type for the list with the descriptions of the acquisition settings applied prior to the start of data acquisition.

- __contact_reference_list__
  - Type: [ContactReferenceList](#ContactReferenceList)
  - Description: none given
  - XML: contactRefList
- __software_reference__
  - Type: [SoftwareReference](#SoftwareReference)
  - Description: none given
  - XML: softwareRef
- __sample_container*__
  - Type: [CVTerm](#CVTerm)
  - Description: The container used to introduc the sample into the autosampler. Example: tube, flow probe, rotor. Must reference a CV term.
  - XML: sampleContainer
- __sample_acquisition_temperature*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: The temperature of the sample during the acquisition.
  - XML: sampleAcquisitionTemperature
- __solvent_suppression_method__
  - Type: [CVParameter](#CVParameter)
  - Description: This tag captures the instrument inherent solvent (usually water) suppression method used during acquisition.
  - XML: solventSuppressionMethod
- __spinning_rate*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: spinningRate
- __relaxation_delay*__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: relaxationDelay
- __pulse_sequence*__
  - Type: [PulseSequence](#PulseSequence)
  - Description: A description of the pulse sequence using CV params/terms, and reference to the pulse sequence file if the source is available.
  - XML: pulseSequence
- __shaped_pulse_file__
  - Type: [SourceFileReference](#SourceFileReference)
  - Description: A reference to the pulse shape file, from the power section of the Bruker acquisition software. Example: gauss
  - XML: shapedPulseFile
- __group_delay__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: In the case of Bruker spectra a dead time or group delay can be observed in the FID: it starts with very small values and then, after some points (usually between 60-80 points) the normal FID starts. It can be a number with decimal value.
  - XML: groupDelay
- __acquisition_parameter_reference_list__
  - Type: [AcquisitionParameterFileReferenceList](#AcquisitionParameterFileReferenceList)
  - Description: none given
  - XML: acquisitionParameterRefList
- __number_of_steady_state_scans*__
  - Type: int
  - Description: Steady state scans taken in an NMR acquisition without collecting data. Also known as dummy scans. The pulse sequence is the same for a steady state scan, the only difference is that data is not collected. (More info here: http://u-of-o-nmr-facility.blogspot.ca/2010/04/dummy-scans.html)
  - XML: @numberOfSteadyStateScans
- __number_of_scans*__
  - Type: int
  - Description: The number of transients/scans.
  - XML: @numberOfScans


### AcquisitionParameterSet1D(AcquisitionParameterSet)

no documentation given

- __direct_dimension_parameter_set__
  - Type: [AcquisitionDimensionParameterSet](#AcquisitionDimensionParameterSet)
  - Description: none given
  - XML: DirectDimensionParameterSet


### HadamardParameterSet

no documentation given

- __hadamard_frequency__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: Required if and only if the encoding type is Hadamard.
  - Multiple: True
  - XML: hadamardFrequency


### AcquisitionParameterSetMultiD(AcquisitionParameterSet)

no documentation given

- __hadamard_parameter_set__
  - Type: HadamardParameterSet
  - Description: TODO needs to be a list of frequencies, but could allow for other parameters.
  - XML: hadamardParameterSet
- __direct_dimension_parameter_set*__
  - Type: [AcquisitionDimensionParameterSet](#AcquisitionDimensionParameterSet)
  - Description: none given
  - XML: directDimensionParameterSet
- __encoding_scheme*__
  - Type: [CVParameter](#CVParameter)
  - Description: Quadrature detection method.
  - XML: encodingScheme
- __indirect_dimension_parameter_set*__
  - Type: [AcquisitionDimensionParameterSet](#AcquisitionDimensionParameterSet)
  - Description: Required once for each indirect dimension that is measured.
  - Multiple: True
  - XML: indirectDimensionParameterSet


### PulseSequence(ParameterGroup)

A list of references to the source files that define the pulse sequence including pulse shape files, pulse sequence source code, pulse sequence parameter files, etc.


### Acquisition

no documentation given

- __acquisition_1d__
  - Type: [Acquisition1D](#Acquisition1D)
  - Description: 
  - XML: acquisition1D
- __acquisition_multi_d__
  - Type: [AcquisitionMultiD](#AcquisitionMultiD)
  - Description: 
  - XML: acquisitionMultiD


### Acquisition1D

no documentation given

- __acquisition_parameter_set*__
  - Type: [AcquisitionParameterSet1D](#AcquisitionParameterSet1D)
  - Description: Note, steady state scan is also know as dummy scan.
  - XML: acquisitionParameterSet
- __fidData__
  - Type: [BinaryDataArray](#BinaryDataArray)
  - Description: The FID is stored here as a binary blob. Byte ordering is always little endian (Intel style). Computers using a different endian style must convert to/from little endian when writing/reading nmrML. The FID should be converted into a Complex64 array before encoding. The base64 encoded binary data. The byte order is always 'little endian'.
  - XML: fidData
- __id__
  - Type: xsID
  - Description: An ID for the spectrum so that it can be referenced within the file for spectrum annotations.
  - XML @id
- __name__
  - Type: string
  - Description: A (optional) name so that it can be differentiated other than by its rank if multiple spectra are embedded within the file
  - XML: @name


### AcquisitionMultiD

no documentation given

- __acquisition_parameter_set*__
  - Type: [AcquisitionParameterSetMultiD](#AcquisitionParameterSetMultiD)
  - Description: none given
  - XML: acquisitionParameterSet
- __fid_data*__
  - Type: [BinaryDataArray](#BinaryDataArray)
  - Description: The FID is stored here as a binary blob. Byte ordering is always little endian (Intel style). Computers using a different endian style must convert to/from little endian when writing/reading nmrML. The FID should be converted into a Complex64 array before encoding. The base64 encoded binary data. The byte order is always 'little endian'.
  - XML: fidData


### ProcessingParameterFileReference

no documentation given

- __reference*__
  - Type: xsIDREF
  - Description: This attribute must reference the 'id' of the sourceFile node in the sourceFileList.
  - XML: @ref


### ProcessingParameterFileReferenceList

no documentation given

- __processing_parameter_file_reference*__
  - Type: [ProcessingParameterFileReference](#ProcessingParameterFileReference)
  - Description: Reference to a previously defined sourceFile.
  - Multiple: True
  - XML: processingParameterFileRef


### SpectrumList

List and descriptions of spectra.

- __spectrum_1d__
  - Type: [Spectrum1D](#Spectrum1D)
  - Description: none given
  - Multiple: True
  - XML: spectrum1D
- __spectrum_multi_d__
  - Type: [SpectrumMultiD](#SpectrumMultiD)
  - Description: none given
  - Multiple: True
  - XML: spectrumMultiD


### ProcessingParameterSet

Optional information about processing that was used to create the frequency domain spectrum.

- __post_acquisition_solvent_suppression_method__
  - Type: [CVTerm](#CVTerm)
  - Description: The method used for post acquisition solvent suppression.
  - XML: postAcquisitionSolventSuppressionMethod
- __calibration_compound__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: calibrationCompound
- __data_transformation_method__
  - Type: [CVTerm](#CVTerm)
  - Description: The method used for time-based to frequency-based data transformation.
  - XML: dataTransformationMethod


### Spectrum

A spectrum that is the result of processing the acquisition and a description of the process used to create it.

- __processing_software_reference_list__
  - Type: [SoftwareReferenceList](#SoftwareReferenceList)
  - Description: none given
  - XML: processingSoftwareRefList
- __processing_parameter_file_reference_list__
  - Type: [ProcessingParameterFileReferenceList](#ProcessingParameterFileReferenceList)
  - Description: none given
  - XML: processingParameterFileRefList
- __spectrum_data_array*__
  - Type: [BinaryDataArray](#BinaryDataArray)
  - Description: The 1D spectrum is represented as either a set of y-axis values at equal x-axis intervals or a set of (x,y) pairs.
  - XML: spectrumDataArray
- __x_axis*__
  - Type: [AxisWithUnit](#AxisWithUnit)
  - Description: none given
  - XML: xAxis
- __processing_parameter_set__
  - Type: [ProcessingParameterSet](#ProcessingParameterSet)
  - Description: Optional information about processing that was used to create the frequency domain spectrum.
  - XML: processingParameterSet
- __number_of_data_points*__
  - Type: int
  - Description: The number of (x,y) points in the spectrum. This is needed to read the binary data.
  - XML: @numberOfDataPoints
- __id*__
  - Type: xsID
  - Description: An ID for the spectrum so that it can be referenced within the file for spectrum annotations.
  - XML: @id
- __name__
  - Type: string
  - Description: An (optional) name so that it can be differentiated other than by its rank if multiple spectra are embedded within the file.
  - XML: @name


### Spectrum1D(Spectrum)

no documentation given

- __first_dimension_processing_parameter_set__
  - Type:[FirstDimensionProcessingParameterSet](#FirstDimensionProcessingParameterSet)
  - Description: Optional additional information about processing that was used to create the frequency domain spectrum. This information is relevant to the first dimension of data only.
  - XML: firstDimensionProcessingParameterSet


### SpectrumMultiD(Spectrum)

no documentation given

- __first_dimension_processing_parameter_set*__
  - Type: [FirstDimensionProcessingParameterSet](#FirstDimensionProcessingParameterSet)
  - Description: none given
  - XML: firstDimensionProcessingParameterSet
- __higher_dimension_processing_parameter_set*__
  - Type: [HigherDimensionProcessingParameterSet](#HigherDimensionProcessingParameterSet)
  - Description: none given
  - Multiple: True
  - XML: higherDimensionProcessingParameterSet
- __projected_3d_processing_parameter_set__
  - Type: [Projected3DProcessingParameterSet](#Projected3DProcessingParameterSet)
  - Description: none given
  - XML: projected3DProcessingParameterSet


### FirstDimensionProcessingParameterSet

Parameters recorded when raw data set is processed to create a spectra that are specific to a dimension.

- __zero_order_phase_correction__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: zeroOrderPhaseCorrection
- __first_order_phase_correction__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: firstOrderPhaseCorrection
- __calibration_reference_shift__
  - Type: [ValueWithUnit](#ValueWithUnit)
  - Description: none given
  - XML: calibrationReferenceShift
- __spectral_denoising_method__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: spectralDenoisingMethod
- __window_function_method*__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: windowFunctionMethod
- __window_function_parameter*__
  - Type: [CVParameter](#CVParameter)
  - Description: The parameters used in the window function method.
  - Multiple: True
  - XML: windowFunctionParameter
- __baseline_correction_method__
  - Type: [CVTerm](#CVTerm)
  - Description: none given
  - XML: baselineCorrectionMethod


### AxisWithUnit

no documentation given

- __unit_accession__
  - Type: string
  - Description: An optional CV accession number for the unit term associated with the value, if any (e.g., 'UO:0000266' for 'electron volt').
  - XML: @unitAccession
- __unit_name__
  - Type: string
  - Description: An optional CV name for the unit accession number, if any (e.g., 'electron volt' for 'UO:0000266').
  - XML: @unitName
- __unit_cv_reference__
  - Type: xsIDREF
  - Description: If a unit term is referenced, this attribute must refer to the CV 'id' attribute defined in the cvList in this nmrML file.
  - XML: @unitCvRef
- __start_value__
  - Type: any
  - Description: none given
  - XML: @startValue
- __end_value__
  - Type: any
  - Description: none given
  - XML: @endValue


### HigherDimensionProcessingParameterSet(FirstDimensionProcessingParameterSet)

Parameters recorded when raw data set is processed to create a spectra that are specific to the second dimension.


### Projected3DProcessingParameterSet

no documentation given

- __projection_angle__
  - Type: float
  - Description: none given
  - XML: @projectionAngle
- __positive_projection_method__
  - Type: bool
  - Description: none given
  - XML: @positiveProjectionMethod


## XSD-specific elements


### xsAnyURI


### xsBase64Binary


### xsID


### xsIDREF


## Enumerations


#### ElementType

Enum containing the various Element symbols.

```python
H = "H"
HE = "He"
LI = "Li"
BE = "Be"
B = "B"
C = "C"
N = "N"
O = "O"
F = "F"
NE = "Ne"
NA = "Na"
MG = "Mg"
AL = "Al"
SI = "Si"
P = "P"
S = "S"
CL = "Cl"
AR = "Ar"
K = "K"
CA = "Ca"
SC = "Sc"
TI = "Ti"
V = "V"
CR = "Cr"
MN = "Mn"
FE = "Fe"
CO = "Co"
NI = "Ni"
CU = "Cu"
ZN = "Zn"
GA = "Ga"
GE = "Ge"
AS = "As"
SE = "Se"
BR = "Br"
KR = "Kr"
RB = "Rb"
SR = "Sr"
Y = "Y"
CE = "Ce"
PR = "Pr"
ND = "Nd"
PM = "Pm"
SM = "Sm"
EU = "Eu"
GD = "Gd"
TB = "Tb"
DY = "Dy"
HO = "Ho"
ER = "Er"
TM = "Tm"
YB = "Yb"
LU = "Lu"
ZR = "Zr"
NB = "Nb"
MO = "Mo"
TC = "Tc"
RU = "Ru"
RH = "Rh"
PD = "Pd"
AG = "Ag"
CD = "Cd"
IN = "In"
SN = "Sn"
SB = "Sb"
TE = "Te"
I = "I"
XE = "Xe"
CS = "Cs"
BA = "Ba"
LA = "La"
HF = "Hf"
TA = "Ta"
W = "W"
RE = "Re"
OS = "Os"
IR = "Ir"
PT = "Pt"
AU = "Au"
HG = "Hg"
TL = "Tl"
PB = "Pb"
BI = "Bi"
PO = "Po"
AT = "At"
RN = "Rn"
FR = "Fr"
RA = "Ra"
AC = "Ac"
TH = "Th"
PA = "Pa"
U = "U"
NP = "Np"
PU = "Pu"
AM = "Am"
CM = "Cm"
BK = "Bk"
CF = "Cf"
ES = "Es"
FM = "Fm"
MD = "Md"
NO = "No"
LR = "Lr"
RF = "Rf"
DB = "Db"
SG = "Sg"
BH = "Bh"
HS = "Hs"
MT = "Mt"
DS = "Ds"
RG = "Rg"
CN = "Cn"
NH = "Mh"
FL = "Fl"
MC = "Mc"
LV = "Lv"
TS = "Ts"
OG = "Og"
```


#### BondOrder

Enum containing allowed bond orders.

```python
FIRSTORDER = "1"
SECONDORDER = "2"
THIRDORDER = "3"
```

```mermaid
classDiagram
    ChemicalCompound <-- QuantifiedCompound
    ParameterGroup <-- Contact
    CVTerm <-- Software
    ParameterGroup <-- SourceFile
    ParameterGroup <-- InstrumentConfiguration
    BinaryDataArray <-- SamplingTimePoints
    AcquisitionParameterSet <-- AcquisitionParameterSet1D
    AcquisitionParameterSet <-- AcquisitionParameterSetMultiD
    ParameterGroup <-- PulseSequence
    BinaryDataArray <-- FIDData
    BinaryDataArray <-- SpectrumDataArray
    Spectrum <-- Spectrum1D
    Spectrum <-- SpectrumMultiD
    FirstDimensionProcessingParameterSet <-- HigherDimensionProcessingParameterSet
    nmrML *-- SpectrumAnnotationList
    nmrML *-- CVList
    nmrML *-- ContactList
    nmrML *-- FileDescription
    nmrML *-- ReferenceableParameterGroupList
    nmrML *-- SourceFileList
    nmrML *-- SampleList
    nmrML *-- SoftwareList
    nmrML *-- InstrumentConfigurationList
    nmrML *-- Acquisition
    nmrML *-- SpectrumList
    QuantifiedCompound *-- ClusterList
    QuantifiedCompound *-- PeakList
    QuantifiedCompound *-- ValueWithUnit
    ClusterList *-- Cluster
    Cluster *-- PeakList
    ChemicalCompound *-- CompoundStructure
    ChemicalCompound *-- CompoundIdentifierList
    CompoundStructure *-- AtomList
    CompoundStructure *-- BondList
    AtomList *-- Atom
    Atom *-- ElementType
    BondList *-- Bond
    Bond *-- BondOrder
    AtomAssignmentList *-- Multiplet
    Multiplet *-- AtomReferences
    Multiplet *-- PeakList
    Multiplet *-- CVTerm
    AtomReferences *-- Atom
    PeakList *-- Peak
    AtomAssignmentAnnotation *-- ChemicalCompound
    AtomAssignmentAnnotation *-- AtomAssignmentList
    AtomAssignmentAnnotation *-- Spectrum
    CompoundIdentifierList *-- CompoundDatabaseIdentifier
    CompoundIdentifierList *-- CVTerm
    QuantificationAnnotation *-- QuantifiedCompoundList
    QuantificationAnnotation *-- CVTerm
    QuantificationAnnotation *-- Spectrum
    QuantifiedCompoundList *-- QuantifiedCompound
    SpectrumAnnotationList *-- AtomAssignmentAnnotation
    SpectrumAnnotationList *-- QuantificationAnnotation
    CVList *-- CV
    ContactList *-- Contact
    ContactReference *-- Contact
    ContactReferenceList *-- ContactReference
    AcquisitionParameterFileReference *-- SourceFile
    AcquisitionParameterFileReferenceList *-- AcquisitionParameterFileReference
    FileDescription *-- ParameterGroup
    CVTerm *-- CV
    CVParameter *-- CV
    CVParameterWithUnit *-- CV
    ValueWithUnit *-- CV
    UserParameter *-- CV
    ParameterGroup *-- CVTerm
    ParameterGroup *-- CVParameter
    ParameterGroup *-- CVParameterWithUnit
    ParameterGroup *-- UserParameter
    ParameterGroup *-- ReferenceableParameterGroupReference
    ReferenceableParameterGroup *-- CVParameter
    ReferenceableParameterGroup *-- UserParameter
    ReferenceableParameterGroupReference *-- ReferenceableParameterGroup
    ReferenceableParameterGroupList *-- ReferenceableParameterGroup
    SourceFileList *-- SourceFile
    SampleList *-- Sample
    ConcentrationStandard *-- CVTerm
    ConcentrationStandard *-- ValueWithUnit
    Sample *-- CVTerm
    Sample *-- CVParameter
    Sample *-- CVParameterWithUnit
    Sample *-- FieldFrequencyLock
    Sample *-- ConcentrationStandard
    Sample *-- AdditionalSoluteList
    SoftwareList *-- Software
    SoftwareReference *-- Software
    SoftwareReferenceList *-- SoftwareReference
    SourceFileReference *-- SourceFile
    SourceFileReferenceList *-- SourceFileReference
    InstrumentConfiguration *-- SoftwareReference
    InstrumentConfigurationList *-- InstrumentConfiguration
    Solute *-- ValueWithUnit
    AdditionalSoluteList *-- Solute
    AcquisitionDimensionParameterSet *-- CVTerm
    AcquisitionDimensionParameterSet *-- ValueWithUnit
    AcquisitionDimensionParameterSet *-- SamplingTimePoints
    AcquisitionParameterSet *-- ContactReferenceList
    AcquisitionParameterSet *-- AcquisitionParameterFileReferenceList
    AcquisitionParameterSet *-- CVTerm
    AcquisitionParameterSet *-- CVParameter
    AcquisitionParameterSet *-- ValueWithUnit
    AcquisitionParameterSet *-- SoftwareReference
    AcquisitionParameterSet *-- SourceFileReference
    AcquisitionParameterSet *-- PulseSequence
    AcquisitionParameterSet1D *-- AcquisitionDimensionParameterSet
    HadamardParameterSet *-- ValueWithUnit
    AcquisitionParameterSetMultiD *-- CVParameter
    AcquisitionParameterSetMultiD *-- AcquisitionDimensionParameterSet
    AcquisitionParameterSetMultiD *-- HadamardParameterSet
    Acquisition *-- Acquisition1D
    Acquisition *-- AcquisitionMultiD
    Acquisition1D *-- AcquisitionParameterSet1D
    Acquisition1D *-- FIDData
    AcquisitionMultiD *-- AcquisitionParameterSetMultiD
    AcquisitionMultiD *-- FIDData
    ProcessingParameterFileReference *-- SourceFile
    ProcessingParameterFileReferenceList *-- ProcessingParameterFileReference
    SpectrumList *-- Spectrum1D
    SpectrumList *-- SpectrumMultiD
    ProcessingParameterSet *-- CVTerm
    Spectrum *-- SoftwareReferenceList
    Spectrum *-- ProcessingParameterFileReferenceList
    Spectrum *-- ProcessingParameterSet
    Spectrum *-- SpectrumDataArray
    Spectrum *-- AxisWithUnit
    Spectrum1D *-- FirstDimensionProcessingParameterSet
    SpectrumMultiD *-- FirstDimensionProcessingParameterSet
    SpectrumMultiD *-- HigherDimensionProcessingParameterSet
    SpectrumMultiD *-- Projected3DProcessingParameterSet
    FirstDimensionProcessingParameterSet *-- CVTerm
    FirstDimensionProcessingParameterSet *-- CVParameter
    FirstDimensionProcessingParameterSet *-- ValueWithUnit
    AxisWithUnit *-- CV
    
    class nmrML {
        +CVList cv_list*
        +FileDescription file_description*
        +ContactList contact_list
        +ReferenceableParameterGroupList referenceable_parameter_group_list
        +SourceFileList source_file_list
        +SoftwareList software_list
        +InstrumentConfigurationList instrument_configuration_list*
        +SampleList sample_list
        +Acquisition acquisition*
        +SpectrumList spectrum_list
        +SpectrumAnnotationList spectrum_annotation_list
        +string version*
        +string accession
        +URL accession_url
    }
    
    class QuantifiedCompound {
        +ValueWithUnit concentration*
        +ClusterList cluster_list
        +PeakList peak_list
    }
    
    class ClusterList {
        +Cluster[0..*] cluster*
    }
    
    class Cluster {
        +PeakList peak_list*
        +float center
        +float shift
    }
    
    class ChemicalCompound {
        +CompoundIdentifierList identifier_list
        +CompoundStructure structure
        +str name
    }
    
    class CompoundStructure {
        +AtomList atom_list*
        +BondList bond_list*
    }
    
    class AtomList {
        +Atom[0..*] atom*
    }
    
    class Atom {
        +ElementType element_type*
        +any x*
        +any y*
    }
    
    class BondList {
        +Bond[0..*] bond*
    }
    
    class Bond {
        +string[0..*] atom_references*
        +BondOrder order*
    }
    
    class AtomAssignmentList {
        +Multiplet[0..*] multiplet*
    }
    
    class Multiplet {
        +AtomReferences atoms*
        +CVTerm multiplicity*
        +PeakList peak_list
        +float center*
    }
    
    class AtomReferences {
        +Atom[0..*] atom_references
    }
    
    class Peak {
        +float _*
        +float amplitude
        +float width
    }
    
    class PeakList {
        +Peak[0..*] peak*
    }
    
    class AtomAssignmentAnnotation {
        +ChemicalCompound chemical_compound*
        +AtomAssignmentList atom_assignment_list
        +Spectrum spectrum_reference*
    }
    
    class InChiString {
    }
    
    class CompoundIdentifierList {
        +CVTerm[0..*] identifier
        +CompoundDatabaseIdentifier[0..*] database_identifier
    }
    
    class CompoundDatabaseIdentifier {
        +string identifier*
        +URL uri*
    }
    
    class QuantificationAnnotation {
        +CVTerm quantification_method*
        +QuantifiedCompoundList quantification_compound_list*
        +Spectrum spectrum_reference*
    }
    
    class QuantifiedCompoundList {
        +QuantifiedCompound[0..*] quantified_compound*
    }
    
    class SpectrumAnnotationList {
        +AtomAssignmentAnnotation atom_assignment
        +QuantificationAnnotation quantification
    }
    
    class CVList {
        +CV cv*
    }
    
    class CV {
        +string full_name*
        +string version
        +URL uri*
    }
    
    class ContactList {
        +Contact[0..*] contact*
    }
    
    class Contact {
        +string full_name*
        +URL url
        +string address
        +string organization
        +string email*
    }
    
    class ContactReference {
        +Contact reference*
    }
    
    class ContactReferenceList {
        +ContactReference[0..*] contact_reference*
    }
    
    class AcquisitionParameterFileReference {
        +SourceFile reference*
    }
    
    class AcquisitionParameterFileReferenceList {
        +AcquisitionParameterFileReference[0..*] acquisition_parameter_file_reference*
    }
    
    class FileDescription {
        +ParameterGroup file_content*
    }
    
    class CVTerm {
        +CV cv_reference*
        +string accession*
        +string name*
    }
    
    class CVParameter {
        +CV cv_reference*
        +string accession*
        +string name*
        +string value
    }
    
    class CVParameterWithUnit {
        +CV cv_reference*
        +string accession*
        +string name*
        +string value
        +CV unit_cv_reference
        +string unit_accession
        +string unit_name
    }
    
    class ValueWithUnit {
        +string value
        +string unit_accession
        +string unit_name
        +CV unit_cv_reference
    }
    
    class UserParameter {
        +string name*
        +string value_type
        +string value
        +string unit_accession
        +string unit_name
        +CV unit_cv_reference
    }
    
    class ParameterGroup {
        +ReferenceableParameterGroupReference[0..*] referenceable_parameter_group_reference
        +CVParameter[0..*] cv_parameter
        +CVParameterWithUnit[0..*] cv_parameter_with_unit
        +CVTerm[0..*] cv_term
        +UserParameter[0..*] user_parameter
    }
    
    class ReferenceableParameterGroup {
        +CVParameter[0..*] cv_parameter
        +UserParameter[0..*] user_parameter
    }
    
    class ReferenceableParameterGroupReference {
        +ReferenceableParameterGroup reference*
    }
    
    class ReferenceableParameterGroupList {
        +ReferenceableParameterGroup[0..*] referenceable_parameter_group*
    }
    
    class SourceFileList {
        +SourceFile[0..*] source_file*
    }
    
    class SampleList {
        +Sample[0..*] sample*
    }
    
    class FieldFrequencyLock {
        +string field_frequency_lock_name*
    }
    
    class ConcentrationStandard {
        +CVTerm type*
        +ValueWithUnit concentration_in_sample*
        +CVTerm name*
    }
    
    class Sample {
        +float original_biological_sample_ph
        +float post_buffer_ph
        +CVTerm buffer
        +FieldFrequencyLock field_frequency_lock*
        +CVParameter chemical_shift_standard*
        +CVParameterWithUnit[0..*] solvent_type
        +AdditionalSoluteList additional_solute_list
        +ConcentrationStandard concentration_standard
        +URL original_biological_sample_reference*
    }
    
    class SoftwareList {
        +Software[0..*] software*
    }
    
    class Software {
        +string version
    }
    
    class SoftwareReference {
        +Software reference*
    }
    
    class SoftwareReferenceList {
        +SoftwareReference[0..*] software_reference
    }
    
    class SourceFile {
        +string name*
        +URL location*
        +string sha1
    }
    
    class SourceFileReference {
        +SourceFile reference*
    }
    
    class SourceFileReferenceList {
        +SourceFileReference[0..*] source_file_reference
    }
    
    class InstrumentConfiguration {
        +SoftwareReference[0..*] software_reference
    }
    
    class InstrumentConfigurationList {
        +InstrumentConfiguration[0..*] instrument_configuration*
    }
    
    class BinaryDataArray {
        +bool compressed*
        +PositiveInt encoded_length*
        +string byte_format*
    }
    
    class Solute {
        +ValueWithUnit concentration_in_sample*
        +string name*
    }
    
    class Temperature {
        +float temperature*
        +string temperature_uni_name*
        +string temperature_unit_id
    }
    
    class AdditionalSoluteList {
        +Solute[0..*] solute
    }
    
    class SamplingTimePoints {
        +string binary_data_array*
    }
    
    class AcquisitionDimensionParameterSet {
        +CVTerm decoupling_method
        +CVTerm acquisition_nucleus*
        +ValueWithUnit effective_excitation_field*
        +ValueWithUnit sweep_width*
        +ValueWithUnit pulse_width*
        +ValueWithUnit irradiation_frequency*
        +ValueWithUnit irradiation_frequency_offset*
        +CVTerm decoupling_nucleus
        +CVTerm sampling_strategy*
        +SamplingTimePoints sampling_time_points
        +bool decoupled*
        +int number_of_data_points*
    }
    
    class AcquisitionParameterSet {
        +ContactReferenceList contact_reference_list
        +SoftwareReference software_reference
        +CVTerm sample_container*
        +ValueWithUnit sample_acquisition_temperature*
        +CVParameter solvent_suppression_method
        +ValueWithUnit spinning_rate*
        +ValueWithUnit relaxation_delay*
        +PulseSequence pulse_sequence*
        +SourceFileReference shaped_pulse_file
        +ValueWithUnit group_delay
        +AcquisitionParameterFileReferenceList acquisition_parameter_reference_list
        +int number_of_steady_state_scans*
        +int number_of_scans*
    }
    
    class AcquisitionParameterSet1D {
        +AcquisitionDimensionParameterSet direct_dimension_parameter_set
    }
    
    class HadamardParameterSet {
        +ValueWithUnit[0..*] hadamard_frequency
    }
    
    class AcquisitionParameterSetMultiD {
        +HadamardParameterSet hadamard_parameter_set
        +AcquisitionDimensionParameterSet direct_dimension_parameter_set*
        +CVParameter encoding_scheme*
        +AcquisitionDimensionParameterSet[0..*] indirect_dimension_parameter_set*
    }
    
    class PulseSequence {
    }
    
    class Acquisition {
        +Acquisition1D, AcquisitionMultiD acquisition*
    }
    
    class FIDData {
        +string binary_data_array*
    }
    
    class Acquisition1D {
        +AcquisitionParameterSet1D acquisition_parameter_set*
        +FIDData fidData
        +string name
    }
    
    class AcquisitionMultiD {
        +AcquisitionParameterSetMultiD acquisition_parameter_set*
        +FIDData fid_data*
    }
    
    class ProcessingParameterFileReference {
        +SourceFile reference*
    }
    
    class ProcessingParameterFileReferenceList {
        +ProcessingParameterFileReference[0..*] processing_parameter_file_reference*
    }
    
    class SpectrumList {
        +Spectrum1D, SpectrumMultiD[0..*] spectrum*
    }
    
    class ProcessingParameterSet {
        +CVTerm post_acquisition_solvent_suppression_method
        +CVTerm calibration_compound
        +CVTerm data_transformation_method
    }
    
    class SpectrumDataArray {
        +string binary_data_array*
    }
    
    class Spectrum {
        +SoftwareReferenceList processing_software_reference_list
        +ProcessingParameterFileReferenceList processing_parameter_file_reference_list
        +SpectrumDataArray spectrum_data_array*
        +AxisWithUnit x_axis*
        +ProcessingParameterSet processing_parameter_set
        +int number_of_data_points*
        +string name
    }
    
    class Spectrum1D {
        +FirstDimensionProcessingParameterSet first_dimension_processing_parameter_set
    }
    
    class SpectrumMultiD {
        +FirstDimensionProcessingParameterSet first_dimension_processing_parameter_set*
        +HigherDimensionProcessingParameterSet[0..*] higher_dimension_processing_parameter_set*
        +Projected3DProcessingParameterSet projected_3d_processing_parameter_set
    }
    
    class FirstDimensionProcessingParameterSet {
        +ValueWithUnit zero_order_phase_correction
        +ValueWithUnit first_order_phase_correction
        +ValueWithUnit calibration_reference_shift
        +CVTerm spectral_denoising_method
        +CVTerm window_function_method*
        +CVParameter[0..*] window_function_parameter*
        +CVTerm baseline_correction_method
    }
    
    class AxisWithUnit {
        +string unit_accession
        +string unit_name
        +CV unit_cv_reference
        +any start_value
        +any end_value
    }
    
    class HigherDimensionProcessingParameterSet {
    }
    
    class Projected3DProcessingParameterSet {
        +float projection_angle
        +bool positive_projection_method
    }
    
    class ElementType {
        << Enumeration >>
        +H
        +HE
        +LI
        +BE
        +B
        +C
        +N
        +O
        +F
        +NE
        +NA
        +MG
        +AL
        +SI
        +P
        +S
        +CL
        +AR
        +K
        +CA
        +SC
        +TI
        +V
        +CR
        +MN
        +FE
        +CO
        +NI
        +CU
        +ZN
        +GA
        +GE
        +AS
        +SE
        +BR
        +KR
        +RB
        +SR
        +Y
        +CE
        +PR
        +ND
        +PM
        +SM
        +EU
        +GD
        +TB
        +DY
        +HO
        +ER
        +TM
        +YB
        +LU
        +ZR
        +NB
        +MO
        +TC
        +RU
        +RH
        +PD
        +AG
        +CD
        +IN
        +SN
        +SB
        +TE
        +I
        +XE
        +CS
        +BA
        +LA
        +HF
        +TA
        +W
        +RE
        +OS
        +IR
        +PT
        +AU
        +HG
        +TL
        +PB
        +BI
        +PO
        +AT
        +RN
        +FR
        +RA
        +AC
        +TH
        +PA
        +U
        +NP
        +PU
        +AM
        +CM
        +BK
        +CF
        +ES
        +FM
        +MD
        +NO
        +LR
        +RF
        +DB
        +SG
        +BH
        +HS
        +MT
        +DS
        +RG
        +CN
        +NH
        +FL
        +MC
        +LV
        +TS
        +OG
    }
    
    class BondOrder {
        << Enumeration >>
        +FIRSTORDER
        +SECONDORDER
        +THIRDORDER
    }
    
```
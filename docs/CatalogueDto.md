# CatalogueDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier. | 
**gaeb_xml_id** | **str** | This is used to store the GAEB XML Id within this Catalogue. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization. | [optional] 
**name** | **str** | The name that is given for this catalogue. | [optional] 
**description** | **str** | Additional information about this catalogue. | [optional] 
**catalogue_type** | [**CatalogueTypeDto**](CatalogueTypeDto.md) | If given, this gives a classification for the contents of the catalogue | 
**catalogue_type_detail** | **str** | This property may hold additional information about the catalogue type. It is currently only used in GAEB XML exchange to carry detailed information about a catalogue type, but it&#39;s otherwise just a free text field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



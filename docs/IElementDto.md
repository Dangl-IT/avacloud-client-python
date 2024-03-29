# IElementDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier. | 
**gaeb_xml_id** | **str** | This is used to store the GAEB XML Id within this IElement. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization. | [optional] 
**addendum_number** | **str** | This optional string property is shared by all IElements, and indicates if the element is part of an addendum, a &#39;Nachtrag&#39; in German. | [optional] 
**project_catalogues** | [**list[CatalogueDto]**](CatalogueDto.md) |  | [optional] 
**catalogue_references** | [**list[CatalogueReferenceDto]**](CatalogueReferenceDto.md) |  | [optional] 
**element_type_discriminator** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



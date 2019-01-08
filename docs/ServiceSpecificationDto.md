# ServiceSpecificationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_hourly_wage** | **float** |  | 
**project_tax_rate** | **float** |  | 
**project_price_components** | **list[str]** |  | [optional] 
**project_item_number_schema** | [**ItemNumberSchemaDto**](ItemNumberSchemaDto.md) |  | [optional] 
**elements** | [**list[IElementDto]**](IElementDto.md) |  | [optional] 
**project_labour_time_label** | **str** |  | [optional] 
**contains_duplicate_item_numbers** | **bool** |  | 
**ignore_duplicate_item_numbers** | **bool** |  | 
**total_price_gross_by_tax_rate** | [**list[GrossPriceComponentDto]**](GrossPriceComponentDto.md) |  | [optional] 
**ignore_child_price_updates** | **bool** |  | 
**deducted_price** | **float** |  | 
**deduction_factor** | **float** |  | 
**total_price** | **float** |  | 
**total_price_gross** | **float** |  | 
**total_price_gross_deducted** | **float** |  | 
**price_type** | [**PriceTypeDto**](PriceTypeDto.md) |  | 
**bidder** | [**PartyInformationDto**](PartyInformationDto.md) |  | [optional] 
**gaeb_xml_id** | **str** |  | [optional] 
**project_information** | **object** |  | [optional] 
**exchange_phase** | [**ExchangePhaseDto**](ExchangePhaseDto.md) |  | 
**origin** | [**OriginDto**](OriginDto.md) |  | 
**creation_date** | **datetime** |  | 
**offer_by_date** | **datetime** |  | 
**decision_date** | **datetime** |  | 
**submission_location** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**price_information** | [**PriceInformationDto**](PriceInformationDto.md) |  | [optional] 
**project_catalogues** | [**list[CatalogueDto]**](CatalogueDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceSpecificationGroupDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**short_text** | **str** |  | [optional] 
**comission_status** | [**ComissionStatusDto**](ComissionStatusDto.md) |  | 
**item_number** | [**ItemNumberDto**](ItemNumberDto.md) |  | [optional] 
**element_type** | **str** |  | [optional] 
**is_lot** | **bool** |  | 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



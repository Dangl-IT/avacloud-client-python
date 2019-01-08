# PositionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_price** | **float** |  | 
**quantity** | **float** |  | 
**unit_tag** | **str** |  | [optional] 
**labour_components** | [**LabourPriceComponentDto**](LabourPriceComponentDto.md) |  | [optional] 
**price_components** | [**list[PriceComponentDto]**](PriceComponentDto.md) |  | [optional] 
**quantity_components** | [**list[CalculationDto]**](CalculationDto.md) |  | [optional] 
**sub_descriptions** | [**list[SubDescriptionDto]**](SubDescriptionDto.md) |  | [optional] 
**comission_status** | [**ComissionStatusDto**](ComissionStatusDto.md) |  | 
**complemented_by** | **list[str]** |  | [optional] 
**complemented** | **bool** |  | 
**amount_to_be_entered_by_bidder** | **bool** |  | 
**price_composition_required** | **bool** |  | 
**use_different_tax_rate** | **bool** |  | 
**tax_rate** | **float** |  | 
**item_number** | [**ItemNumberDto**](ItemNumberDto.md) |  | [optional] 
**deduction_factor** | **float** |  | 
**total_price** | **float** |  | 
**total_price_gross** | **float** |  | 
**total_price_gross_deducted** | **float** |  | 
**deducted_price** | **float** |  | 
**position_type** | [**PositionTypeDto**](PositionTypeDto.md) |  | 
**price_type** | [**PriceTypeDto**](PriceTypeDto.md) |  | 
**service_type** | [**ServiceTypeDto**](ServiceTypeDto.md) |  | 
**short_text** | **str** |  | [optional] 
**long_text** | **str** |  | [optional] 
**html_long_text** | **str** |  | [optional] 
**addition_type** | [**AdditionTypeDto**](AdditionTypeDto.md) |  | 
**element_type** | **str** |  | [optional] 
**quantity_assignments** | [**list[QuantityAssignmentDto]**](QuantityAssignmentDto.md) |  | [optional] 
**commerce_properties** | [**CommercePropertiesDto**](CommercePropertiesDto.md) |  | [optional] 
**alternative_to** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



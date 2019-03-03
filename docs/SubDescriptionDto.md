# SubDescriptionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier.              | 
**quantity** | **float** | Returns the total calculated sum of all quantity assignments. Will return the result rounded to three decimal places.              | 
**quantity_components** | [**list[CalculationDto]**](CalculationDto.md) | Holds quantity information for this sub description. Quantity is listening to changes here and is reporting the total sum of all quantity components.              | [optional] 
**amount_to_be_entered_by_bidder** | **bool** | Indicates if the bidder is asked to specify an amount.              | 
**identifier** | **str** | Identifier for this SubDescription.              | [optional] 
**short_text** | **str** | Short description for this DescriptionBase element.              | [optional] 
**long_text** | **str** | Detailed description for this DescriptionBase element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText.              | [optional] 
**html_long_text** | **str** | This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out.              | [optional] 
**addition_type** | **object** | Indicates if this DescriptionBase element contains Buyer or Bidder additions to the text.              | 
**standardized_description** | **object** | This represents a standardized description. This means that instead of solely relying on texts to describe a service, external standards and definitions are referenced for a common understanding. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



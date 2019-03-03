# ProjectInformationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | **object** | Information about the buyer.              | [optional] 
**description** | **str** | Description for the project.              | [optional] 
**description_short** | **str** | Short description for the project.              | [optional] 
**name** | **str** | Name of the project.              | [optional] 
**site** | **object** | Information about the site.              | [optional] 
**item_number_schema** | **object** | The ItemNumberSchema used in the project.              | [optional] 
**currency_short** | **str** | Short label for the currency used.              | [optional] 
**currency_long** | **str** | Full label of the currency used.              | [optional] 
**labour_time_label** | **str** | Label for the labour time part of prices used in the project.              | [optional] 
**price_components** | **list[str]** | Labels for the price components used in the project. Caution: Removal of a price component will trigger to have dependent price informations be deleted in IElements that use this property.              | [optional] 
**bidder_comment_allowed** | **bool** | This bool indicates if this project allows the bidder to add bidder comments. Bidder comments are a way to attach clarifying information when submitting an offer. | 
**side_offers_allowed** | **bool** | This property indicates if the project should allow side offers from contractors. In GAEB, a side offer would typically be in exchange phase 85. | 
**award_type** | **object** | This enumeration describes the type of the award / procurement process. If this is used in a GAEB context, more information about award types can be found in the German VOB/A rules and the GAEB standard | 
**special_award_kind** | **object** | This enumeration describes awards for project that are not just a regular procurement. For example, it can be used to describe recurring maintenance or an outline contract (German: Rahmenvertrag) which just specifies services and prices but may be requested on demand when necessary | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



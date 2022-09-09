# ServiceSpecificationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier. | 
**project_hourly_wage** | **float** | The hourly wage that is used within this ElementContainerBase. Will be propagated to child elements. | 
**project_tax_rate** | **float** | The tax rate that is used within this ElementContainerBase. Will be propagated to child elements. | 
**project_price_components** | **list[str]** | The price components that are used within this project. They are ignored during Json deserialization because they will be set from the parent project. | [optional] 
**project_item_number_schema** | [**ItemNumberSchemaDto**](ItemNumberSchemaDto.md) | The ItemNumberSchema that is used within this project. | [optional] 
**elements** | [**list[IElementDto]**](IElementDto.md) | The IElements within this ElementContainerBase. | [optional] 
**project_labour_time_label** | **str** | The label used in the parent Project to mark labour time, e.g. \&quot;Hours\&quot; or \&quot;Stunden\&quot;. | [optional] 
**contains_duplicate_item_numbers** | **bool** | Indicates if there are child IElements that have conflicting, duplicated ItemNumbers or if any child ElementContainerBase elements themselves contain duplicate ItemNumber s. Will always indicate false when told to ignore duplicate item numbers. | 
**contains_duplicate_element_ids** | **bool** | Indicates if there are child IElements that have conflicting, duplicated Ids or if any child ElementContainerBase elements themselves contain duplicate Id s. Will always indicate false when told to ignore duplicate item numbers. | 
**ignore_duplicate_item_numbers** | **bool** | Indicate if duplicated ItemNumbers within child elements are to be ignored. Will not perform checks for duplicates if yes. | 
**ignore_duplicate_element_ids** | **bool** | Indicate if duplicated Ids within child elements are to be ignored. Will not perform checks for duplicates if yes. | 
**total_price_gross_by_tax_rate** | [**list[GrossPriceComponentDto]**](GrossPriceComponentDto.md) | Price composition by tax rate. | [optional] 
**ignore_child_price_updates** | **bool** | Internally used to indicate that a propagation is currently done, this is done to not recalculate every single result from a lot of changes when it is sufficient to calculate the total price at once. | 
**deducted_price** | **float** | Net price after applied deductions. | 
**deduction_factor** | **float** | Factor of applied deductions to the total price. For example, \&quot;0.03\&quot; means that a 3% deduction is to be applied. | 
**absolute_deduction** | **float** | The exact amount of the discount as an absolute value. For backwards compatibility reasons, setting this value will also set a calculated value to DeductionFactor, which will also be updated in case the total price is changed to reflect a relative value of the absolute discount sum. | [optional] 
**total_price** | **float** | Will return this ElementContainerBase&#39;s total price. | 
**total_price_gross** | **float** | The total gross price for this ElementContainerBase including all child elements. | 
**total_price_gross_deducted** | **float** | Total gross price after applied deductions. | 
**price_type** | [**PriceTypeDto**](PriceTypeDto.md) | Indicates the PriceType of this ElementContainerBase, whether it should factor into total costs or not. | 
**bidder** | [**PartyInformationDto**](PartyInformationDto.md) | Information about the bidder. | [optional] 
**bidder_discriminator** | **str** | This discriminator is used to identify different bidders in a project. It is different from the Identifier property in the Bidder in that the BidderDiscriminator is intended to be a numerical identifier within a project, while the Identifier does uniquely identify a bidder in the system independent of a specific project. This property should map to \&quot;Bieternummer\&quot; or \&quot;BidderNo\&quot; in GAEB. | [optional] 
**gaeb_xml_id** | **str** | This is used to store the GAEB XML Id within this ServiceSpecification. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization. | [optional] 
**project_information** | [**ProjectInformationDto**](ProjectInformationDto.md) | The ProjectInformation used within the Project in which this ElementContainerBase is contained. This is reference equal to the ProjectInformation used in the parent project. | [optional] 
**exchange_phase** | [**ExchangePhaseDto**](ExchangePhaseDto.md) | This service specifications exchange phase, i.e. the current status in the project it is intended to be used (such as request for offer, offer, awarding...). | 
**origin** | [**OriginDto**](OriginDto.md) | This indicates where the service specification originates, i.e. from an exchange file format or self created. If applicable, additional information is present in the OriginDetail property. | 
**origin_detail** | **str** | This property complements the Origin property. Some formats, e.g. GaebXml might have additional information attached, e.g. GAEB XML V3.2 oder GAEB XML V3.1. This string property is used to hold such data. The Dangl.AVA module does not have a list of possible values, since this is defined in the native format assemblies, e.g. Dangl.GAEB or Dangl.Oenorm. | [optional] 
**creation_date** | **datetime** | Creation date of this ServiceSpecification. | [optional] 
**offer_by_date** | **datetime** | Date indicating until when an offer has to be submitted. In German, this is often called the \&quot;Eröffnungstermin\&quot; | [optional] 
**decision_date** | **datetime** | Date indicating by when the buyer will select a contractor. | [optional] 
**submission_location** | **str** | String indicating where the physical submission of the offer is taking place. | [optional] 
**description** | **str** | Description of this ServiceSpecification. | [optional] 
**name** | **str** | The name of this ServiceSpecification. | [optional] 
**price_information** | [**PriceInformationDto**](PriceInformationDto.md) | This PriceInformation contains global data for the ServiceSpecification. When inside a Project, do not set this property manually. | [optional] 
**project_catalogues** | [**list[CatalogueDto]**](CatalogueDto.md) | These are Catalogue that are used within this ElementContainerBase. Catalogue references are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. | [optional] 
**catalogue_references** | [**list[CatalogueReferenceDto]**](CatalogueReferenceDto.md) | Referenced catalogues for this ElementContainerBase. | [optional] 
**planned_execution_start** | **datetime** | The date when the execution of the services is scheduled to start | [optional] 
**planned_execution_end** | **datetime** | The date then the execution of the services is scheduled to be finished | [optional] 
**contract_date** | **datetime** | The date on which the contract has been awarded. This matches \&quot;Auftragsdatum\&quot; in GAEB | [optional] 
**contract_identifier** | **str** | This value can be used to indicate the number or identifier of the contract. It matches \&quot;Auftragsnummer\&quot; in GAEB | [optional] 
**warranty_duration** | [**WarrantyDurationDto**](WarrantyDurationDto.md) | This indicates how long the warranty period is for this ServiceSpecification | [optional] 
**warranty_end** | **datetime** | The date on which the warranty period ends | [optional] 
**approval_date** | **datetime** | The date on which the services rendered by the bidder are scheduled to be approved by the buyer | [optional] 
**type_of_approval** | **str** | This should specify how the approval is performed by the buyer. This matches \&quot;AcceptType\&quot; in GAEB | [optional] 
**addendum_number** | **str** | This optional string property is shared by all IElements, and indicates if the element is part of an addendum, a &#39;Nachtrag&#39; in German. | [optional] 
**addendum_status** | [**AddendumStatusDto**](AddendumStatusDto.md) | This indicates, if this element is part of an addendum an, if yes, with what status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PartyInformationDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Elements GUID identifier. | 
**name** | **str** | This party&#39;s name. | [optional] 
**street** | **str** | This party&#39;s street. | [optional] 
**zip_code** | **str** | This party&#39;s ZipCode. | [optional] 
**city** | **str** | This party&#39;s City. | [optional] 
**country** | **str** | This party&#39;s Country. | [optional] 
**identifier** | **str** | This party&#39;s Identifier. | [optional] 
**remarks** | **str** | Remarks for this party. | [optional] 
**email** | **str** | An email address for this party. | [optional] 
**phone** | **str** | A phone number for this party. | [optional] 
**contact_person_name** | **str** | The name of a contact person. | [optional] 
**award_identifier** | **str** | This is an identifier related to this PartyInformation and their internal reference of the tender (or award). This might be used to assign an identifier (German \&quot;Vergabenummer\&quot;) for the current project. This is typically only used in Buyer and Bidder representations and should map to the concept of \&quot;Vergabenummer\&quot; or \&quot;AwardNo\&quot; in GAEB. | [optional] 
**is_in_european_economic_area** | **bool** | This property indicates if the party is registered within the European Economic Area. | 
**vat_id** | **str** | If this is within the European Economic Area (see IsInEuropeanEconomicArea, then as a business entity it likely has an EU VAT Id. | [optional] 
**fax** | **str** | The fax number for this party. | [optional] 
**country_code** | **str** | The two letter ISO country code, e.g. DE for Germany. | [optional] 
**creditor_or_debtor_identifier** | **str** | Depending on which party this class represents, it might have either a &#39;creditor&#39; or &#39;debtor&#39; number. This is often used in internal accounting systems. | [optional] 
**global_location_number** | **str** | The Global Location Number (GLN) is issued by GS1 and is intended to be a unique identifier for the physical address of a party, e.g. a business office. | [optional] 
**banking_information** | [**list[BankingInformationDto]**](BankingInformationDto.md) | This list contains information about bank accounts associated with this PartyInformation. It&#39;s typically used for buyers and bidders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**invoice_type** | [**InvoiceType**](InvoiceType.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**payment_due_date** | **datetime** |  | [optional] 
**references** | [**References**](References.md) |  | [optional] 
**payment_terms** | **str** |  | [optional] 
**previous_invoices** | [**list[PreviousInvoice]**](PreviousInvoice.md) |  | [optional] 
**buyer** | [**Organization**](Organization.md) |  | [optional] 
**seller** | [**Organization**](Organization.md) |  | [optional] 
**payee** | [**Payee**](Payee.md) |  | [optional] 
**invoice_notes** | [**list[InvoiceNote]**](InvoiceNote.md) |  | [optional] 
**invoice_period** | [**InvoicePeriod**](InvoicePeriod.md) |  | [optional] 
**totals** | [**InvoiceTotals**](InvoiceTotals.md) |  | [optional] 
**payment_instructions** | [**PaymentInstructions**](PaymentInstructions.md) |  | [optional] 
**documents** | [**list[SupportingDocument]**](SupportingDocument.md) |  | [optional] 
**vat_breakdown** | [**list[VatBreakdown]**](VatBreakdown.md) |  | [optional] 
**allowances** | [**list[InvoiceAllowance]**](InvoiceAllowance.md) |  | [optional] 
**charges** | [**list[InvoiceCharge]**](InvoiceCharge.md) |  | [optional] 
**line_items** | [**list[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] 
**source_type** | [**SourceType**](SourceType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



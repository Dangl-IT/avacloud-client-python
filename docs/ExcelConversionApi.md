# avacloud_client_python.ExcelConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**excel_conversion_convert_to_ava**](ExcelConversionApi.md#excel_conversion_convert_to_ava) | **POST** /conversion/excel/ava | Converts Excel files to Dangl.AVA projects.
[**excel_conversion_convert_to_excel**](ExcelConversionApi.md#excel_conversion_convert_to_excel) | **POST** /conversion/excel/excel | Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.
[**excel_conversion_convert_to_flat_ava**](ExcelConversionApi.md#excel_conversion_convert_to_flat_ava) | **POST** /conversion/excel/flat-ava | Converts Excel files to Dangl.AVA projects.
[**excel_conversion_convert_to_gaeb**](ExcelConversionApi.md#excel_conversion_convert_to_gaeb) | **POST** /conversion/excel/gaeb | Converts Excel files to GAEB files.
[**excel_conversion_convert_to_oenorm**](ExcelConversionApi.md#excel_conversion_convert_to_oenorm) | **POST** /conversion/excel/oenorm | Converts Excel files to Oenorm files.


# **excel_conversion_convert_to_ava**
> ProjectDto excel_conversion_convert_to_ava(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)

Converts Excel files to Dangl.AVA projects.

### Example
```python
from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avacloud_client_python.ExcelConversionApi(avacloud_client_python.ApiClient(configuration))
excel_file = '/path/to/file.txt' # file | The input file (optional)
read_new_elements = true # bool | Defaults to false (optional)
rebuild_item_number_schema = true # bool | When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. (optional)
remove_plain_text_long_texts = true # bool | If set to true, plain text long texts will be removed from the output to reduce response sizes (optional)
remove_html_long_texts = true # bool | If set to true, html long texts will be removed from the output to reduce response sizes (optional)

try:
    # Converts Excel files to Dangl.AVA projects.
    api_response = api_instance.excel_conversion_convert_to_ava(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelConversionApi->excel_conversion_convert_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_file** | **file**| The input file | [optional] 
 **read_new_elements** | **bool**| Defaults to false | [optional] 
 **rebuild_item_number_schema** | **bool**| When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. | [optional] 
 **remove_plain_text_long_texts** | **bool**| If set to true, plain text long texts will be removed from the output to reduce response sizes | [optional] 
 **remove_html_long_texts** | **bool**| If set to true, html long texts will be removed from the output to reduce response sizes | [optional] 

### Return type

[**ProjectDto**](ProjectDto.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.com.dangl-it.ProjectDto.v1+json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_excel**
> file excel_conversion_convert_to_excel(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, include_article_numbers=include_article_numbers)

Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.

### Example
```python
from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avacloud_client_python.ExcelConversionApi(avacloud_client_python.ApiClient(configuration))
excel_file = '/path/to/file.txt' # file | The input file (optional)
read_new_elements = true # bool | Defaults to false (optional)
rebuild_item_number_schema = true # bool | When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. (optional)
write_prices = true # bool | Defaults to true (optional)
write_long_texts = true # bool | Defaults to true (optional)
conversion_culture = 'conversion_culture_example' # str | The culture that should be used for the conversion process, to have localized Excel files (optional)
include_article_numbers = true # bool | If this is enabled, then a new column will be created in the overview worksheet that contains the article numbers for positions. Article numbers will be read from 'position.commerceProperties.articleNumber' (optional)

try:
    # Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.
    api_response = api_instance.excel_conversion_convert_to_excel(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, include_article_numbers=include_article_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelConversionApi->excel_conversion_convert_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_file** | **file**| The input file | [optional] 
 **read_new_elements** | **bool**| Defaults to false | [optional] 
 **rebuild_item_number_schema** | **bool**| When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. | [optional] 
 **write_prices** | **bool**| Defaults to true | [optional] 
 **write_long_texts** | **bool**| Defaults to true | [optional] 
 **conversion_culture** | **str**| The culture that should be used for the conversion process, to have localized Excel files | [optional] 
 **include_article_numbers** | **bool**| If this is enabled, then a new column will be created in the overview worksheet that contains the article numbers for positions. Article numbers will be read from &#39;position.commerceProperties.articleNumber&#39; | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_flat_ava**
> FlatAvaProject excel_conversion_convert_to_flat_ava(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema)

Converts Excel files to Dangl.AVA projects.

### Example
```python
from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avacloud_client_python.ExcelConversionApi(avacloud_client_python.ApiClient(configuration))
excel_file = '/path/to/file.txt' # file | The input file (optional)
read_new_elements = true # bool | Defaults to false (optional)
rebuild_item_number_schema = true # bool | When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. (optional)

try:
    # Converts Excel files to Dangl.AVA projects.
    api_response = api_instance.excel_conversion_convert_to_flat_ava(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelConversionApi->excel_conversion_convert_to_flat_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_file** | **file**| The input file | [optional] 
 **read_new_elements** | **bool**| Defaults to false | [optional] 
 **rebuild_item_number_schema** | **bool**| When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. | [optional] 

### Return type

[**FlatAvaProject**](FlatAvaProject.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_gaeb**
> file excel_conversion_convert_to_gaeb(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid)

Converts Excel files to GAEB files.

### Example
```python
from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avacloud_client_python.ExcelConversionApi(avacloud_client_python.ApiClient(configuration))
excel_file = '/path/to/file.txt' # file | The input file (optional)
read_new_elements = true # bool | Defaults to false (optional)
rebuild_item_number_schema = true # bool | When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. (optional)
destination_gaeb_type = 'destination_gaeb_type_example' # str | Defaults to GAEB XML V3.2 (optional)
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done. The phases are: Base = 81 CostEstimate = 82 OfferRequest = 83 Offer = 84 SideOffer = 85 Grant = 86 (optional)
enforce_strict_offer_phase_long_text_output = true # bool | Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. (optional)
export_quantity_determination = true # bool | Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)
force_include_descriptions = true # bool | If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. (optional)
treat_null_item_number_schema_as_invalid = true # bool | When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons. (optional)

try:
    # Converts Excel files to GAEB files.
    api_response = api_instance.excel_conversion_convert_to_gaeb(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelConversionApi->excel_conversion_convert_to_gaeb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_file** | **file**| The input file | [optional] 
 **read_new_elements** | **bool**| Defaults to false | [optional] 
 **rebuild_item_number_schema** | **bool**| When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. | [optional] 
 **destination_gaeb_type** | **str**| Defaults to GAEB XML V3.2 | [optional] 
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done. The phases are: Base &#x3D; 81 CostEstimate &#x3D; 82 OfferRequest &#x3D; 83 Offer &#x3D; 84 SideOffer &#x3D; 85 Grant &#x3D; 86 | [optional] 
 **enforce_strict_offer_phase_long_text_output** | **bool**| Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. | [optional] 
 **export_quantity_determination** | **bool**| Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the &#39;QtyDeterm&#39; (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the &#39;QuantityComponents&#39; property of positions. Please see the entry for &#39;Quantity Determination&#39; in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the &#39;QuantityComponents&#39; property. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. | [optional] 
 **force_include_descriptions** | **bool**| If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. | [optional] 
 **treat_null_item_number_schema_as_invalid** | **bool**| When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_oenorm**
> file excel_conversion_convert_to_oenorm(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts)

Converts Excel files to Oenorm files.

### Example
```python
from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = avacloud_client_python.ExcelConversionApi(avacloud_client_python.ApiClient(configuration))
excel_file = '/path/to/file.txt' # file | The input file (optional)
read_new_elements = true # bool | Defaults to false (optional)
rebuild_item_number_schema = true # bool | When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. (optional)
destination_oenorm_type = 'destination_oenorm_type_example' # str | Defaults to Lv2015 (optional)
try_repair_project_structure = true # bool | Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target (optional)
skip_try_enforce_schema_compliant_xml_output = true # bool | If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)

try:
    # Converts Excel files to Oenorm files.
    api_response = api_instance.excel_conversion_convert_to_oenorm(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelConversionApi->excel_conversion_convert_to_oenorm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_file** | **file**| The input file | [optional] 
 **read_new_elements** | **bool**| Defaults to false | [optional] 
 **rebuild_item_number_schema** | **bool**| When importing new elements from Excel, sometimes the ItemNumberSchema in the file is not in compliance with the GAEB requirements. Enabling this option tries to repair the ItemNumberSchema. Defaults to false. | [optional] 
 **destination_oenorm_type** | **str**| Defaults to Lv2015 | [optional] 
 **try_repair_project_structure** | **bool**| Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target | [optional] 
 **skip_try_enforce_schema_compliant_xml_output** | **bool**| If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


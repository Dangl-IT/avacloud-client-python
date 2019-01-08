# avacloud_client_python.ExcelConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**excel_conversion_convert_to_ava**](ExcelConversionApi.md#excel_conversion_convert_to_ava) | **POST** /conversion/excel/ava | Converts Excel files to Dangl.AVA projects.
[**excel_conversion_convert_to_excel**](ExcelConversionApi.md#excel_conversion_convert_to_excel) | **POST** /conversion/excel/excel | Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.
[**excel_conversion_convert_to_gaeb**](ExcelConversionApi.md#excel_conversion_convert_to_gaeb) | **POST** /conversion/excel/gaeb | Converts Excel files to GAEB files.


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
 - **Accept**: application/vnd.com.dangl-it.ProjectDto.v1+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_excel**
> file excel_conversion_convert_to_excel(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)

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

try:
    # Converts Excel files to Excel files. Used, for example, when elements were added in excel to generate or modify a project. The Excel file can then be shared containing the full project with all formattings, formulas and styles applied.
    api_response = api_instance.excel_conversion_convert_to_excel(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)
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

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **excel_conversion_convert_to_gaeb**
> file excel_conversion_convert_to_gaeb(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform)

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
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done (optional)

try:
    # Converts Excel files to GAEB files.
    api_response = api_instance.excel_conversion_convert_to_gaeb(excel_file=excel_file, read_new_elements=read_new_elements, rebuild_item_number_schema=rebuild_item_number_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform)
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
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


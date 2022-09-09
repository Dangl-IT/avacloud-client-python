# avacloud_client_python.AvaConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ava_conversion_convert_to_ava**](AvaConversionApi.md#ava_conversion_convert_to_ava) | **POST** /conversion/ava/ava | Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.
[**ava_conversion_convert_to_excel**](AvaConversionApi.md#ava_conversion_convert_to_excel) | **POST** /conversion/ava/excel | Converts Dangl.AVA projects to Excel
[**ava_conversion_convert_to_gaeb**](AvaConversionApi.md#ava_conversion_convert_to_gaeb) | **POST** /conversion/ava/gaeb | Converts Dangl.AVA projects to GAEB
[**ava_conversion_convert_to_oenorm**](AvaConversionApi.md#ava_conversion_convert_to_oenorm) | **POST** /conversion/ava/oenorm | Converts Dangl.AVA projects to Oenorm
[**ava_conversion_convert_to_reb**](AvaConversionApi.md#ava_conversion_convert_to_reb) | **POST** /conversion/ava/reb | Converts Dangl.AVA projects to REB
[**ava_conversion_convert_to_sia**](AvaConversionApi.md#ava_conversion_convert_to_sia) | **POST** /conversion/ava/sia | Converts Dangl.AVA projects to SIA 451


# **ava_conversion_convert_to_ava**
> ProjectDto ava_conversion_convert_to_ava(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)

Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)
remove_plain_text_long_texts = true # bool | If set to true, plain text long texts will be removed from the output to reduce response sizes (optional)
remove_html_long_texts = true # bool | If set to true, html long texts will be removed from the output to reduce response sizes (optional)

try:
    # Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.
    api_response = api_instance.ava_conversion_convert_to_ava(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **remove_plain_text_long_texts** | **bool**| If set to true, plain text long texts will be removed from the output to reduce response sizes | [optional] 
 **remove_html_long_texts** | **bool**| If set to true, html long texts will be removed from the output to reduce response sizes | [optional] 

### Return type

[**ProjectDto**](ProjectDto.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/vnd.com.dangl-it.ProjectDto.v1+json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_excel**
> file ava_conversion_convert_to_excel(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)

Converts Dangl.AVA projects to Excel

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)
write_prices = true # bool | Defaults to true (optional)
write_long_texts = true # bool | Defaults to true (optional)
conversion_culture = 'conversion_culture_example' # str | The culture that should be used for the conversion process, to have localized Excel files (optional)

try:
    # Converts Dangl.AVA projects to Excel
    api_response = api_instance.ava_conversion_convert_to_excel(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **write_prices** | **bool**| Defaults to true | [optional] 
 **write_long_texts** | **bool**| Defaults to true | [optional] 
 **conversion_culture** | **str**| The culture that should be used for the conversion process, to have localized Excel files | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_gaeb**
> file ava_conversion_convert_to_gaeb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions)

Converts Dangl.AVA projects to GAEB

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)
destination_gaeb_type = 'destination_gaeb_type_example' # str | Defaults to GAEB XML V3.2 (optional)
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done (optional)
enforce_strict_offer_phase_long_text_output = true # bool | Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. (optional)
export_quantity_determination = true # bool | Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. (optional)
force_include_descriptions = true # bool | If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. (optional)

try:
    # Converts Dangl.AVA projects to GAEB
    api_response = api_instance.ava_conversion_convert_to_gaeb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_gaeb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **destination_gaeb_type** | **str**| Defaults to GAEB XML V3.2 | [optional] 
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done | [optional] 
 **enforce_strict_offer_phase_long_text_output** | **bool**| Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. | [optional] 
 **export_quantity_determination** | **bool**| Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the &#39;QtyDeterm&#39; (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the &#39;QuantityComponents&#39; property of positions. Please see the entry for &#39;Quantity Determination&#39; in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the &#39;QuantityComponents&#39; property. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. | [optional] 
 **force_include_descriptions** | **bool**| If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_oenorm**
> file ava_conversion_convert_to_oenorm(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts)

Converts Dangl.AVA projects to Oenorm

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)
destination_oenorm_type = 'destination_oenorm_type_example' # str | Defaults to Lv2015 (optional)
try_repair_project_structure = true # bool | Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target (optional)
skip_try_enforce_schema_compliant_xml_output = true # bool | If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. (optional)

try:
    # Converts Dangl.AVA projects to Oenorm
    api_response = api_instance.ava_conversion_convert_to_oenorm(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_oenorm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **destination_oenorm_type** | **str**| Defaults to Lv2015 | [optional] 
 **try_repair_project_structure** | **bool**| Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target | [optional] 
 **skip_try_enforce_schema_compliant_xml_output** | **bool**| If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_reb**
> file ava_conversion_convert_to_reb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_reb_type=destination_reb_type)

Converts Dangl.AVA projects to REB

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)
destination_reb_type = 'destination_reb_type_example' # str | Defaults to D11 (optional)

try:
    # Converts Dangl.AVA projects to REB
    api_response = api_instance.ava_conversion_convert_to_reb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_reb_type=destination_reb_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_reb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **destination_reb_type** | **str**| Defaults to D11 | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_sia**
> file ava_conversion_convert_to_sia(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema)

Converts Dangl.AVA projects to SIA 451

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
api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
ava_project = avacloud_client_python.ProjectDto() # ProjectDto | The Dangl.AVA project
try_auto_generate_item_numbers_and_schema = true # bool | If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. (optional)

try:
    # Converts Dangl.AVA projects to SIA 451
    api_response = api_instance.ava_conversion_convert_to_sia(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_sia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


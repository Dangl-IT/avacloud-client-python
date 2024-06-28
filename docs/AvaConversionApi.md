# avacloud_client_python.AvaConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ava_conversion_convert_to_ava**](AvaConversionApi.md#ava_conversion_convert_to_ava) | **POST** /conversion/ava/ava | Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.
[**ava_conversion_convert_to_datanorm**](AvaConversionApi.md#ava_conversion_convert_to_datanorm) | **POST** /conversion/ava/datanorm | Converts Dangl.AVA projects to Datanorm
[**ava_conversion_convert_to_excel**](AvaConversionApi.md#ava_conversion_convert_to_excel) | **POST** /conversion/ava/excel | Converts Dangl.AVA projects to Excel
[**ava_conversion_convert_to_flat_ava**](AvaConversionApi.md#ava_conversion_convert_to_flat_ava) | **POST** /conversion/ava/flat-ava | Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.
[**ava_conversion_convert_to_gaeb**](AvaConversionApi.md#ava_conversion_convert_to_gaeb) | **POST** /conversion/ava/gaeb | Converts Dangl.AVA projects to GAEB
[**ava_conversion_convert_to_ids_connect**](AvaConversionApi.md#ava_conversion_convert_to_ids_connect) | **POST** /conversion/ava/ids-connect | Converts Dangl.AVA projects to IDS Connect files
[**ava_conversion_convert_to_oenorm**](AvaConversionApi.md#ava_conversion_convert_to_oenorm) | **POST** /conversion/ava/oenorm | Converts Dangl.AVA projects to Oenorm
[**ava_conversion_convert_to_reb**](AvaConversionApi.md#ava_conversion_convert_to_reb) | **POST** /conversion/ava/reb | Converts Dangl.AVA projects to REB
[**ava_conversion_convert_to_sia**](AvaConversionApi.md#ava_conversion_convert_to_sia) | **POST** /conversion/ava/sia | Converts Dangl.AVA projects to SIA 451
[**ava_conversion_convert_to_ugl**](AvaConversionApi.md#ava_conversion_convert_to_ugl) | **POST** /conversion/ava/ugl | Converts Dangl.AVA projects to UGL


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

# **ava_conversion_convert_to_datanorm**
> file ava_conversion_convert_to_datanorm(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, datanorm_destination_version=datanorm_destination_version)

Converts Dangl.AVA projects to Datanorm

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
datanorm_destination_version = 'datanorm_destination_version_example' # str | The Datanorm version to convert to. Defaults to V4. (optional)

try:
    # Converts Dangl.AVA projects to Datanorm
    api_response = api_instance.ava_conversion_convert_to_datanorm(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, datanorm_destination_version=datanorm_destination_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_datanorm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **datanorm_destination_version** | **str**| The Datanorm version to convert to. Defaults to V4. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_excel**
> file ava_conversion_convert_to_excel(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, include_article_numbers=include_article_numbers)

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
include_article_numbers = true # bool | If this is enabled, then a new column will be created in the overview worksheet that contains the article numbers for positions. Article numbers will be read from 'position.commerceProperties.articleNumber' (optional)

try:
    # Converts Dangl.AVA projects to Excel
    api_response = api_instance.ava_conversion_convert_to_excel(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, include_article_numbers=include_article_numbers)
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
 **include_article_numbers** | **bool**| If this is enabled, then a new column will be created in the overview worksheet that contains the article numbers for positions. Article numbers will be read from &#39;position.commerceProperties.articleNumber&#39; | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_flat_ava**
> FlatAvaProject ava_conversion_convert_to_flat_ava(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema)

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

try:
    # Converts Dangl.AVA projects to Dangl.AVA. This is useful when you want to generate the calculated properties.
    api_response = api_instance.ava_conversion_convert_to_flat_ava(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_flat_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 

### Return type

[**FlatAvaProject**](FlatAvaProject.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_gaeb**
> file ava_conversion_convert_to_gaeb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid)

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
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done. The phases are: Base = 81 CostEstimate = 82 OfferRequest = 83 Offer = 84 SideOffer = 85 Grant = 86 (optional)
enforce_strict_offer_phase_long_text_output = true # bool | Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. (optional)
export_quantity_determination = true # bool | Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)
force_include_descriptions = true # bool | If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. (optional)
treat_null_item_number_schema_as_invalid = true # bool | When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons. (optional)

try:
    # Converts Dangl.AVA projects to GAEB
    api_response = api_instance.ava_conversion_convert_to_gaeb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid)
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

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_ids_connect**
> file ava_conversion_convert_to_ids_connect(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, version=version)

Converts Dangl.AVA projects to IDS Connect files

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
version = 'version_example' # str | The IDS Connect version to convert to. Defaults to V2_5. (optional)

try:
    # Converts Dangl.AVA projects to IDS Connect files
    api_response = api_instance.ava_conversion_convert_to_ids_connect(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_ids_connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **version** | **str**| The IDS Connect version to convert to. Defaults to V2_5. | [optional] 

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
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)

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
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_reb**
> file ava_conversion_convert_to_reb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_reb_type=destination_reb_type, last_row_address=last_row_address)

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
last_row_address = 'last_row_address_example' # str | If this is present, the export to REB will be started from the next available row address after the given one. This must be a valid 6 character address, e.g. \"1234A0\" (optional)

try:
    # Converts Dangl.AVA projects to REB
    api_response = api_instance.ava_conversion_convert_to_reb(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, destination_reb_type=destination_reb_type, last_row_address=last_row_address)
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
 **last_row_address** | **str**| If this is present, the export to REB will be started from the next available row address after the given one. This must be a valid 6 character address, e.g. \&quot;1234A0\&quot; | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_sia**
> file ava_conversion_convert_to_sia(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, sia_destination_type=sia_destination_type)

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
sia_destination_type = 'sia_destination_type_example' # str | Defaults to Sia451 (optional)

try:
    # Converts Dangl.AVA projects to SIA 451
    api_response = api_instance.ava_conversion_convert_to_sia(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, sia_destination_type=sia_destination_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_sia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **sia_destination_type** | **str**| Defaults to Sia451 | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_ugl**
> file ava_conversion_convert_to_ugl(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, ugl_destination_version=ugl_destination_version)

Converts Dangl.AVA projects to UGL

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
ugl_destination_version = 'ugl_destination_version_example' # str | The UGL version to convert to. Defaults to V1. (optional)

try:
    # Converts Dangl.AVA projects to UGL
    api_response = api_instance.ava_conversion_convert_to_ugl(ava_project, try_auto_generate_item_numbers_and_schema=try_auto_generate_item_numbers_and_schema, ugl_destination_version=ugl_destination_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_ugl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **try_auto_generate_item_numbers_and_schema** | **bool**| If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number. | [optional] 
 **ugl_destination_version** | **str**| The UGL version to convert to. Defaults to V1. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


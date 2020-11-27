# avacloud_client_python.SiaConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sia_conversion_convert_to_ava**](SiaConversionApi.md#sia_conversion_convert_to_ava) | **POST** /conversion/sia/ava | Converts SIA 451 files to Dangl.AVA projects
[**sia_conversion_convert_to_excel**](SiaConversionApi.md#sia_conversion_convert_to_excel) | **POST** /conversion/sia/excel | Converts SIA 451 files to Excel
[**sia_conversion_convert_to_gaeb**](SiaConversionApi.md#sia_conversion_convert_to_gaeb) | **POST** /conversion/sia/gaeb | Converts SIA 451 files to GAEB files
[**sia_conversion_convert_to_oenorm**](SiaConversionApi.md#sia_conversion_convert_to_oenorm) | **POST** /conversion/sia/oenorm | Converts SIA 451 files to Oenorm files


# **sia_conversion_convert_to_ava**
> ProjectDto sia_conversion_convert_to_ava(sia_file=sia_file, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)

Converts SIA 451 files to Dangl.AVA projects

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
api_instance = avacloud_client_python.SiaConversionApi(avacloud_client_python.ApiClient(configuration))
sia_file = '/path/to/file.txt' # file | The input file (optional)
remove_plain_text_long_texts = true # bool | If set to true, plain text long texts will be removed from the output to reduce response sizes (optional)
remove_html_long_texts = true # bool | If set to true, html long texts will be removed from the output to reduce response sizes (optional)

try:
    # Converts SIA 451 files to Dangl.AVA projects
    api_response = api_instance.sia_conversion_convert_to_ava(sia_file=sia_file, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiaConversionApi->sia_conversion_convert_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sia_file** | **file**| The input file | [optional] 
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

# **sia_conversion_convert_to_excel**
> file sia_conversion_convert_to_excel(sia_file=sia_file, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)

Converts SIA 451 files to Excel

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
api_instance = avacloud_client_python.SiaConversionApi(avacloud_client_python.ApiClient(configuration))
sia_file = '/path/to/file.txt' # file | The input file (optional)
write_prices = true # bool | Defaults to true (optional)
write_long_texts = true # bool | Defaults to true (optional)
conversion_culture = 'conversion_culture_example' # str | The culture that should be used for the conversion process, to have localized Excel files (optional)

try:
    # Converts SIA 451 files to Excel
    api_response = api_instance.sia_conversion_convert_to_excel(sia_file=sia_file, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiaConversionApi->sia_conversion_convert_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sia_file** | **file**| The input file | [optional] 
 **write_prices** | **bool**| Defaults to true | [optional] 
 **write_long_texts** | **bool**| Defaults to true | [optional] 
 **conversion_culture** | **str**| The culture that should be used for the conversion process, to have localized Excel files | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sia_conversion_convert_to_gaeb**
> file sia_conversion_convert_to_gaeb(sia_file=sia_file, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output)

Converts SIA 451 files to GAEB files

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
api_instance = avacloud_client_python.SiaConversionApi(avacloud_client_python.ApiClient(configuration))
sia_file = '/path/to/file.txt' # file | The input file (optional)
destination_gaeb_type = 'destination_gaeb_type_example' # str | Defaults to GAEB XML V3.2 (optional)
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done (optional)
enforce_strict_offer_phase_long_text_output = true # bool | Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. (optional)

try:
    # Converts SIA 451 files to GAEB files
    api_response = api_instance.sia_conversion_convert_to_gaeb(sia_file=sia_file, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiaConversionApi->sia_conversion_convert_to_gaeb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sia_file** | **file**| The input file | [optional] 
 **destination_gaeb_type** | **str**| Defaults to GAEB XML V3.2 | [optional] 
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done | [optional] 
 **enforce_strict_offer_phase_long_text_output** | **bool**| Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sia_conversion_convert_to_oenorm**
> file sia_conversion_convert_to_oenorm(sia_file=sia_file, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure)

Converts SIA 451 files to Oenorm files

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
api_instance = avacloud_client_python.SiaConversionApi(avacloud_client_python.ApiClient(configuration))
sia_file = '/path/to/file.txt' # file | The input file (optional)
destination_oenorm_type = 'destination_oenorm_type_example' # str | Defaults to Lv2015 (optional)
try_repair_project_structure = true # bool | Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target (optional)

try:
    # Converts SIA 451 files to Oenorm files
    api_response = api_instance.sia_conversion_convert_to_oenorm(sia_file=sia_file, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiaConversionApi->sia_conversion_convert_to_oenorm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sia_file** | **file**| The input file | [optional] 
 **destination_oenorm_type** | **str**| Defaults to Lv2015 | [optional] 
 **try_repair_project_structure** | **bool**| Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


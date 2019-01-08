# avacloud_client_python.AvaConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ava_conversion_convert_to_excel**](AvaConversionApi.md#ava_conversion_convert_to_excel) | **POST** /conversion/ava/excel | Converts Dangl.AVA projects to Excel
[**ava_conversion_convert_to_gaeb**](AvaConversionApi.md#ava_conversion_convert_to_gaeb) | **POST** /conversion/ava/gaeb | Converts Dangl.AVA projects to GAEB


# **ava_conversion_convert_to_excel**
> file ava_conversion_convert_to_excel(ava_project, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)

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
write_prices = true # bool | Defaults to true (optional)
write_long_texts = true # bool | Defaults to true (optional)
conversion_culture = 'conversion_culture_example' # str | The culture that should be used for the conversion process, to have localized Excel files (optional)

try:
    # Converts Dangl.AVA projects to Excel
    api_response = api_instance.ava_conversion_convert_to_excel(ava_project, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **write_prices** | **bool**| Defaults to true | [optional] 
 **write_long_texts** | **bool**| Defaults to true | [optional] 
 **conversion_culture** | **str**| The culture that should be used for the conversion process, to have localized Excel files | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ava_conversion_convert_to_gaeb**
> file ava_conversion_convert_to_gaeb(ava_project, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform)

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
destination_gaeb_type = 'destination_gaeb_type_example' # str | Defaults to GAEB XML V3.2 (optional)
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done (optional)

try:
    # Converts Dangl.AVA projects to GAEB
    api_response = api_instance.ava_conversion_convert_to_gaeb(ava_project, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_gaeb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project** | [**ProjectDto**](ProjectDto.md)| The Dangl.AVA project | 
 **destination_gaeb_type** | **str**| Defaults to GAEB XML V3.2 | [optional] 
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


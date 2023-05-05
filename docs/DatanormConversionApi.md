# avacloud_client_python.DatanormConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datanorm_conversion_convert_to_ava**](DatanormConversionApi.md#datanorm_conversion_convert_to_ava) | **POST** /conversion/datanorm/ava | Converts Datanorm files to Dangl.AVA projects


# **datanorm_conversion_convert_to_ava**
> ProjectDto datanorm_conversion_convert_to_ava(datanorm_file=datanorm_file, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)

Converts Datanorm files to Dangl.AVA projects

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
api_instance = avacloud_client_python.DatanormConversionApi(avacloud_client_python.ApiClient(configuration))
datanorm_file = '/path/to/file.txt' # file | The input file (optional)
remove_plain_text_long_texts = true # bool | If set to true, plain text long texts will be removed from the output to reduce response sizes (optional)
remove_html_long_texts = true # bool | If set to true, html long texts will be removed from the output to reduce response sizes (optional)

try:
    # Converts Datanorm files to Dangl.AVA projects
    api_response = api_instance.datanorm_conversion_convert_to_ava(datanorm_file=datanorm_file, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatanormConversionApi->datanorm_conversion_convert_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datanorm_file** | **file**| The input file | [optional] 
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


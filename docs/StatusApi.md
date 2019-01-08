# avacloud_client_python.StatusApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get_status**](StatusApi.md#status_get_status) | **GET** /status | Reports the health status of the AVACloud API


# **status_get_status**
> GetStatus status_get_status()

Reports the health status of the AVACloud API

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
api_instance = avacloud_client_python.StatusApi(avacloud_client_python.ApiClient(configuration))

try:
    # Reports the health status of the AVACloud API
    api_response = api_instance.status_get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStatus**](GetStatus.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


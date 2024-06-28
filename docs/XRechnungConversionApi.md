# avacloud_client_python.XRechnungConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**x_rechnung_conversion_convert_ava_to_x_rechnung**](XRechnungConversionApi.md#x_rechnung_conversion_convert_ava_to_x_rechnung) | **POST** /conversion/xrechnung/ava-wrapper/xrechnung | This will convert an AVA wrapper object to an XRechnung file
[**x_rechnung_conversion_convert_invoice_to_x_rechnung**](XRechnungConversionApi.md#x_rechnung_conversion_convert_invoice_to_x_rechnung) | **POST** /conversion/xrechnung/invoice/xrechnung | This will convert an Invoice object to an XRechnung file
[**x_rechnung_conversion_convert_x_rechnung_to_ava**](XRechnungConversionApi.md#x_rechnung_conversion_convert_x_rechnung_to_ava) | **POST** /conversion/xrechnung/ava-wrapper | This will read an XRechnung file and convert it to an AVA wrapper object
[**x_rechnung_conversion_convert_x_rechnung_to_invoice**](XRechnungConversionApi.md#x_rechnung_conversion_convert_x_rechnung_to_invoice) | **POST** /conversion/xrechnung/invoice | This will read an XRechnung file and convert it to an Invoice object


# **x_rechnung_conversion_convert_ava_to_x_rechnung**
> file x_rechnung_conversion_convert_ava_to_x_rechnung(ava_wrapper)

This will convert an AVA wrapper object to an XRechnung file

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
api_instance = avacloud_client_python.XRechnungConversionApi(avacloud_client_python.ApiClient(configuration))
ava_wrapper = avacloud_client_python.AvaProjectWrapper() # AvaProjectWrapper | 

try:
    # This will convert an AVA wrapper object to an XRechnung file
    api_response = api_instance.x_rechnung_conversion_convert_ava_to_x_rechnung(ava_wrapper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XRechnungConversionApi->x_rechnung_conversion_convert_ava_to_x_rechnung: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_wrapper** | [**AvaProjectWrapper**](AvaProjectWrapper.md)|  | 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_rechnung_conversion_convert_invoice_to_x_rechnung**
> file x_rechnung_conversion_convert_invoice_to_x_rechnung(invoice)

This will convert an Invoice object to an XRechnung file

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
api_instance = avacloud_client_python.XRechnungConversionApi(avacloud_client_python.ApiClient(configuration))
invoice = avacloud_client_python.Invoice() # Invoice | 

try:
    # This will convert an Invoice object to an XRechnung file
    api_response = api_instance.x_rechnung_conversion_convert_invoice_to_x_rechnung(invoice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XRechnungConversionApi->x_rechnung_conversion_convert_invoice_to_x_rechnung: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)|  | 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_rechnung_conversion_convert_x_rechnung_to_ava**
> AvaProjectWrapper x_rechnung_conversion_convert_x_rechnung_to_ava(xrechnung_file=xrechnung_file)

This will read an XRechnung file and convert it to an AVA wrapper object

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
api_instance = avacloud_client_python.XRechnungConversionApi(avacloud_client_python.ApiClient(configuration))
xrechnung_file = '/path/to/file.txt' # file |  (optional)

try:
    # This will read an XRechnung file and convert it to an AVA wrapper object
    api_response = api_instance.x_rechnung_conversion_convert_x_rechnung_to_ava(xrechnung_file=xrechnung_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XRechnungConversionApi->x_rechnung_conversion_convert_x_rechnung_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xrechnung_file** | **file**|  | [optional] 

### Return type

[**AvaProjectWrapper**](AvaProjectWrapper.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x_rechnung_conversion_convert_x_rechnung_to_invoice**
> Invoice x_rechnung_conversion_convert_x_rechnung_to_invoice(xrechnung_file=xrechnung_file)

This will read an XRechnung file and convert it to an Invoice object

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
api_instance = avacloud_client_python.XRechnungConversionApi(avacloud_client_python.ApiClient(configuration))
xrechnung_file = '/path/to/file.txt' # file |  (optional)

try:
    # This will read an XRechnung file and convert it to an Invoice object
    api_response = api_instance.x_rechnung_conversion_convert_x_rechnung_to_invoice(xrechnung_file=xrechnung_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XRechnungConversionApi->x_rechnung_conversion_convert_x_rechnung_to_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xrechnung_file** | **file**|  | [optional] 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


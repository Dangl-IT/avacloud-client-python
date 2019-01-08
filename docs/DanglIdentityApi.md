# avacloud_client_python.DanglIdentityApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dangl_identity_login_and_return_token**](DanglIdentityApi.md#dangl_identity_login_and_return_token) | **POST** /identity/token-login | 
[**dangl_identity_login_with_cookie**](DanglIdentityApi.md#dangl_identity_login_with_cookie) | **POST** /identity/login | 
[**dangl_identity_refresh_token**](DanglIdentityApi.md#dangl_identity_refresh_token) | **POST** /identity/token-refresh | 
[**dangl_identity_register**](DanglIdentityApi.md#dangl_identity_register) | **POST** /identity/register | 
[**dangl_identity_request_password_reset**](DanglIdentityApi.md#dangl_identity_request_password_reset) | **POST** /identity/password-forgotten | 
[**dangl_identity_sign_out_with_sign_in_manager**](DanglIdentityApi.md#dangl_identity_sign_out_with_sign_in_manager) | **DELETE** /identity/login | 


# **dangl_identity_login_and_return_token**
> TokenResponseGet dangl_identity_login_and_return_token(model)



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))
model = avacloud_client_python.TokenLoginPost() # TokenLoginPost | 

try:
    api_response = api_instance.dangl_identity_login_and_return_token(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_login_and_return_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**TokenLoginPost**](TokenLoginPost.md)|  | 

### Return type

[**TokenResponseGet**](TokenResponseGet.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dangl_identity_login_with_cookie**
> dangl_identity_login_with_cookie(model, redirect_url=redirect_url)



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))
model = avacloud_client_python.LoginPost() # LoginPost | 
redirect_url = 'redirect_url_example' # str |  (optional)

try:
    api_instance.dangl_identity_login_with_cookie(model, redirect_url=redirect_url)
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_login_with_cookie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**LoginPost**](LoginPost.md)|  | 
 **redirect_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dangl_identity_refresh_token**
> TokenResponseGet dangl_identity_refresh_token(model)



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))
model = avacloud_client_python.TokenRefreshPost() # TokenRefreshPost | 

try:
    api_response = api_instance.dangl_identity_refresh_token(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**TokenRefreshPost**](TokenRefreshPost.md)|  | 

### Return type

[**TokenResponseGet**](TokenResponseGet.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dangl_identity_register**
> dangl_identity_register(register_model)



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))
register_model = avacloud_client_python.RegisterPost() # RegisterPost | 

try:
    api_instance.dangl_identity_register(register_model)
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_model** | [**RegisterPost**](RegisterPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dangl_identity_request_password_reset**
> dangl_identity_request_password_reset(forgot_password_model)



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))
forgot_password_model = avacloud_client_python.ForgotPasswordPost() # ForgotPasswordPost | 

try:
    api_instance.dangl_identity_request_password_reset(forgot_password_model)
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_request_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_model** | [**ForgotPasswordPost**](ForgotPasswordPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dangl_identity_sign_out_with_sign_in_manager**
> dangl_identity_sign_out_with_sign_in_manager()



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
api_instance = avacloud_client_python.DanglIdentityApi(avacloud_client_python.ApiClient(configuration))

try:
    api_instance.dangl_identity_sign_out_with_sign_in_manager()
except ApiException as e:
    print("Exception when calling DanglIdentityApi->dangl_identity_sign_out_with_sign_in_manager: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# avacloud_client_python.ValidationApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validation_validate_file**](ValidationApi.md#validation_validate_file) | **POST** /validation/file | This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.
[**validation_validate_project**](ValidationApi.md#validation_validate_project) | **POST** /validation/project | This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.


# **validation_validate_file**
> ValidationResult validation_validate_file(ava_file=ava_file, file_validation_source_type=file_validation_source_type)

This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.

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
api_instance = avacloud_client_python.ValidationApi(avacloud_client_python.ApiClient(configuration))
ava_file = '/path/to/file.txt' # file | The file to validate (optional)
file_validation_source_type = 'file_validation_source_type_example' # str | You need to indicate which type of file is being provided, there is no auto detection mechanism (optional)

try:
    # This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.
    api_response = api_instance.validation_validate_file(ava_file=ava_file, file_validation_source_type=file_validation_source_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->validation_validate_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_file** | **file**| The file to validate | [optional] 
 **file_validation_source_type** | **str**| You need to indicate which type of file is being provided, there is no auto detection mechanism | [optional] 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validation_validate_project**
> ValidationResult validation_validate_project(ava_project_validation_source_options)

This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.

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
api_instance = avacloud_client_python.ValidationApi(avacloud_client_python.ApiClient(configuration))
ava_project_validation_source_options = avacloud_client_python.PostAvaProjectValidationSourceOptions() # PostAvaProjectValidationSourceOptions | The options used for the validation operation

try:
    # This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.
    api_response = api_instance.validation_validate_project(ava_project_validation_source_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->validation_validate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ava_project_validation_source_options** | [**PostAvaProjectValidationSourceOptions**](PostAvaProjectValidationSourceOptions.md)| The options used for the validation operation | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


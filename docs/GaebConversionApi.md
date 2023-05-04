# avacloud_client_python.GaebConversionApi

All URIs are relative to *https://avacloud-api.dangl-it.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gaeb_conversion_convert_to_ava**](GaebConversionApi.md#gaeb_conversion_convert_to_ava) | **POST** /conversion/gaeb/ava | Converts GAEB files to Dangl.AVA projects
[**gaeb_conversion_convert_to_excel**](GaebConversionApi.md#gaeb_conversion_convert_to_excel) | **POST** /conversion/gaeb/excel | Converts GAEB files to Excel
[**gaeb_conversion_convert_to_gaeb**](GaebConversionApi.md#gaeb_conversion_convert_to_gaeb) | **POST** /conversion/gaeb/gaeb | Converts GAEB files to GAEB files. Used for example when transforming or repairing GAEB files.
[**gaeb_conversion_convert_to_oenorm**](GaebConversionApi.md#gaeb_conversion_convert_to_oenorm) | **POST** /conversion/gaeb/oenorm | Converts GAEB files to Oenorm files


# **gaeb_conversion_convert_to_ava**
> ProjectDto gaeb_conversion_convert_to_ava(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)

Converts GAEB files to Dangl.AVA projects

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
api_instance = avacloud_client_python.GaebConversionApi(avacloud_client_python.ApiClient(configuration))
gaeb_file = '/path/to/file.txt' # file | The input file (optional)
support_skipped_item_number_levels_in_positions = true # bool | Defaults to 'false'. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just '01.02', then it will be displayed as '01.__.02' if this is set to true. (optional)
remove_plain_text_long_texts = true # bool | If set to true, plain text long texts will be removed from the output to reduce response sizes (optional)
remove_html_long_texts = true # bool | If set to true, html long texts will be removed from the output to reduce response sizes (optional)
output_html_as_xml = true # bool | Defaults to 'false'. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce '<br />' instead of '<br>'. (optional)
keep_empty_html_text = true # bool | Defaults to 'false'. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. (optional)
allow_upper_case_item_numbers = true # bool | Defaults to 'false'. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. (optional)

try:
    # Converts GAEB files to Dangl.AVA projects
    api_response = api_instance.gaeb_conversion_convert_to_ava(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, remove_plain_text_long_texts=remove_plain_text_long_texts, remove_html_long_texts=remove_html_long_texts, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_ava: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gaeb_file** | **file**| The input file | [optional] 
 **support_skipped_item_number_levels_in_positions** | **bool**| Defaults to &#39;false&#39;. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just &#39;01.02&#39;, then it will be displayed as &#39;01.__.02&#39; if this is set to true. | [optional] 
 **remove_plain_text_long_texts** | **bool**| If set to true, plain text long texts will be removed from the output to reduce response sizes | [optional] 
 **remove_html_long_texts** | **bool**| If set to true, html long texts will be removed from the output to reduce response sizes | [optional] 
 **output_html_as_xml** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce &#39;&lt;br /&gt;&#39; instead of &#39;&lt;br&gt;&#39;. | [optional] 
 **keep_empty_html_text** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. | [optional] 
 **allow_upper_case_item_numbers** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. | [optional] 

### Return type

[**ProjectDto**](ProjectDto.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.com.dangl-it.ProjectDto.v1+json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gaeb_conversion_convert_to_excel**
> file gaeb_conversion_convert_to_excel(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)

Converts GAEB files to Excel

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
api_instance = avacloud_client_python.GaebConversionApi(avacloud_client_python.ApiClient(configuration))
gaeb_file = '/path/to/file.txt' # file | The input file (optional)
support_skipped_item_number_levels_in_positions = true # bool | Defaults to 'false'. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just '01.02', then it will be displayed as '01.__.02' if this is set to true. (optional)
write_prices = true # bool | Defaults to true (optional)
write_long_texts = true # bool | Defaults to true (optional)
conversion_culture = 'conversion_culture_example' # str | The culture that should be used for the conversion process, to have localized Excel files (optional)
output_html_as_xml = true # bool | Defaults to 'false'. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce '<br />' instead of '<br>'. (optional)
keep_empty_html_text = true # bool | Defaults to 'false'. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. (optional)
allow_upper_case_item_numbers = true # bool | Defaults to 'false'. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. (optional)

try:
    # Converts GAEB files to Excel
    api_response = api_instance.gaeb_conversion_convert_to_excel(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, write_prices=write_prices, write_long_texts=write_long_texts, conversion_culture=conversion_culture, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gaeb_file** | **file**| The input file | [optional] 
 **support_skipped_item_number_levels_in_positions** | **bool**| Defaults to &#39;false&#39;. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just &#39;01.02&#39;, then it will be displayed as &#39;01.__.02&#39; if this is set to true. | [optional] 
 **write_prices** | **bool**| Defaults to true | [optional] 
 **write_long_texts** | **bool**| Defaults to true | [optional] 
 **conversion_culture** | **str**| The culture that should be used for the conversion process, to have localized Excel files | [optional] 
 **output_html_as_xml** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce &#39;&lt;br /&gt;&#39; instead of &#39;&lt;br&gt;&#39;. | [optional] 
 **keep_empty_html_text** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. | [optional] 
 **allow_upper_case_item_numbers** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gaeb_conversion_convert_to_gaeb**
> file gaeb_conversion_convert_to_gaeb(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)

Converts GAEB files to GAEB files. Used for example when transforming or repairing GAEB files.

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
api_instance = avacloud_client_python.GaebConversionApi(avacloud_client_python.ApiClient(configuration))
gaeb_file = '/path/to/file.txt' # file | The input file (optional)
support_skipped_item_number_levels_in_positions = true # bool | Defaults to 'false'. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just '01.02', then it will be displayed as '01.__.02' if this is set to true. (optional)
destination_gaeb_type = 'destination_gaeb_type_example' # str | Defaults to GAEB XML V3.2 (optional)
target_exchange_phase_transform = 'target_exchange_phase_transform_example' # str | Defaults to none, meaning no transformation will be done (optional)
enforce_strict_offer_phase_long_text_output = true # bool | Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. (optional)
export_quantity_determination = true # bool | Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)
force_include_descriptions = true # bool | If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. (optional)
treat_null_item_number_schema_as_invalid = true # bool | When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons. (optional)
output_html_as_xml = true # bool | Defaults to 'false'. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce '<br />' instead of '<br>'. (optional)
keep_empty_html_text = true # bool | Defaults to 'false'. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. (optional)
allow_upper_case_item_numbers = true # bool | Defaults to 'false'. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. (optional)

try:
    # Converts GAEB files to GAEB files. Used for example when transforming or repairing GAEB files.
    api_response = api_instance.gaeb_conversion_convert_to_gaeb(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, destination_gaeb_type=destination_gaeb_type, target_exchange_phase_transform=target_exchange_phase_transform, enforce_strict_offer_phase_long_text_output=enforce_strict_offer_phase_long_text_output, export_quantity_determination=export_quantity_determination, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, force_include_descriptions=force_include_descriptions, treat_null_item_number_schema_as_invalid=treat_null_item_number_schema_as_invalid, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_gaeb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gaeb_file** | **file**| The input file | [optional] 
 **support_skipped_item_number_levels_in_positions** | **bool**| Defaults to &#39;false&#39;. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just &#39;01.02&#39;, then it will be displayed as &#39;01.__.02&#39; if this is set to true. | [optional] 
 **destination_gaeb_type** | **str**| Defaults to GAEB XML V3.2 | [optional] 
 **target_exchange_phase_transform** | **str**| Defaults to none, meaning no transformation will be done | [optional] 
 **enforce_strict_offer_phase_long_text_output** | **bool**| Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export. | [optional] 
 **export_quantity_determination** | **bool**| Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the &#39;QtyDeterm&#39; (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the &#39;QuantityComponents&#39; property of positions. Please see the entry for &#39;Quantity Determination&#39; in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the &#39;QuantityComponents&#39; property. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. | [optional] 
 **force_include_descriptions** | **bool**| If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions. | [optional] 
 **treat_null_item_number_schema_as_invalid** | **bool**| When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons. | [optional] 
 **output_html_as_xml** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce &#39;&lt;br /&gt;&#39; instead of &#39;&lt;br&gt;&#39;. | [optional] 
 **keep_empty_html_text** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. | [optional] 
 **allow_upper_case_item_numbers** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gaeb_conversion_convert_to_oenorm**
> file gaeb_conversion_convert_to_oenorm(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)

Converts GAEB files to Oenorm files

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
api_instance = avacloud_client_python.GaebConversionApi(avacloud_client_python.ApiClient(configuration))
gaeb_file = '/path/to/file.txt' # file | The input file (optional)
support_skipped_item_number_levels_in_positions = true # bool | Defaults to 'false'. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just '01.02', then it will be displayed as '01.__.02' if this is set to true. (optional)
destination_oenorm_type = 'destination_oenorm_type_example' # str | Defaults to Lv2015 (optional)
try_repair_project_structure = true # bool | Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target (optional)
skip_try_enforce_schema_compliant_xml_output = true # bool | If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. (optional)
remove_unprintable_characters_from_texts = true # bool | If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. (optional)
output_html_as_xml = true # bool | Defaults to 'false'. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce '<br />' instead of '<br>'. (optional)
keep_empty_html_text = true # bool | Defaults to 'false'. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. (optional)
allow_upper_case_item_numbers = true # bool | Defaults to 'false'. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. (optional)

try:
    # Converts GAEB files to Oenorm files
    api_response = api_instance.gaeb_conversion_convert_to_oenorm(gaeb_file=gaeb_file, support_skipped_item_number_levels_in_positions=support_skipped_item_number_levels_in_positions, destination_oenorm_type=destination_oenorm_type, try_repair_project_structure=try_repair_project_structure, skip_try_enforce_schema_compliant_xml_output=skip_try_enforce_schema_compliant_xml_output, remove_unprintable_characters_from_texts=remove_unprintable_characters_from_texts, output_html_as_xml=output_html_as_xml, keep_empty_html_text=keep_empty_html_text, allow_upper_case_item_numbers=allow_upper_case_item_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_oenorm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gaeb_file** | **file**| The input file | [optional] 
 **support_skipped_item_number_levels_in_positions** | **bool**| Defaults to &#39;false&#39;. This controls if, when deserializing GAEB files, skipped levels in position item numbers should be supported. For example, if an ItemNumberSchema defines three levels - two group levels and one position level - but the ItemNumber of the position is just &#39;01.02&#39;, then it will be displayed as &#39;01.__.02&#39; if this is set to true. | [optional] 
 **destination_oenorm_type** | **str**| Defaults to Lv2015 | [optional] 
 **try_repair_project_structure** | **bool**| Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target | [optional] 
 **skip_try_enforce_schema_compliant_xml_output** | **bool**| If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option. | [optional] 
 **remove_unprintable_characters_from_texts** | **bool**| If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true. | [optional] 
 **output_html_as_xml** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text will be output as XML in the output. This means that e.g. void Html tags will always be output with their closing tag, e.g. it will produce &#39;&lt;br /&gt;&#39; instead of &#39;&lt;br&gt;&#39;. | [optional] 
 **keep_empty_html_text** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then Html text that is empty will be kept in the output. Otherwise, Html text without any plain text will be removed. This is useful for example if you want to keep texts that only consist of empty paragraphs in the output. | [optional] 
 **allow_upper_case_item_numbers** | **bool**| Defaults to &#39;false&#39;. If this is enabled, then the ItemNumber of positions will be in uppercase format if the source file has them. By default, all item numbers will be converted to lowercase, but this option will enable the option to support uppercase item numbers as well. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[Dangl.Identity](../README.md#Dangl.Identity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


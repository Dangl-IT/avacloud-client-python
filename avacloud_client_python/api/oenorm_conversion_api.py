# coding: utf-8

"""
    AVACloud API 1.41.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from avacloud_client_python.api_client import ApiClient


class OenormConversionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oenorm_conversion_convert_to_ava(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Dangl.AVA projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_ava(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param bool remove_plain_text_long_texts: If set to true, plain text long texts will be removed from the output to reduce response sizes
        :param bool remove_html_long_texts: If set to true, html long texts will be removed from the output to reduce response sizes
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oenorm_conversion_convert_to_ava_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oenorm_conversion_convert_to_ava_with_http_info(**kwargs)  # noqa: E501
            return data

    def oenorm_conversion_convert_to_ava_with_http_info(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Dangl.AVA projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_ava_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param bool remove_plain_text_long_texts: If set to true, plain text long texts will be removed from the output to reduce response sizes
        :param bool remove_html_long_texts: If set to true, html long texts will be removed from the output to reduce response sizes
        :return: ProjectDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oenorm_file', 'remove_plain_text_long_texts', 'remove_html_long_texts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oenorm_conversion_convert_to_ava" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'remove_plain_text_long_texts' in params:
            query_params.append(('RemovePlainTextLongTexts', params['remove_plain_text_long_texts']))  # noqa: E501
        if 'remove_html_long_texts' in params:
            query_params.append(('RemoveHtmlLongTexts', params['remove_html_long_texts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'oenorm_file' in params:
            local_var_files['oenormFile'] = params['oenorm_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.com.dangl-it.ProjectDto.v1+json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/oenorm/ava', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oenorm_conversion_convert_to_excel(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Excel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_excel(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param bool write_prices: Defaults to true
        :param bool write_long_texts: Defaults to true
        :param str conversion_culture: The culture that should be used for the conversion process, to have localized Excel files
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oenorm_conversion_convert_to_excel_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oenorm_conversion_convert_to_excel_with_http_info(**kwargs)  # noqa: E501
            return data

    def oenorm_conversion_convert_to_excel_with_http_info(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Excel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_excel_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param bool write_prices: Defaults to true
        :param bool write_long_texts: Defaults to true
        :param str conversion_culture: The culture that should be used for the conversion process, to have localized Excel files
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oenorm_file', 'write_prices', 'write_long_texts', 'conversion_culture']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oenorm_conversion_convert_to_excel" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'write_prices' in params:
            query_params.append(('WritePrices', params['write_prices']))  # noqa: E501
        if 'write_long_texts' in params:
            query_params.append(('WriteLongTexts', params['write_long_texts']))  # noqa: E501
        if 'conversion_culture' in params:
            query_params.append(('ConversionCulture', params['conversion_culture']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'oenorm_file' in params:
            local_var_files['oenormFile'] = params['oenorm_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/oenorm/excel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oenorm_conversion_convert_to_gaeb(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to GAEB files.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_gaeb(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param str destination_gaeb_type: Defaults to GAEB XML V3.2
        :param str target_exchange_phase_transform: Defaults to none, meaning no transformation will be done
        :param bool enforce_strict_offer_phase_long_text_output: Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export.
        :param bool export_quantity_determination: Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property.
        :param bool remove_unprintable_characters_from_texts: If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.
        :param bool force_include_descriptions: If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions.
        :param bool treat_null_item_number_schema_as_invalid: When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oenorm_conversion_convert_to_gaeb_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oenorm_conversion_convert_to_gaeb_with_http_info(**kwargs)  # noqa: E501
            return data

    def oenorm_conversion_convert_to_gaeb_with_http_info(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to GAEB files.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_gaeb_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param str destination_gaeb_type: Defaults to GAEB XML V3.2
        :param str target_exchange_phase_transform: Defaults to none, meaning no transformation will be done
        :param bool enforce_strict_offer_phase_long_text_output: Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export.
        :param bool export_quantity_determination: Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property.
        :param bool remove_unprintable_characters_from_texts: If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.
        :param bool force_include_descriptions: If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions.
        :param bool treat_null_item_number_schema_as_invalid: When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oenorm_file', 'destination_gaeb_type', 'target_exchange_phase_transform', 'enforce_strict_offer_phase_long_text_output', 'export_quantity_determination', 'remove_unprintable_characters_from_texts', 'force_include_descriptions', 'treat_null_item_number_schema_as_invalid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oenorm_conversion_convert_to_gaeb" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'destination_gaeb_type' in params:
            query_params.append(('DestinationGaebType', params['destination_gaeb_type']))  # noqa: E501
        if 'target_exchange_phase_transform' in params:
            query_params.append(('TargetExchangePhaseTransform', params['target_exchange_phase_transform']))  # noqa: E501
        if 'enforce_strict_offer_phase_long_text_output' in params:
            query_params.append(('EnforceStrictOfferPhaseLongTextOutput', params['enforce_strict_offer_phase_long_text_output']))  # noqa: E501
        if 'export_quantity_determination' in params:
            query_params.append(('ExportQuantityDetermination', params['export_quantity_determination']))  # noqa: E501
        if 'remove_unprintable_characters_from_texts' in params:
            query_params.append(('RemoveUnprintableCharactersFromTexts', params['remove_unprintable_characters_from_texts']))  # noqa: E501
        if 'force_include_descriptions' in params:
            query_params.append(('ForceIncludeDescriptions', params['force_include_descriptions']))  # noqa: E501
        if 'treat_null_item_number_schema_as_invalid' in params:
            query_params.append(('TreatNullItemNumberSchemaAsInvalid', params['treat_null_item_number_schema_as_invalid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'oenorm_file' in params:
            local_var_files['oenormFile'] = params['oenorm_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/oenorm/gaeb', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oenorm_conversion_convert_to_oenorm(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Oenorm files.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_oenorm(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param str destination_oenorm_type: Defaults to Lv2015
        :param bool try_repair_project_structure: Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target
        :param bool skip_try_enforce_schema_compliant_xml_output: If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option.
        :param bool remove_unprintable_characters_from_texts: If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oenorm_conversion_convert_to_oenorm_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oenorm_conversion_convert_to_oenorm_with_http_info(**kwargs)  # noqa: E501
            return data

    def oenorm_conversion_convert_to_oenorm_with_http_info(self, **kwargs):  # noqa: E501
        """Converts ÖNorm files to Oenorm files.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oenorm_conversion_convert_to_oenorm_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file oenorm_file: The input file
        :param str destination_oenorm_type: Defaults to Lv2015
        :param bool try_repair_project_structure: Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target
        :param bool skip_try_enforce_schema_compliant_xml_output: If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option.
        :param bool remove_unprintable_characters_from_texts: If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oenorm_file', 'destination_oenorm_type', 'try_repair_project_structure', 'skip_try_enforce_schema_compliant_xml_output', 'remove_unprintable_characters_from_texts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oenorm_conversion_convert_to_oenorm" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'destination_oenorm_type' in params:
            query_params.append(('DestinationOenormType', params['destination_oenorm_type']))  # noqa: E501
        if 'try_repair_project_structure' in params:
            query_params.append(('TryRepairProjectStructure', params['try_repair_project_structure']))  # noqa: E501
        if 'skip_try_enforce_schema_compliant_xml_output' in params:
            query_params.append(('SkipTryEnforceSchemaCompliantXmlOutput', params['skip_try_enforce_schema_compliant_xml_output']))  # noqa: E501
        if 'remove_unprintable_characters_from_texts' in params:
            query_params.append(('RemoveUnprintableCharactersFromTexts', params['remove_unprintable_characters_from_texts']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'oenorm_file' in params:
            local_var_files['oenormFile'] = params['oenorm_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/oenorm/oenorm', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

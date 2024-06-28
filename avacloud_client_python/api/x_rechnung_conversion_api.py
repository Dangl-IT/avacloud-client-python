# coding: utf-8

"""
    AVACloud API 1.52.1

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.52.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from avacloud_client_python.api_client import ApiClient


class XRechnungConversionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def x_rechnung_conversion_convert_ava_to_x_rechnung(self, ava_wrapper, **kwargs):  # noqa: E501
        """This will convert an AVA wrapper object to an XRechnung file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_ava_to_x_rechnung(ava_wrapper, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AvaProjectWrapper ava_wrapper: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.x_rechnung_conversion_convert_ava_to_x_rechnung_with_http_info(ava_wrapper, **kwargs)  # noqa: E501
        else:
            (data) = self.x_rechnung_conversion_convert_ava_to_x_rechnung_with_http_info(ava_wrapper, **kwargs)  # noqa: E501
            return data

    def x_rechnung_conversion_convert_ava_to_x_rechnung_with_http_info(self, ava_wrapper, **kwargs):  # noqa: E501
        """This will convert an AVA wrapper object to an XRechnung file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_ava_to_x_rechnung_with_http_info(ava_wrapper, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AvaProjectWrapper ava_wrapper: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ava_wrapper']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method x_rechnung_conversion_convert_ava_to_x_rechnung" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ava_wrapper' is set
        if self.api_client.client_side_validation and ('ava_wrapper' not in params or
                                                       params['ava_wrapper'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ava_wrapper` when calling `x_rechnung_conversion_convert_ava_to_x_rechnung`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ava_wrapper' in params:
            body_params = params['ava_wrapper']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/xrechnung/ava-wrapper/xrechnung', 'POST',
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

    def x_rechnung_conversion_convert_invoice_to_x_rechnung(self, invoice, **kwargs):  # noqa: E501
        """This will convert an Invoice object to an XRechnung file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_invoice_to_x_rechnung(invoice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Invoice invoice: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.x_rechnung_conversion_convert_invoice_to_x_rechnung_with_http_info(invoice, **kwargs)  # noqa: E501
        else:
            (data) = self.x_rechnung_conversion_convert_invoice_to_x_rechnung_with_http_info(invoice, **kwargs)  # noqa: E501
            return data

    def x_rechnung_conversion_convert_invoice_to_x_rechnung_with_http_info(self, invoice, **kwargs):  # noqa: E501
        """This will convert an Invoice object to an XRechnung file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_invoice_to_x_rechnung_with_http_info(invoice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Invoice invoice: (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method x_rechnung_conversion_convert_invoice_to_x_rechnung" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice' is set
        if self.api_client.client_side_validation and ('invoice' not in params or
                                                       params['invoice'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `invoice` when calling `x_rechnung_conversion_convert_invoice_to_x_rechnung`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'invoice' in params:
            body_params = params['invoice']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/conversion/xrechnung/invoice/xrechnung', 'POST',
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

    def x_rechnung_conversion_convert_x_rechnung_to_ava(self, **kwargs):  # noqa: E501
        """This will read an XRechnung file and convert it to an AVA wrapper object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_x_rechnung_to_ava(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file xrechnung_file:
        :return: AvaProjectWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.x_rechnung_conversion_convert_x_rechnung_to_ava_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.x_rechnung_conversion_convert_x_rechnung_to_ava_with_http_info(**kwargs)  # noqa: E501
            return data

    def x_rechnung_conversion_convert_x_rechnung_to_ava_with_http_info(self, **kwargs):  # noqa: E501
        """This will read an XRechnung file and convert it to an AVA wrapper object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_x_rechnung_to_ava_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file xrechnung_file:
        :return: AvaProjectWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['xrechnung_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method x_rechnung_conversion_convert_x_rechnung_to_ava" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'xrechnung_file' in params:
            local_var_files['xrechnungFile'] = params['xrechnung_file']  # noqa: E501

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
            '/conversion/xrechnung/ava-wrapper', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvaProjectWrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def x_rechnung_conversion_convert_x_rechnung_to_invoice(self, **kwargs):  # noqa: E501
        """This will read an XRechnung file and convert it to an Invoice object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_x_rechnung_to_invoice(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file xrechnung_file:
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.x_rechnung_conversion_convert_x_rechnung_to_invoice_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.x_rechnung_conversion_convert_x_rechnung_to_invoice_with_http_info(**kwargs)  # noqa: E501
            return data

    def x_rechnung_conversion_convert_x_rechnung_to_invoice_with_http_info(self, **kwargs):  # noqa: E501
        """This will read an XRechnung file and convert it to an Invoice object  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.x_rechnung_conversion_convert_x_rechnung_to_invoice_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file xrechnung_file:
        :return: Invoice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['xrechnung_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method x_rechnung_conversion_convert_x_rechnung_to_invoice" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'xrechnung_file' in params:
            local_var_files['xrechnungFile'] = params['xrechnung_file']  # noqa: E501

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
            '/conversion/xrechnung/invoice', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Invoice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

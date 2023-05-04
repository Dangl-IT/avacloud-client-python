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


class ValidationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def validation_validate_file(self, **kwargs):  # noqa: E501
        """This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validation_validate_file(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file ava_file: The file to validate
        :param str file_validation_source_type: You need to indicate which type of file is being provided, there is no auto detection mechanism
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validation_validate_file_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.validation_validate_file_with_http_info(**kwargs)  # noqa: E501
            return data

    def validation_validate_file_with_http_info(self, **kwargs):  # noqa: E501
        """This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validation_validate_file_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file ava_file: The file to validate
        :param str file_validation_source_type: You need to indicate which type of file is being provided, there is no auto detection mechanism
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ava_file', 'file_validation_source_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validation_validate_file" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_validation_source_type' in params:
            query_params.append(('fileValidationSourceType', params['file_validation_source_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'ava_file' in params:
            local_var_files['avaFile'] = params['ava_file']  # noqa: E501

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
            '/validation/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validation_validate_project(self, ava_project_validation_source_options, **kwargs):  # noqa: E501
        """This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validation_validate_project(ava_project_validation_source_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAvaProjectValidationSourceOptions ava_project_validation_source_options: The options used for the validation operation (required)
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validation_validate_project_with_http_info(ava_project_validation_source_options, **kwargs)  # noqa: E501
        else:
            (data) = self.validation_validate_project_with_http_info(ava_project_validation_source_options, **kwargs)  # noqa: E501
            return data

    def validation_validate_project_with_http_info(self, ava_project_validation_source_options, **kwargs):  # noqa: E501
        """This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validation_validate_project_with_http_info(ava_project_validation_source_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAvaProjectValidationSourceOptions ava_project_validation_source_options: The options used for the validation operation (required)
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ava_project_validation_source_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validation_validate_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ava_project_validation_source_options' is set
        if self.api_client.client_side_validation and ('ava_project_validation_source_options' not in params or
                                                       params['ava_project_validation_source_options'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ava_project_validation_source_options` when calling `validation_validate_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ava_project_validation_source_options' in params:
            body_params = params['ava_project_validation_source_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/validation/project', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

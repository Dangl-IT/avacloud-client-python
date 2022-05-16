# coding: utf-8

"""
    AVACloud API 1.27.4

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.27.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""




import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from avacloud_client_python.api_client import ApiClient


class DanglIdentityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dangl_identity_login_and_return_token(self, model, **kwargs):  # noqa: E501
        """dangl_identity_login_and_return_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_login_and_return_token(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenLoginPost model: (required)
        :return: TokenResponseGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_login_and_return_token_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_login_and_return_token_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def dangl_identity_login_and_return_token_with_http_info(self, model, **kwargs):  # noqa: E501
        """dangl_identity_login_and_return_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_login_and_return_token_with_http_info(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenLoginPost model: (required)
        :return: TokenResponseGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_login_and_return_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and ('model' not in params or
                                                       params['model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `model` when calling `dangl_identity_login_and_return_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/token-login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponseGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dangl_identity_login_with_cookie(self, model, **kwargs):  # noqa: E501
        """dangl_identity_login_with_cookie  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_login_with_cookie(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginPost model: (required)
        :param str redirect_url:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_login_with_cookie_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_login_with_cookie_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def dangl_identity_login_with_cookie_with_http_info(self, model, **kwargs):  # noqa: E501
        """dangl_identity_login_with_cookie  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_login_with_cookie_with_http_info(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginPost model: (required)
        :param str redirect_url:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_login_with_cookie" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and ('model' not in params or
                                                       params['model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `model` when calling `dangl_identity_login_with_cookie`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'redirect_url' in params:
            query_params.append(('redirectUrl', params['redirect_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dangl_identity_refresh_token(self, model, **kwargs):  # noqa: E501
        """dangl_identity_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_refresh_token(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenRefreshPost model: (required)
        :return: TokenResponseGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_refresh_token_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_refresh_token_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def dangl_identity_refresh_token_with_http_info(self, model, **kwargs):  # noqa: E501
        """dangl_identity_refresh_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_refresh_token_with_http_info(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenRefreshPost model: (required)
        :return: TokenResponseGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_refresh_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and ('model' not in params or
                                                       params['model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `model` when calling `dangl_identity_refresh_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/token-refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponseGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dangl_identity_register(self, register_model, **kwargs):  # noqa: E501
        """dangl_identity_register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_register(register_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegisterPost register_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_register_with_http_info(register_model, **kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_register_with_http_info(register_model, **kwargs)  # noqa: E501
            return data

    def dangl_identity_register_with_http_info(self, register_model, **kwargs):  # noqa: E501
        """dangl_identity_register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_register_with_http_info(register_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegisterPost register_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['register_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_register" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'register_model' is set
        if self.api_client.client_side_validation and ('register_model' not in params or
                                                       params['register_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `register_model` when calling `dangl_identity_register`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'register_model' in params:
            body_params = params['register_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dangl_identity_request_password_reset(self, forgot_password_model, **kwargs):  # noqa: E501
        """dangl_identity_request_password_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_request_password_reset(forgot_password_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPasswordPost forgot_password_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_request_password_reset_with_http_info(forgot_password_model, **kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_request_password_reset_with_http_info(forgot_password_model, **kwargs)  # noqa: E501
            return data

    def dangl_identity_request_password_reset_with_http_info(self, forgot_password_model, **kwargs):  # noqa: E501
        """dangl_identity_request_password_reset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_request_password_reset_with_http_info(forgot_password_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPasswordPost forgot_password_model: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_password_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_request_password_reset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'forgot_password_model' is set
        if self.api_client.client_side_validation and ('forgot_password_model' not in params or
                                                       params['forgot_password_model'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `forgot_password_model` when calling `dangl_identity_request_password_reset`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_password_model' in params:
            body_params = params['forgot_password_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/problem+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/password-forgotten', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dangl_identity_sign_out_with_sign_in_manager(self, **kwargs):  # noqa: E501
        """dangl_identity_sign_out_with_sign_in_manager  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_sign_out_with_sign_in_manager(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dangl_identity_sign_out_with_sign_in_manager_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dangl_identity_sign_out_with_sign_in_manager_with_http_info(**kwargs)  # noqa: E501
            return data

    def dangl_identity_sign_out_with_sign_in_manager_with_http_info(self, **kwargs):  # noqa: E501
        """dangl_identity_sign_out_with_sign_in_manager  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dangl_identity_sign_out_with_sign_in_manager_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dangl_identity_sign_out_with_sign_in_manager" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/problem+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Dangl.Identity']  # noqa: E501

        return self.api_client.call_api(
            '/identity/login', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


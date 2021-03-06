# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: al.a.volkov@tinkoff.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PortfolioApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def portfolio_currencies_get(self, **kwargs):  # noqa: E501
        """Получение валютных активов клиента  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_currencies_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :return: PortfolioCurrenciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.portfolio_currencies_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.portfolio_currencies_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def portfolio_currencies_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение валютных активов клиента  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_currencies_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :return: PortfolioCurrenciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['broker_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portfolio_currencies_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portfolio/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioCurrenciesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def portfolio_get(self, **kwargs):  # noqa: E501
        """Получение портфеля клиента  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :return: PortfolioResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.portfolio_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.portfolio_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def portfolio_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение портфеля клиента  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :return: PortfolioResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['broker_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portfolio_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portfolio', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

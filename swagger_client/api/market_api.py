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


class MarketApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def market_bonds_get(self, **kwargs):  # noqa: E501
        """Получение списка облигаций  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_bonds_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_bonds_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.market_bonds_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def market_bonds_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение списка облигаций  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_bonds_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
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
                    " to method market_bonds_get" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/market/bonds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_candles_get(self, figi, _from, to, interval, **kwargs):  # noqa: E501
        """Получение исторических свечей по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_candles_get(figi, _from, to, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :param datetime _from: Начало временного промежутка (required)
        :param datetime to: Конец временного промежутка (required)
        :param CandleResolution interval: Интервал свечи (required)
        :return: CandlesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_candles_get_with_http_info(figi, _from, to, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.market_candles_get_with_http_info(figi, _from, to, interval, **kwargs)  # noqa: E501
            return data

    def market_candles_get_with_http_info(self, figi, _from, to, interval, **kwargs):  # noqa: E501
        """Получение исторических свечей по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_candles_get_with_http_info(figi, _from, to, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :param datetime _from: Начало временного промежутка (required)
        :param datetime to: Конец временного промежутка (required)
        :param CandleResolution interval: Интервал свечи (required)
        :return: CandlesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['figi', '_from', 'to', 'interval']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_candles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_candles_get`")  # noqa: E501
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `market_candles_get`")  # noqa: E501
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `market_candles_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `market_candles_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501

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
            '/market/candles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CandlesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_currencies_get(self, **kwargs):  # noqa: E501
        """Получение списка валютных пар  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_currencies_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_currencies_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.market_currencies_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def market_currencies_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение списка валютных пар  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_currencies_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
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
                    " to method market_currencies_get" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/market/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_etfs_get(self, **kwargs):  # noqa: E501
        """Получение списка ETF  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_etfs_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_etfs_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.market_etfs_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def market_etfs_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение списка ETF  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_etfs_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
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
                    " to method market_etfs_get" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/market/etfs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_orderbook_get(self, figi, depth, **kwargs):  # noqa: E501
        """Получение стакана по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_orderbook_get(figi, depth, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :param int depth: Глубина стакана [1..20] (required)
        :return: OrderbookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_orderbook_get_with_http_info(figi, depth, **kwargs)  # noqa: E501
        else:
            (data) = self.market_orderbook_get_with_http_info(figi, depth, **kwargs)  # noqa: E501
            return data

    def market_orderbook_get_with_http_info(self, figi, depth, **kwargs):  # noqa: E501
        """Получение стакана по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_orderbook_get_with_http_info(figi, depth, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :param int depth: Глубина стакана [1..20] (required)
        :return: OrderbookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['figi', 'depth']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_orderbook_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_orderbook_get`")  # noqa: E501
        # verify the required parameter 'depth' is set
        if ('depth' not in params or
                params['depth'] is None):
            raise ValueError("Missing the required parameter `depth` when calling `market_orderbook_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))  # noqa: E501
        if 'depth' in params:
            query_params.append(('depth', params['depth']))  # noqa: E501

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
            '/market/orderbook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderbookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_search_by_figi_get(self, figi, **kwargs):  # noqa: E501
        """Получение инструмента по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_search_by_figi_get(figi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :return: SearchMarketInstrumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_search_by_figi_get_with_http_info(figi, **kwargs)  # noqa: E501
        else:
            (data) = self.market_search_by_figi_get_with_http_info(figi, **kwargs)  # noqa: E501
            return data

    def market_search_by_figi_get_with_http_info(self, figi, **kwargs):  # noqa: E501
        """Получение инструмента по FIGI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_search_by_figi_get_with_http_info(figi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str figi: FIGI (required)
        :return: SearchMarketInstrumentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['figi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_search_by_figi_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_search_by_figi_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))  # noqa: E501

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
            '/market/search/by-figi', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchMarketInstrumentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_search_by_ticker_get(self, ticker, **kwargs):  # noqa: E501
        """Получение инструмента по тикеру  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_search_by_ticker_get(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: Тикер инструмента (required)
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_search_by_ticker_get_with_http_info(ticker, **kwargs)  # noqa: E501
        else:
            (data) = self.market_search_by_ticker_get_with_http_info(ticker, **kwargs)  # noqa: E501
            return data

    def market_search_by_ticker_get_with_http_info(self, ticker, **kwargs):  # noqa: E501
        """Получение инструмента по тикеру  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_search_by_ticker_get_with_http_info(ticker, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ticker: Тикер инструмента (required)
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ticker']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_search_by_ticker_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `market_search_by_ticker_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))  # noqa: E501

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
            '/market/search/by-ticker', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_stocks_get(self, **kwargs):  # noqa: E501
        """Получение списка акций  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_stocks_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.market_stocks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.market_stocks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def market_stocks_get_with_http_info(self, **kwargs):  # noqa: E501
        """Получение списка акций  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.market_stocks_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MarketInstrumentListResponse
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
                    " to method market_stocks_get" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/market/stocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

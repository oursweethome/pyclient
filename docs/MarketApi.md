# swagger_client.MarketApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_bonds_get**](MarketApi.md#market_bonds_get) | **GET** /market/bonds | Получение списка облигаций
[**market_candles_get**](MarketApi.md#market_candles_get) | **GET** /market/candles | Получение исторических свечей по FIGI
[**market_currencies_get**](MarketApi.md#market_currencies_get) | **GET** /market/currencies | Получение списка валютных пар
[**market_etfs_get**](MarketApi.md#market_etfs_get) | **GET** /market/etfs | Получение списка ETF
[**market_orderbook_get**](MarketApi.md#market_orderbook_get) | **GET** /market/orderbook | Получение стакана по FIGI
[**market_search_by_figi_get**](MarketApi.md#market_search_by_figi_get) | **GET** /market/search/by-figi | Получение инструмента по FIGI
[**market_search_by_ticker_get**](MarketApi.md#market_search_by_ticker_get) | **GET** /market/search/by-ticker | Получение инструмента по тикеру
[**market_stocks_get**](MarketApi.md#market_stocks_get) | **GET** /market/stocks | Получение списка акций

# **market_bonds_get**
> MarketInstrumentListResponse market_bonds_get()

Получение списка облигаций

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка облигаций
    api_response = api_instance.market_bonds_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_bonds_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_candles_get**
> CandlesResponse market_candles_get(figi, _from, to, interval)

Получение исторических свечей по FIGI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
figi = 'figi_example' # str | FIGI
_from = '2013-10-20T19:20:30+01:00' # datetime | Начало временного промежутка
to = '2013-10-20T19:20:30+01:00' # datetime | Конец временного промежутка
interval = swagger_client.CandleResolution() # CandleResolution | Интервал свечи

try:
    # Получение исторических свечей по FIGI
    api_response = api_instance.market_candles_get(figi, _from, to, interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_candles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **figi** | **str**| FIGI | 
 **_from** | **datetime**| Начало временного промежутка | 
 **to** | **datetime**| Конец временного промежутка | 
 **interval** | [**CandleResolution**](.md)| Интервал свечи | 

### Return type

[**CandlesResponse**](CandlesResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_currencies_get**
> MarketInstrumentListResponse market_currencies_get()

Получение списка валютных пар

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка валютных пар
    api_response = api_instance.market_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_etfs_get**
> MarketInstrumentListResponse market_etfs_get()

Получение списка ETF

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка ETF
    api_response = api_instance.market_etfs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_etfs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_orderbook_get**
> OrderbookResponse market_orderbook_get(figi, depth)

Получение стакана по FIGI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
figi = 'figi_example' # str | FIGI
depth = 56 # int | Глубина стакана [1..20]

try:
    # Получение стакана по FIGI
    api_response = api_instance.market_orderbook_get(figi, depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_orderbook_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **figi** | **str**| FIGI | 
 **depth** | **int**| Глубина стакана [1..20] | 

### Return type

[**OrderbookResponse**](OrderbookResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_search_by_figi_get**
> SearchMarketInstrumentResponse market_search_by_figi_get(figi)

Получение инструмента по FIGI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
figi = 'figi_example' # str | FIGI

try:
    # Получение инструмента по FIGI
    api_response = api_instance.market_search_by_figi_get(figi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_search_by_figi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **figi** | **str**| FIGI | 

### Return type

[**SearchMarketInstrumentResponse**](SearchMarketInstrumentResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_search_by_ticker_get**
> MarketInstrumentListResponse market_search_by_ticker_get(ticker)

Получение инструмента по тикеру

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Тикер инструмента

try:
    # Получение инструмента по тикеру
    api_response = api_instance.market_search_by_ticker_get(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_search_by_ticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Тикер инструмента | 

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_stocks_get**
> MarketInstrumentListResponse market_stocks_get()

Получение списка акций

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))

try:
    # Получение списка акций
    api_response = api_instance.market_stocks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->market_stocks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketInstrumentListResponse**](MarketInstrumentListResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


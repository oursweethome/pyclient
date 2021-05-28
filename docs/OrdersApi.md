# swagger_client.OrdersApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_cancel_post**](OrdersApi.md#orders_cancel_post) | **POST** /orders/cancel | Отмена заявки
[**orders_get**](OrdersApi.md#orders_get) | **GET** /orders | Получение списка активных заявок
[**orders_limit_order_post**](OrdersApi.md#orders_limit_order_post) | **POST** /orders/limit-order | Создание лимитной заявки
[**orders_market_order_post**](OrdersApi.md#orders_market_order_post) | **POST** /orders/market-order | Создание рыночной заявки

# **orders_cancel_post**
> Empty orders_cancel_post(order_id, broker_account_id=broker_account_id)

Отмена заявки

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
order_id = 'order_id_example' # str | ID заявки
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Отмена заявки
    api_response = api_instance.orders_cancel_post(order_id, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID заявки | 
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get**
> OrdersResponse orders_get(broker_account_id=broker_account_id)

Получение списка активных заявок

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Получение списка активных заявок
    api_response = api_instance.orders_get(broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_limit_order_post**
> LimitOrderResponse orders_limit_order_post(body, figi, broker_account_id=broker_account_id)

Создание лимитной заявки

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.LimitOrderRequest() # LimitOrderRequest | 
figi = 'figi_example' # str | FIGI инструмента
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Создание лимитной заявки
    api_response = api_instance.orders_limit_order_post(body, figi, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_limit_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LimitOrderRequest**](LimitOrderRequest.md)|  | 
 **figi** | **str**| FIGI инструмента | 
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**LimitOrderResponse**](LimitOrderResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_market_order_post**
> MarketOrderResponse orders_market_order_post(body, figi, broker_account_id=broker_account_id)

Создание рыночной заявки

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.MarketOrderRequest() # MarketOrderRequest | 
figi = 'figi_example' # str | FIGI инструмента
broker_account_id = 'broker_account_id_example' # str | Уникальный идентификатор счета (по умолчанию - Тинькофф) (optional)

try:
    # Создание рыночной заявки
    api_response = api_instance.orders_market_order_post(body, figi, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_market_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarketOrderRequest**](MarketOrderRequest.md)|  | 
 **figi** | **str**| FIGI инструмента | 
 **broker_account_id** | **str**| Уникальный идентификатор счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**MarketOrderResponse**](MarketOrderResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


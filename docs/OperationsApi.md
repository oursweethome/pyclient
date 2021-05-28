# swagger_client.OperationsApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operations_get**](OperationsApi.md#operations_get) | **GET** /operations | Получение списка операций

# **operations_get**
> OperationsResponse operations_get(_from, to, figi=figi, broker_account_id=broker_account_id)

Получение списка операций

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | Начало временного промежутка
to = '2013-10-20T19:20:30+01:00' # datetime | Конец временного промежутка
figi = 'figi_example' # str | Figi инструмента для фильтрации (optional)
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Получение списка операций
    api_response = api_instance.operations_get(_from, to, figi=figi, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->operations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Начало временного промежутка | 
 **to** | **datetime**| Конец временного промежутка | 
 **figi** | **str**| Figi инструмента для фильтрации | [optional] 
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**OperationsResponse**](OperationsResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


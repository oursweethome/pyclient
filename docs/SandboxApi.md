# swagger_client.SandboxApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_clear_post**](SandboxApi.md#sandbox_clear_post) | **POST** /sandbox/clear | Удаление всех позиций
[**sandbox_currencies_balance_post**](SandboxApi.md#sandbox_currencies_balance_post) | **POST** /sandbox/currencies/balance | Выставление баланса по валютным позициям
[**sandbox_positions_balance_post**](SandboxApi.md#sandbox_positions_balance_post) | **POST** /sandbox/positions/balance | Выставление баланса по инструментным позициям
[**sandbox_register_post**](SandboxApi.md#sandbox_register_post) | **POST** /sandbox/register | Регистрация клиента в sandbox
[**sandbox_remove_post**](SandboxApi.md#sandbox_remove_post) | **POST** /sandbox/remove | Удаление счета

# **sandbox_clear_post**
> Empty sandbox_clear_post(broker_account_id=broker_account_id)

Удаление всех позиций

Удаление всех позиций клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SandboxApi(swagger_client.ApiClient(configuration))
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Удаление всех позиций
    api_response = api_instance.sandbox_clear_post(broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_clear_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_currencies_balance_post**
> Empty sandbox_currencies_balance_post(body, broker_account_id=broker_account_id)

Выставление баланса по валютным позициям

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SandboxApi(swagger_client.ApiClient(configuration))
body = swagger_client.SandboxSetCurrencyBalanceRequest() # SandboxSetCurrencyBalanceRequest | Запрос на выставление баланса по валютным позициям
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Выставление баланса по валютным позициям
    api_response = api_instance.sandbox_currencies_balance_post(body, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_currencies_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxSetCurrencyBalanceRequest**](SandboxSetCurrencyBalanceRequest.md)| Запрос на выставление баланса по валютным позициям | 
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_positions_balance_post**
> Empty sandbox_positions_balance_post(body, broker_account_id=broker_account_id)

Выставление баланса по инструментным позициям

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SandboxApi(swagger_client.ApiClient(configuration))
body = swagger_client.SandboxSetPositionBalanceRequest() # SandboxSetPositionBalanceRequest | Запрос на выставление баланса по инструментным позициям
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Выставление баланса по инструментным позициям
    api_response = api_instance.sandbox_positions_balance_post(body, broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_positions_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxSetPositionBalanceRequest**](SandboxSetPositionBalanceRequest.md)| Запрос на выставление баланса по инструментным позициям | 
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_register_post**
> SandboxRegisterResponse sandbox_register_post(body=body)

Регистрация клиента в sandbox

Создание счета и валютных позиций для клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SandboxApi(swagger_client.ApiClient(configuration))
body = swagger_client.SandboxRegisterRequest() # SandboxRegisterRequest | Запрос на создание счета и выставление баланса по валютным позициям (optional)

try:
    # Регистрация клиента в sandbox
    api_response = api_instance.sandbox_register_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxRegisterRequest**](SandboxRegisterRequest.md)| Запрос на создание счета и выставление баланса по валютным позициям | [optional] 

### Return type

[**SandboxRegisterResponse**](SandboxRegisterResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_remove_post**
> Empty sandbox_remove_post(broker_account_id=broker_account_id)

Удаление счета

Удаление счета клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SandboxApi(swagger_client.ApiClient(configuration))
broker_account_id = 'broker_account_id_example' # str | Номер счета (по умолчанию - Тинькофф) (optional)

try:
    # Удаление счета
    api_response = api_instance.sandbox_remove_post(broker_account_id=broker_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->sandbox_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_account_id** | **str**| Номер счета (по умолчанию - Тинькофф) | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


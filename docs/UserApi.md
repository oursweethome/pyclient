# swagger_client.UserApi

All URIs are relative to *https://api-invest.tinkoff.ru/openapi/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_accounts_get**](UserApi.md#user_accounts_get) | **GET** /user/accounts | Получение брокерских счетов клиента

# **user_accounts_get**
> UserAccountsResponse user_accounts_get()

Получение брокерских счетов клиента

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Получение брокерских счетов клиента
    api_response = api_instance.user_accounts_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_accounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAccountsResponse**](UserAccountsResponse.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


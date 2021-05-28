# Orderbook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**figi** | **str** |  | 
**depth** | **int** |  | 
**bids** | [**list[OrderResponse]**](OrderResponse.md) |  | 
**asks** | [**list[OrderResponse]**](OrderResponse.md) |  | 
**trade_status** | [**TradeStatus**](TradeStatus.md) |  | 
**min_price_increment** | **float** | Шаг цены | 
**face_value** | **float** | Номинал для облигаций | [optional] 
**last_price** | **float** |  | [optional] 
**close_price** | **float** |  | [optional] 
**limit_up** | **float** | Верхняя граница цены | [optional] 
**limit_down** | **float** | Нижняя граница цены | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


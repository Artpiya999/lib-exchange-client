# OrderSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExOrdId** | **int64** | The unique order id assigned by the exchange | [optional] 
**ClOrdId** | **string** | Reference field provided by client. Cannot exceed 20 characters, only alphanumeric characters are allowed. | 
**OrdType** | [**OrdType**](ordType.md) |  | 
**OrdStatus** | [**OrderStatus**](OrderStatus.md) |  | 
**Side** | [**Side**](side.md) |  | 
**Price** | **float64** | The limit price for the order | [optional] 
**Text** | **string** | The reason for rejecting the order, if applicable | [optional] 
**Symbol** | **string** | Blockchain symbol identifier | 
**LastShares** | **float64** | The executed quantity for the order&#39;s last fill | [optional] 
**LastPx** | **float64** | The executed price for the last fill | [optional] 
**LeavesQty** | **float64** | For Open and Partially Filled orders this is the remaining quantity open for execution. For Canceled and Expired orders this is the quantity than was still open before cancellation/expiration. For Rejected order this is equal to orderQty. For other states this is always zero. | [optional] 
**CumQty** | **float64** | The quantity of the order which has been filled | [optional] 
**AvgPx** | **float64** | Calculated the Volume Weighted Average Price of all fills for this order | [optional] 
**Timestamp** | **int64** | Time in ms since 01/01/1970 (epoch) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



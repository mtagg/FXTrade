import oandapy as opy
import CONFIG

##simple order request example from the oandapy api website


order = {
     "units" : ""
}


"""
order_dic = {
    # The Order’s identifier, unique within the Order’s Account.
    id : (OrderID),

    # The time when the Order was created.
    createTime : (DateTime),

    # The current state of the Order.
    state : (OrderState),

    # The client extensions of the Order. Do not set, modify, or delete
    # clientExtensions if your account is associated with MT4.
    clientExtensions : (ClientExtensions),

    # The type of the Order. Always set to “MARKET” for Market Orders.
    type : (OrderType, default=MARKET),

    # The Market Order’s Instrument.
    instrument : (InstrumentName, required),

    # The quantity requested to be filled by the Market Order. A positive
    # number of units results in a long Order, and a negative number of units
    # results in a short Order.
    units : (DecimalNumber, required),

    # The time-in-force requested for the Market Order. Restricted to FOK or
    # IOC for a MarketOrder.
    timeInForce : (TimeInForce, required, default=FOK),

    # The worst price that the client is willing to have the Market Order
    # filled at.
    priceBound : (PriceValue),

    # Specification of how Positions in the Account are modified when the Order
    # is filled.
    positionFill : (OrderPositionFill, required, default=DEFAULT),

    # Details of the Trade requested to be closed, only provided when the
    # Market Order is being used to explicitly close a Trade.
    tradeClose : (MarketOrderTradeClose),

    # 
    # Details of the long Position requested to be closed out, only provided
    # when a Market Order is being used to explicitly closeout a long Position.
    # 
    longPositionCloseout : (MarketOrderPositionCloseout),

    # 
    # Details of the short Position requested to be closed out, only provided
    # when a Market Order is being used to explicitly closeout a short
    # Position.
    # 
    shortPositionCloseout : (MarketOrderPositionCloseout),

    # Details of the Margin Closeout that this Market Order was created for
    marginCloseout : (MarketOrderMarginCloseout),

    # Details of the delayed Trade close that this Market Order was created for
    delayedTradeClose : (MarketOrderDelayedTradeClose),

    # 
    # TakeProfitDetails specifies the details of a Take Profit Order to be
    # created on behalf of a client. This may happen when an Order is filled
    # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
    # Take Profit Order is modified directly through the Trade.
    # 
    takeProfitOnFill : (TakeProfitDetails),

    # 
    # StopLossDetails specifies the details of a Stop Loss Order to be created
    # on behalf of a client. This may happen when an Order is filled that opens
    # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
    # Order is modified directly through the Trade.
    # 
    stopLossOnFill : (StopLossDetails),

    # 
    # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
    # Order to be created on behalf of a client. This may happen when an Order
    # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
    # Trade’s dependent Trailing Stop Loss Order is modified directly through
    # the Trade.
    # 
    trailingStopLossOnFill : (TrailingStopLossDetails),

    # 
    # Client Extensions to add to the Trade created when the Order is filled
    # (if such a Trade is created). Do not set, modify, or delete
    # tradeClientExtensions if your account is associated with MT4.
    # 
    tradeClientExtensions : (ClientExtensions),

    # 
    # ID of the Transaction that filled this Order (only provided when the
    # Order’s state is FILLED)
    # 
    fillingTransactionID : (TransactionID),

    # 
    # Date/time when the Order was filled (only provided when the Order’s state
    # is FILLED)
    # 
    filledTime : (DateTime),

    # 
    # Trade ID of Trade opened when the Order was filled (only provided when
    # the Order’s state is FILLED and a Trade was opened as a result of the
    # fill)
    # 
    tradeOpenedID : (TradeID),

    # 
    # Trade ID of Trade reduced when the Order was filled (only provided when
    # the Order’s state is FILLED and a Trade was reduced as a result of the
    # fill)
    # 
    tradeReducedID : (TradeID),

    # 
    # Trade IDs of Trades closed when the Order was filled (only provided when
    # the Order’s state is FILLED and one or more Trades were closed as a
    # result of the fill)
    # 
    tradeClosedIDs : (Array[TradeID]),

    # 
    # ID of the Transaction that cancelled the Order (only provided when the
    # Order’s state is CANCELLED)
    # 
    cancellingTransactionID : (TransactionID),

    # 
    # Date/time when the Order was cancelled (only provided when the state of
    # the Order is CANCELLED)
    # 
    cancelledTime : (DateTime)
}

"""






from scripts.areas.ConnectedArea import ConnectedArea

MarketArea = {
    'trade': lambda state: state,
} + ConnectedArea

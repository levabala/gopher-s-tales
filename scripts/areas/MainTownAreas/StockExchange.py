from scripts.areas.RootArea import RootArea


def StockExchangeArea(): return {
    'area name': 'Stock Exchange',
    'symbol': '$',
    'move cost': 0,
    **RootArea()
}

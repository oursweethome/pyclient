import swagger_client
from swagger_client.rest import ApiException
from swagger_client import ApiClient
from swagger_client import MarketApi
from swagger_client.api.user_api import UserApi
from swagger_client.api.portfolio_api import PortfolioApi
from pprint import pprint


if __name__ == "__main__":
    # create an instance of the API class
    TOKEN = 't.MZiZzz4q9pfyAt2Zc12NzMmacmbdwYE2pBap5cFS3xUM16wVb-UKAF1jHO_rrQ_k_TNyANO4KIowQCg4Pojkkg'
    client = ApiClient(header_name="Authorization",header_value="Bearer "+TOKEN)
    client.set_default_header("Accept","text/html")
    api_instance = MarketApi(client)
    api = UserApi(client)
    api_portfolio = PortfolioApi(client)

    try:
        # Получение списка облигаций
        bonds = api_instance.market_bonds_get().payload.instruments
        stocks = api_instance.market_stocks_get().payload.instruments
        currencies = api_instance.market_currencies_get().payload.instruments
        accounts = api.user_accounts_get(async_req=False).payload.accounts
        accountsList = {}
        port = {}
        for pos in accounts:
            accountsList[pos.broker_account_type] = pos.broker_account_id

        portfolio = api_portfolio.portfolio_get(broker_account_id=accountsList["Tinkoff"]).payload.positions
        portfolioIis = api_portfolio.portfolio_get(broker_account_id=accountsList["TinkoffIis"]).payload.positions

    except ApiException as e:
        print("Exception: %s\n" % e)

    for pos in currencies:
        print("{} {}".format(pos.figi,pos.name))

    for pos in portfolio:
        print("{:20} {:5} {} {} {}".format(pos.name,
                                              pos.figi,
                                              pos.average_position_price.currency,
                                              pos.average_position_price.value,
                                              pos.lots
                                              )
              )

    print()
    print("{:20}{}".format("BONDS CNT:",len(bonds)))
    print("{:20}{}".format("STOCKS CNT:",len(stocks)))
    print("{:20}{}".format("CURRENCIES CNT:",len(currencies)))



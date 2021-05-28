from swagger_client.rest import ApiException
from swagger_client import ApiClient
from swagger_client import MarketApi
from swagger_client.api.user_api import UserApi
from swagger_client.api.portfolio_api import PortfolioApi
from win10toast import ToastNotifier
from threading import Timer
from tkinter import *
import time


def get_usd_kurs(portfolio):
    for item in portfolio:
        if item.name == 'Доллар США':
            item_summa = item.balance * item.average_position_price.value + item.expected_yield.value
            kurs = item_summa / item.balance
            # print("Курс USD, руб {:3.4f}".format(kurs))
            return kurs, True
    return None, False


def get_eur_kurs(portfolio):
    for item in portfolio:
        if item.name == 'Евро':
            item_summa = item.balance * item.average_position_price.value + item.expected_yield.value
            kurs = item_summa / item.balance
            # print("Курс EUR, руб {:3.4f}".format(kurs))
            return kurs, True
    return None, False


def getPortfolioCost(portfolio):
    kurs = {}
    kurs['USD'], result = get_usd_kurs(portfolio)
    if not result:
        return 0
    kurs['EUR'], result = get_eur_kurs(portfolio)
    if not result:
        return 0
    kurs['RUB'] = 1

    bal = 0
    for item in portfolio:
        if item.name in {'Доллар США', 'Евро'}:
            bal += item.balance * item.average_position_price.value + item.expected_yield.value
        else:
            bal += (item.balance * item.average_position_price.value +
                        item.expected_yield.value) * \
                       kurs[item.average_position_price.currency]
    return bal


def getBalance(portfolio_cost, currencies):
    for item in currencies:
        if item.currency == 'RUB':
            return portfolio_cost + item.balance
    return 0


def prescript(window, label):
    timer2 = Timer(5, prescript, args=(ws, lbl,))
    try:
        # Получение списка облигаций
        # bonds = api_instance.market_bonds_get().payload.instruments
        # stocks = api_instance.market_stocks_get().payload.instruments
        # currencies = api_instance.market_currencies_get().payload.instruments
        accounts = api.user_accounts_get(async_req=False).payload.accounts
        accountslist = {}
        # port = {}
        for pos in accounts:
            accountslist[pos.broker_account_type] = pos.broker_account_id
    except ApiException as e:
        toaster.show_toast("Ошибка", "%s" % e, duration=60)

    try:
        portfolio = api_portfolio.portfolio_get(broker_account_id=accountslist["Tinkoff"]).payload.positions
        currencies = api_portfolio.portfolio_currencies_get(broker_account_id=accountslist["Tinkoff"])\
            .payload.currencies
        # portfolioIis = api_portfolio.portfolio_get(broker_account_id=accountsList["TinkoffIis"]).payload.positions
        # for pos in currencies:
        #    print("{} {}".format(pos.figi, pos.name))
        # for pos in portfolio:
        #    print("{:20} {:5} {} {} {}".format(
        #        pos.name,
        #        pos.figi,
        #        pos.average_position_price.currency,
        #        pos.average_position_price.value,
        #        pos.lots))

        # for pos in currencies:
        #    print("{:5} {:5}".format(
        #        pos.currency,
        #        pos.balance))

        # print()
        # print("{:20}{}".format("BONDS CNT:", len(bonds)))
        # print("{:20}{}".format("STOCKS CNT:", len(stocks)))
        # print("{:20}{}".format("CURRENCIES CNT:", len(currencies)))
        portfolio_cost = getPortfolioCost(portfolio)
        balance = getBalance(portfolio_cost, currencies)

        if window.winfo_viewable():
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            ws.title(current_time)
            label.config(text=format(balance, '8.2f'))
            timer2.start()

    except ApiException as e:
        toaster.show_toast("Ошибка", "{}" % e, duration=60)


if __name__ == "__main__":

    ws = Tk()
    ws.geometry("225x40+300+300")
    ws.resizable(False, False)
    ws.attributes("-topmost", True)

    lbl = Label(ws, text="-", font="TimesNewRomans 18 bold")
    lbl.pack()

    toaster = ToastNotifier()

    TOKEN = "t.MZiZzz4q9pfyAt2Zc12NzMmacmbdwYE2pBap5cFS3xUM16wVb-UKAF1jHO_rrQ_k_TNyANO4KIowQCg4Pojkkg"
    client = ApiClient(header_name="Authorization", header_value="Bearer " + TOKEN)
    client.set_default_header("Accept", "text/html")
    api_instance = MarketApi(client)
    api = UserApi(client)
    api_portfolio = PortfolioApi(client)

    timer1 = Timer(0.1, prescript, args=(ws, lbl,))
    timer1.start()

    ws.mainloop()
    timer1.cancel()
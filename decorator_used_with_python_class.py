import requests


class LimitQuery:
    def __int__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f"No queries left. All {self.count} queries used.")
            return


@LimitQuery
def get_coin_price(limit):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        text = response.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


if __name__ == "__main__":
    get_coin_price(5)
    get_coin_price(5)
    get_coin_price(5)
    get_coin_price(5)
    get_coin_price(5)
    get_coin_price(5)

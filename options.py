import argparse
import yoptions as yo
import pandas as pd
import math
from scipy.stats import norm

class Study:
    def __init__(self, ticker, option_type):
        self.ticker = ticker
        self.option_type = option_type

    def __repr__(self):
        return self.name

    def get_expiration_dates(self):
        exp_dates = yo.get_expiration_dates(stock_ticker=self.ticker)
        print("Available expiration dates:")
        for date in exp_dates:
            print(date)

    def get_options_data(self, date):
        tte = (pd.to_datetime(date) - pd.Timestamp.today()).days + 1
        option_type = self.option_type[0].lower()
        options_data = yo.get_chain_greeks_date(stock_ticker=self.ticker, dividend_yield=0, option_type=option_type, expiration_date=date)
        df = pd.DataFrame(options_data)
        price = yo.get_underlying_price(df.iloc[0]["Symbol"])
        df["BS_Value"] = df.apply(lambda row: self.black_scholes_value(S=price, X=row["Strike"], T=tte, r=0.04, sigma=row["Impl. Volatility"], option_type='p'), axis=1)
        df["Difference"] = df["BS_Value"] - df["Last Price"]
        sorted_df = df.sort_values(by='Difference', ascending=False)
        return sorted_df

    def black_scholes_value(self, S, X, T, r, sigma, option_type):
        d1 = (math.log(S/X) + (r + sigma**2/2)*T/365) / (sigma*math.sqrt(T/365))
        d2 = d1 - sigma*math.sqrt(T/365)

        if option_type == 'c':
            return S*norm.cdf(d1) - X*math.exp(-r*(T/365))*norm.cdf(d2)
        elif option_type == 'p':
            return X*math.exp(-r*T/365)*norm.cdf(-d2) - S*norm.cdf(-d1)
        else:
            raise ValueError('option_type must be "c" or "p"')
        
def main():
    parser = argparse.ArgumentParser(description='Options Study')
    parser.add_argument('ticker', type=str, help='Stock ticker symbol')
    parser.add_argument('--exp_dates', action='store_true', help='Get available expiration dates')
    parser.add_argument('--d', dest='date', type=str, help='Expiration date in the format YYYY-MM-DD')
    parser.add_argument('--o', dest='option_type', choices=['p', 'c'], default='p', help='Type of options to retrieve (p/c)')
    args = parser.parse_args()

    study = Study(args.ticker, args.option_type)

    if args.exp_dates:
        study.get_expiration_dates()
    elif args.date:
        options_data = study.get_options_data(args.date)
        print(options_data)
    else:
        print("Please provide either --exp_dates or --d argument.")

if __name__ == '__main__':
    main()


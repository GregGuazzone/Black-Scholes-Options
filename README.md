## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
    - [Usage Examples](#usage-examples)
        - [Get Available Expiration Dates](#get-available-expiration-dates)
        - [Get Puts or Calls Data for a Specific Stock and Expiration Date](#get-puts-or-calls-data-for-a-specific-stock-and-expiration-date)


## Setup

##### 1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/GregGuazzone/Black-Scholes-Options.git
cd options
```

##### 2. Create a virtual environment to isolate project dependencies (optional but recommended).

*macOS/Linux*
```bash
python3 -m venv venv
source venv/bin/activate
```

*Windows*
```bash
python -m venv venv
venv\Scripts\activate
```

##### 3. Install the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Usage

##### Usage Examples

##### Get Available Expiration Dates
To get the available expiration dates for a specific stock, use the --exp_dates option:

```bash
python3 options.py AAPL --exp_dates
```

##### Get Puts or Calls Data for a Specific Stock and Expiration Date

To get the options data for a specific stock and a chosen expiration date, use the --d option. 
By default, the script retrieves put options data. To get call options data, use the --o c flag:

Get puts data for AAPL stock with expiration date 2023-08-04:
```bash
python3 options.py AAPL --d 2023-08-04
```

Get calls data for AAPL stock with expiration date 2023-08-04

```bash
python3 options.py AAPL --d 2023-08-04 --o c
```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
#!/bin/bash

# <bitbar.title>BTC2EUR</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Ryan Chiechi</bitbar.author>
# <bitbar.author.github>rchiechi</bitbar.author.github>
# <bitbar.desc>Checks BTC exchange rate.</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>bash</bitbar.dependencies>

echo -n € ; curl -4 -s https://api.coinbase.com/v1/currencies/exchange_rates | egrep -o ',"btc_to_eur":"[0-9]+(\.)?([0-9]{0,2}")?' | sed 's/,"btc_to_eur"://'  | sed 's:^.\(.*\).$:\1:'

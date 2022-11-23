# Price-Monitor
Monitor Price of BTC &amp; ETH using coingecko's public API.

## Build the image
    docker build -t monitor:slim .
## Launch the monitor
    docker compose up

Note: Change the URL endpoint and the loop on monitor.py to add more coins. Reference on how to use the API can be found here: https://www.coingecko.com/en/api 

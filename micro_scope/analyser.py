# measure price formation
# measure liquidity
# measure transaction costs
# use to monitor price discovery
# feed to visuals, decision and output
from numba import jit
import numpy as np

@jit(nopython=True)
def measure_spread(bid_prices, ask_prices):
    return ask_prices - bid_prices

@jit(nopython=True)
def measure_imbalance(bid_sizes, ask_sizes):
    return (bid_sizes - ask_sizes) / (bid_sizes + ask_sizes)
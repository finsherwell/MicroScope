"""
Market microstructure analysis module.
Implements high-performance calculations for key market metrics using Numba.
"""
from numba import njit, float64, int64, prange
import numpy as np
import time

@njit(float64[:](float64[:], float64[:]), parallel=True)
def measure_spread(bid_prices, ask_prices):
    """
    Calculate bid-ask spread for each price pair.
    Optimised with Numba for parallel computation.
    
    Args:
        bid_prices: Array of bid prices
        ask_prices: Array of ask prices
        
    Returns:
        Array of spreads (ask_price - bid_price)
    """
    n = len(bid_prices)
    spreads = np.empty(n, dtype=np.float64)

    for i in prange(n):
        spreads[i] = ask_prices[i] - bid_prices[i]

    return spreads
    
@njit(float64[:](float64[:], float64[:]), parallel=True)
def measure_imbalance(bid_sizes, ask_sizes):
    """
    Calculate order book imbalance for each size pair.
    Imbalance measures the relative difference between buy and sell pressure.
    
    Args:
        bid_sizes: Array of bid sizes
        ask_sizes: Array of ask sizes
        
    Returns:
        Array of imbalance values, range [-1, 1]
    """
    n = len(bid_sizes)
    imbalances= np.empty(n, dtype=np.float64)

    for i in prange(n):
        total = bid_sizes[i] + ask_sizes[i]
        if total > 0:
            imbalances[i] = (bid_sizes[i] - ask_sizes[i]) / total
        else:
            imbalances[i] = 0.0
            
    return imbalances

@njit(float64[:](float64[:], int64[:]), parallel=True)
def measure_intensity(volumes, time_deltas):
    """
    Calculate trading intensity (volume divided by time).
    Measures the rate of trading activity in the market.
    
    Args:
        volumes: Array of trading volumes
        time_deltas: Array of time differences in seconds
        
    Returns:
        Array of intensity values (volume per unit time)
    """
    n = len(volumes)
    intensity = np.empty(n, dtype=np.float64)

    for i in prange(n):
        if time_deltas[i] > 0:
            intensity[i] = volumes[i] / time_deltas[i]
        else:
            if i > 0:
                intensity[i] = intensity[i-1]
            else:
                intensity[i] = 0.0

@njit
def calculate_metrics_batch(bid_prices, ask_prices, bid_sizes, ask_sizes, volumes, time_deltas, batch_size=10000):
    """
    Calculate all market metrics in batches to optimise memory usage and cache performance.
    
    Args:
        bid_prices: Array of bid prices
        ask_prices: Array of ask prices
        bid_sizes: Array of bid sizes
        ask_sizes: Array of ask sizes
        volumes: Array of trade volumes
        time_deltas: Array of time differences
        batch_size: Size of processing batches
        
    Returns:
        Tuple of (spreads, imbalances, intensities)
    """
    n = len(bid_prices)

    spreads = np.empty(n, dtype=np.float64)
    imbalances = np.empty(n, dtype=np.float64)
    intensity = np.empty(n, dtype=np.float64)

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)

        batch_spreads = measure_spread(bid_prices[start:end], ask_prices[start:end])
        batch_imbalances = measure_imbalance(bid_sizes[start:end], ask_sizes[start:end])
        batch_intensity = measure_intensity(volumes[start:end], time_deltas[start:end])

        spreads[start:end] = batch_spreads
        imbalances[start:end] = batch_imbalances
        intensity[start:end] = batch_intensity
    
    return spreads, imbalances, intensity

def calculate_metrics(bid_data, ask_data, volumes_data, timestamp_data):
    """
    Main entry point for metric calculation.
    Converts input data to optimised formats and calls Numba-accelerated functions.
    
    Args:
        bid_data: Dictionary with 'prices' and 'sizes' arrays
        ask_data: Dictionary with 'prices' and 'sizes' arrays
        volume_data: Array of trading volumes
        timestamp_data: Array of timestamps
        
    Returns:
        Dictionary with calculated metrics
    """
    start_time = time.time()

    bid_prices = np.asarray(bid_data['prices'], dtype=np.float64)
    ask_prices = np.asarray(ask_data['prices'], dtype=np.float64)
    bid_sizes = np.asarray(bid_data['sizes'], dtype=np.float64)
    ask_sizes = np.asarray(ask_data['sizes'], dtype=np.float64)
    volumes = np.asarray(volumes_data, dtype=np.float64)

    timestamps = np.asarray(timestamp_data, dtype=np.int64)
    time_deltas = np.empty_like(timestamps)
    time_deltas[0] = 1
    time_deltas[1:] = timestamps[1:] - timestamps[:-1]

    spreads, imbalances, intensities = calculate_metrics_batch(
        bid_prices, ask_prices, bid_sizes, ask_sizes, volumes, time_deltas
    )
    
    calculation_time = time.time() - start_time
    
    return {
        'spread': spreads,
        'imbalance': imbalances,
        'intensity': intensities,
        'calculation_time': calculation_time
    }
import datetime, os, yaml

from dotenv import load_dotenv
from pathlib import Path
from hashlib import md5

def convert_timestamps_to_datetime(timestamps):
    """Convert Unix timestamps to datetime objects."""
    return [datetime.datetime.fromtimestamp(ts) for ts in timestamps]

def generate_key_value(ticker, timestamp, spread, imbalance, intensity):
    """Generates a key value to identify data by, based on key data (make sure quick)"""
    data = f"{ticker}|{timestamp}|{spread}|{imbalance}|{intensity}"
    return md5(data.encode()).hexdigest()

def load_config_file(config_path=None):
    """  
    Load configuration from YAML file.
    
    Args:
        config_path: Path to config file
        
    Returns:
        Configuration dictionary
    """
    if config_path == None:
        config_path = Path(os.path.dirname(os.path.dirname(__file__))) / "config.yaml"
    
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Warning: Could not load config file. Error: {e}")
        return {
            'data_source': 'manual',
            'max_trade_size': 1000,
            'decision_thresholds': {
                'spread_max': 0.05,
                'imbalance_min': 0.2,
                'intensity_min': 5
            }
        }


def get_alpha_api_key():
    return load_dotenv("ALPHA_VANTAGE_API_KEY")
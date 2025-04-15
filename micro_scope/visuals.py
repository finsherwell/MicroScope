import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pathlib import Path
from utils import convert_timestamps_to_datetime

# make directory in reports/graphs for graph data, name of directory is key generated value, search for key generated value in reports, then
# put visuals in keyvalue/graphs folder
def create_spread_chart(timestamps, spreads, output_path):
    """
    Create a chart showing spread over time.
    
    Args:
        timestamps: Array of timestamps
        spreads: Array of spread values
        output_path: Path to save the chart
        
    Returns:
        Path to the saved chart
    """
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")

def create_imbalance_chart():

def create_intensity_chart():

def create_decision_timeline():

def create_spread_intensity_plot():

def generate_all_charts():
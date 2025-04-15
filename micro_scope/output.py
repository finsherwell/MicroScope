import json, decision

from utils import generate_key_value

def generate_dict(timestamp, spread, imbalance, intensity):
    dec = decision.make_decision()
    dict = {"timestamp": timestamp, 
            "metrics": {"spread": spread, "imbalance": imbalance, "intensity": intensity},
            "decision": dec
    }
    return dict

def generate_key(ticker, timestamp, spread, imbalance, intensity):
    return generate_key_value(ticker, timestamp, spread, imbalance, intensity)

def generate_json_from_dict(dict):
    return json.dumps(dict)

def output_json_file():
    key = generate_key()
    dict = generate_json_from_dict(generate_dict())
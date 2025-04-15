import json, decision, hashlib, random, time

def generate_dict(timestamp, spread, imbalance, intensity):
    dec = decision.make_decision
    timestamp = int(time.time())

    data = f"{timestamp}-{spread}-{imbalance}-{intensity}-{random.random()}"
    unique_key = hashlib.sha256(data.encode()).hexdigest
    dict = {
        unique_key: {"timestamp": timestamp, 
                     "metrics": {"spread": spread, "imbalance": imbalance, "intensity": intensity},
                     "decision": dec
                     }
    }
    return dict

def generate_json_from_dict(dict):
    return json.dumps(dict)
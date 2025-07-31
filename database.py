import json
import os

DATA_FILE = "data.json"

# Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"players": {}, "tournaments": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Initialize DB
def init_db():
    if not os.path.exists(DATA_FILE):
        save_data({"players": {}, "tournaments": []})

# Save tournament registration
def save_tournament_registration(user_id, name):
    data = load_data()
    if user_id not in [p["user_id"] for p in data["tournaments"]]:
        data["tournaments"].append({"user_id": user_id, "name": name})
        save_data(data)

# Get tournament players
def get_tournament_players():
    data = load_data()
    return data["tournaments"]

# Save player stats
def save_player_stats(user_id, name, goals=0):
    data = load_data()
    if str(user_id) not in data["players"]:
        data["players"][str(user_id)] = {"name": name, "goals": 0, "matches": 0}
    data["players"][str(user_id)]["goals"] += goals
    data["players"][str(user_id)]["matches"] += 1
    save_data(data)

# Get stats
def get_player_stats(user_id):
    data = load_data()
    return data["players"].get(str(user_id), {"name": "Unknown", "goals": 0, "matches": 0})

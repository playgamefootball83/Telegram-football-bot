from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["football_bot"]

# Initialize database collections
def init_db():
    db.players.create_index("user_id", unique=True)
    db.tournaments.create_index("user_id", unique=True)

# Save tournament registration
def save_tournament_registration(user_id, name):
    db.tournaments.update_one(
        {"user_id": user_id},
        {"$set": {"name": name}},
        upsert=True
    )

# Get all tournament players
def get_tournament_players():
    return list(db.tournaments.find({}, {"_id": 0}))

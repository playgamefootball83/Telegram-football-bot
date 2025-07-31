from telegram import Update
from telegram.ext import ContextTypes
from database import save_tournament_registration, get_tournament_players

tournaments = {}

async def handle_tournament_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user

    if chat_id not in tournaments:
        tournaments[chat_id] = {"players": []}

    if user.id not in tournaments[chat_id]["players"]:
        tournaments[chat_id]["players"].append(user.id)
        save_tournament_registration(user.id, user.first_name)
        await update.message.reply_text(f"✅ {user.first_name} registered for the tournament!")
    else:
        await update.message.reply_text("❌ You are already registered!")

async def show_tournament_players(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in tournaments or len(tournaments[chat_id]["players"]) == 0:
        await update.message.reply_text("No players registered yet.")
        return

    players = get_tournament_players()
    player_names = [p["name"] for p in players]
    await update.message.reply_text("🎯 *Tournament Players:*\n" + "\n".join(player_names), parse_mode="Markdown")

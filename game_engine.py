import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Store active games
active_games = {}

async def handle_mode_selection(query, context):
    mode = query.data
    chat_id = query.message.chat_id

    if mode == "solo_mode":
        active_games[chat_id] = {"mode": "solo", "players": []}
        await query.edit_message_caption(
            caption="⚽ *Solo Mode Selected*\nWaiting for 2 players to join...",
            parse_mode="Markdown"
        )

    elif mode == "team_mode":
        active_games[chat_id] = {"mode": "team", "teams": {"A": [], "B": []}}
        await query.edit_message_caption(
            caption="🏆 *Team Mode Selected*\nHost please set teams using /add_A and /add_B.",
            parse_mode="Markdown"
        )

    elif mode == "tournament_mode":
        await query.edit_message_caption(
            caption="🎯 *Tournament Mode*\nUse /register_tournament to start registrations.",
            parse_mode="Markdown"
        )

async def start_match(chat_id, context):
    game = active_games.get(chat_id)
    if not game:
        return

    if game["mode"] == "solo":
        players = game["players"]
        if len(players) == 2:
            await context.bot.send_message(chat_id, f"🎮 *Solo Match Started!*\n{players[0]} vs {players[1]}", parse_mode="Markdown")
        else:
            await context.bot.send_message(chat_id, "Need 2 players to start a solo match.")

    elif game["mode"] == "team":
        team_a = ", ".join(game["teams"]["A"])
        team_b = ", ".join(game["teams"]["B"])
        await context.bot.send_message(chat_id, f"🏟️ *Team Match Started!*\nTeam A: {team_a}\nvs\nTeam B: {team_b}", parse_mode="Markdown")

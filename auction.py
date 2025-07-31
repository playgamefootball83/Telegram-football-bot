import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from database import get_player_stats

auctions = {}

async def start_auction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in auctions:
        await update.message.reply_text("⚠️ An auction is already running!")
        return

    auctions[chat_id] = {"host": update.effective_user.id, "bidders": {}, "current_player": None, "active": True}
    await update.message.reply_text(
        "🏆 Auction started!\n\n"
        "👉 Use /add_player <name> to add players for bidding.\n"
        "👉 Bidders use +0.5 or +1 to bid.\n"
        "👉 Host uses /next to move to the next player."
    )

async def add_player(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in auctions or not auctions[chat_id]["active"]:
        return

    player_name = " ".join(context.args)
    if not player_name:
        await update.message.reply_text("❌ Usage: /add_player <name>")
        return

    auctions[chat_id]["current_player"] = {"name": player_name, "highest": 0, "winner": None}
    await update.message.reply_text(
        f"⚽ Player up for auction: *{player_name}*\n\n💰 Start bidding!", parse_mode="Markdown"
    )

async def bid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user

    if chat_id not in auctions or not auctions[chat_id]["active"]:
        return

    msg = update.message.text.strip()
    if msg not in ["+0.5", "+1"]:
        return

    current = auctions[chat_id]["current_player"]
    if not current:
        return

    bid_value = 0.5 if msg == "+0.5" else 1
    total_bid = auctions[chat_id]["bidders"].get(user.id, 0) + bid_value
    auctions[chat_id]["bidders"][user.id] = total_bid

    if total_bid > current["highest"]:
        current["highest"] = total_bid
        current["winner"] = user.id

    await update.message.reply_text(
        f"💸 {user.first_name} bid {bid_value}!\n"
        f"🏆 Current Highest: {current['highest']} by {user.first_name}"
    )

async def next_player(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in auctions or not auctions[chat_id]["active"]:
        return

    current = auctions[chat_id]["current_player"]
    if not current:
        await update.message.reply_text("⚠️ No player in auction. Use /add_player first.")
        return

    winner_id = current["winner"]
    if winner_id:
        stats = get_player_stats(winner_id)
        await update.message.reply_text(
            f"✅ *{current['name']}* SOLD to <a href='tg://user?id={winner_id}'>"
            f"{stats['name']}</a> for {current['highest']} 💰",
            parse_mode="HTML"
        )
    else:
        await update.message.reply_text(f"⏹️ No bids for *{current['name']}*", parse_mode="Markdown")

    auctions[chat_id]["current_player"] = None

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TOKEN
from game_engine import handle_mode_selection, start_match
from tournament import handle_tournament_commands
from database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize DB
init_db()

async def start_football(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Solo Mode", callback_data="solo_mode")],
        [InlineKeyboardButton("🏆 Team Mode", callback_data="team_mode")],
        [InlineKeyboardButton("🎯 Tournament", callback_data="tournament_mode")]
    ]
    await update.message.reply_animation(
        animation="https://media.giphy.com/media/OYAn8wyZylD1W/giphy.gif",
        caption="🏟️ *Play Football Bot*\nChoose a mode to start the game!",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await handle_mode_selection(query, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start_football", start_football))
    app.add_handler(CallbackQueryHandler(button_handler))
    # Tournament commands
    app.add_handler(CommandHandler("register_tournament", handle_tournament_commands))
    app.run_polling()

application.add_handler(CommandHandler("start_auction", start_auction))
application.add_handler(CommandHandler("add_player", add_player))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bid))
application.add_handler(CommandHandler("next", next_player))

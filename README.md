# ⚽ Telegram Football Bot

A Telegram bot to host football matches, tournaments, and player auctions with real-time commentary, GIFs, and stats.

---

## 🔥 Features
- ✅ Solo & Team Matches
- ✅ Tournament + Auction System
- ✅ Real Football GIFs & English Commentary
- ✅ Player Stats & MVP
- ✅ Goalkeeper Selection & Replacement
- ✅ Logs to Dedicated Group
- ✅ 30+ Teams in Tournaments

---

## 🔑 Environment Variables
---

## 🛠️ Bot Commands & Explanation

- `/start` → Start the bot.
- `/help` → Shows rules and how to play.
- `/create_match` → Create a football match.
- `/join` → Join the current match.
- `/start_match` → Start the match after teams are set.
- `/stats` → Shows player performance & MVP.
- `/tournament` → Create a tournament.
- `/auction` → Start player auction with bidding.
- `/end_tournament` → End tournament & clear data.
- `/set_captain` → Change team captain.
- `/replace_player` → Replace any offline player.
- `/logs` → Sends logs to dedicated group.

---

## 🚀 Deployment Methods

### ✅ VPS / Local Server

```bash
git clone https://github.com/playgamefootball83/Telegram-football-bot.git
cd Telegram-football-bot
pip install -r requirements.txt

# Add environment variables
export BOT_TOKEN=7665417259:AAG_1zJDDv21BrBoANbNjfADiQPk4A1WRco
export OWNER_USERNAME=II_Mr_Attitude_II
export SUPPORT_GROUP=https://t.me/Football_support_group
export SUPPORT_CHANNEL=https://t.me/Football_support_channel
export LOGS_GROUP_ID=-1002725338652

python3 main.py

# A Simple Telegram Bot
This telegram bot was built using pyTelegramBotApi and gspread, and deployed on Heroku.  
The main functionality of this bot is to:
1) Read data from Google Sheets
2) Output data based on given command

# Commands
- **/list** - lists out the events for this week. A week starts on Monday, and ends on Sunday.
- **/upcoming** - lists the next event
- **/listRemaining** - lists the remaining items for this month

# Learning Outcome
It's a simple bot, but a few things I learned are:
1) How to deploy stuff onto heroku!
2) How to make a (simple) Telegram bot
3) Making use of Google Drive/Sheets API on Google Cloud in order to read Google Sheets, and making meaningful use of the data

Overall, it was pretty fun. I struggled most with getting the Heroku deployment properly, which I thought should have been the easiest. But that's my own mistake, as I was really just trying to rush through it (HUGE mistake).

🎌 Mahiru Anime Hub Bot

A powerful Telegram Anime Provider Bot built with ⚡ speed, MongoDB, and smart search.

---

✨ Features

- 🔍 Smart Anime Search
  
  - Exact search → "/anime"
  - Partial search → "/search"
  - Button UI → "/btn"
  - Auto-detect from text

- 📜 Anime List System
  
  - Paginated "/animelist"
  - Fast navigation buttons

- ⚡ Ultra Fast Performance
  
  - MongoDB caching system
  - Optimized search index

- 📢 Broadcast System
  
  - Copy-paste messages (buttons, media, formatting)
  - Send to all users & groups

- 🧠 Advanced Database
  
  - MongoDB (async)
  - Users + Groups tracking
  - Anime storage system

- 🎭 Fun + Utility
  
  - Roast system 😈
  - Admin list (Anime styled)
  - Owner detection (Hokage 👑)
  - ID, Ping, Help commands

---

📂 Project Structure

AnimeProvider/
│
├── main.py
├── config.py
├── mongodb.py
│
├── start.py
├── anime.py
├── search.py
├── animelist.py
├── callback.py
├── inline.py
│
├── add.py
├── broadcast.py
│
├── misc.py
├── group.py
│
├── utilc.py
├── utilf.py
├── utilh.py
│
├── requirements.txt
└── README.md

---

⚙️ Setup

1️⃣ Clone Repo

git clone https://github.com/your-username/AnimeProvider.git
cd AnimeProvider

---

2️⃣ Install Requirements

pip install -r requirements.txt

---

3️⃣ Setup Environment

Create ".env" file:

BOT_TOKEN=your_bot_token_here
MONGO_URI=your_mongodb_uri_here

---

4️⃣ Run Bot

python main.py

---

☁️ Deploy on Render

- Create a new Web Service on Render
- Add environment variables:
  - "BOT_TOKEN"
  - "MONGO_URI"
- Build command:

pip install -r requirements.txt

- Start command:

python main.py

---

🎯 Commands

🔍 Anime

- "/anime Naruto"
- "/search One Piece"
- "/btn Bleach"
- "/animelist"

⚙️ Admin

- "/add"
- "/del"
- "/broadcast"
- "/stats"
- "/bulkadd"

🎭 Fun & Utility

- "/roast"
- "/id"
- "/owner"
- "/adminlist"
- "/ping"
- "/help"

---

⚡ Performance

- 🔥 Cached DB system
- 🚀 Fast response time
- 📉 Reduced Mongo usage

---

👑 Credits

- Developed by Sahu Bots
- Powered by Python & MongoDB

---

⭐ Support

If you like this project:

👉 Star the repo
👉 Share with friends
👉 Build your own anime bot 😈

---

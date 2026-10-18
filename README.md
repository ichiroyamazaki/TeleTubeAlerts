# 📊 Telegram YouTube Stats Bot

> A robust, lightning-fast Telegram bot designed to fetch and display real-time YouTube channel analytics, subscriber milestones, view counts, and video statistics instantly within your Telegram chats.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot%20API-2CA5E0?logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![YouTube API](https://img.shields.io/badge/YouTube-Data%20API%20v3-FF0000?logo=youtube&logoColor=white)](https://developers.google.com/youtube/v3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Developed and maintained by **GoForAll Worldwide Corporation**  
Created by **Ichiro Yamazaki**

---

## 🚀 Features

* **Real-Time Analytics:** Pulls live subscriber counts, total views, and video upload statistics straight from the YouTube Data API v3.
* **Instant Command Lookups:** Query any public YouTube channel using simple Telegram commands (`/stats`).
* **Rich Markdown Formatting:** Clean, easily readable outputs with emojis, clean spacing, and structured data layouts.
* **Lightweight & Async:** Built using asynchronous Python libraries for high concurrency and zero lag under heavy group loads.
* **Secure Environment Configuration:** Environment-based credential management to keep API keys safe.

---

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Framework / Library:** `python-telegram-bot` (or `aiogram`)
* **API:** YouTube Data API v3

---

## 📋 Prerequisites

Before running or deploying the bot, make sure you have:
1. Python `3.9` or higher installed on your machine.
2. A **Telegram Bot Token** obtained from [@BotFather](https://t.me/BotFather).
3. A **Google Cloud / YouTube Data API v3 Key** from the [Google Cloud Console](https://console.cloud.google.com/).

---

## ⚙️ Installation & Local Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/GoForAll-Worldwide-Corporation/telegram-youtube-stats-bot.git](https://github.com/GoForAll-Worldwide-Corporation/telegram-youtube-stats-bot.git)
   cd telegram-youtube-stats-bot
Create and Activate a Virtual Environment:Bashpython -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install Dependencies:Bashpip install -r requirements.txt
Configure Environment Variables:Create a .env file in the root directory and add your credentials:Code snippetTELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
YOUTUBE_API_KEY=your_google_youtube_api_key_here
Run the Bot:Bashpython main.py
⌨️ Bot CommandsCommandDescriptionExample/startInitializes the bot and displays the welcome message./start/statsFetches public analytics for a specified YouTube channel or username./stats @GoForAllCorp/helpDisplays usage instructions and available commands./help📁 Project StructurePlaintexttelegram-youtube-stats-bot/
│
├── core/
│   ├── __init__.py
│   ├── bot_handler.py      # Telegram command logic & routers
│   └── youtube_client.py   # YouTube Data API v3 integration wrapper
│
├── .env.example            # Template for environment variables
├── .gitignore              # Ignored files (venv, .env, __pycache__)
├── LICENSE                 # MIT License file
├── README.md               # Project documentation
├── requirements.txt        # Python package dependencies
└── main.py                 # Application entry point
🏢 Corporate OwnershipThis project is official open-source software owned and managed by GoForAll Worldwide Corporation.Lead Architect & Developer: Ichiro YamazakiContact & Support: For corporate inquiries, bug reports, or feature requests, please open an issue in this repository or contact the GoForAll development team.📄 LicenseDistributed under the MIT License. See LICENSE for more information.

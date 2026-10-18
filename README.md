# 📊 Telegram YouTube Stats Bot (TeleTubeAlerts)

> A robust, automated Telegram bot designed to deliver daily YouTube channel analytics and milestone alerts straight to your chat. 

<div align="center">

[![GitHub Release](https://img.shields.io/github/v/release/ichiroyamazaki/TeleTubeAlerts?style=flat-square&color=green)](https://github.com/ichiroyamazaki/TeleTubeAlerts/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/ichiroyamazaki/TeleTubeAlerts/graphs/commit-activity)

</div>

---

## 🚀 Overview

**TeleTubeAlerts** is an automated monitoring tool built for creators, agencies, and community managers who want to keep a close eye on their YouTube performance without constantly opening YouTube Studio. Powered by Python and integrated seamlessly with the Telegram Bot API and YouTube Data API v3, it fetches up-to-date metrics—such as subscriber counts, total views, and video uploads—and pushes structured daily summaries directly to your Telegram channel or group.

---

## 💼 Corporate & Creator Credit

* **Developed by:** [Ichiro Yamazaki](https://github.com/ichiroyamazaki)
* **Organization:** GoForAll Worldwide Corporation

---

## ✨ Features

* **Daily Automated Reports:** Scheduled updates providing clear, at-a-glance performance metrics.
* **Real-Time Channel Metrics:** Tracks total subscribers, view counts, video counts, and growth variations.
* **Lightweight & Fast:** Built with efficiency in mind to run smoothly on local machines, VPS, or cloud containers (Docker-ready).
* **Easy Configuration:** Simple environment variables setup to manage Telegram tokens and YouTube channel IDs.

---

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **APIs:** 
  * Telegram Bot API
  * YouTube Data API v3
* **Libraries:** `requests`, `python-dotenv`, `apscheduler` (or equivalent task scheduler)

---

## 📦 Project Structure

```text
TeleTubeAlerts/
├── bot.py              # Main application entry point
├── config.py           # Configuration and environment loaders
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
└── README.md           # Project documentation
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/ichiroyamazaki/TeleTubeAlerts.git](https://github.com/ichiroyamazaki/TeleTubeAlerts.git)
cd TeleTubeAlerts
2. Install Dependencies
Make sure you have Python 3.8+ installed, then run:

Bash
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory using the template provided below or copy .env.example:

Code snippet
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
YOUTUBE_API_KEY=your_google_youtube_api_key_here
YOUTUBE_CHANNEL_ID=your_youtube_channel_id_here
TELEGRAM_BOT_TOKEN: Get this from @BotFather on Telegram.

TELEGRAM_CHAT_ID: The target chat or channel ID where alerts will be posted.

YOUTUBE_API_KEY: Generated via the Google Cloud Console with YouTube Data API v3 enabled.

YOUTUBE_CHANNEL_ID: The unique identifier of the YouTube channel you want to monitor.

4. Run the Bot
Bash
python bot.py
🤝 Contributing
Contributions, bug reports, and feature requests are welcome!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

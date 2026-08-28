"""
Торговый бот с ML + Telegram уведомления
Для деплоя на Bothost
"""

import requests
import time
import os
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier

# Переменные окружения на Bothost
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# Настройки
CHECK_INTERVAL = 300
TAKE_PROFIT = 8.0
STOP_LOSS = -5.0
CONFIDENCE_THRESHOLD = 0.55
DEPOSIT = 1000.0
RISK_PER_TRADE = 2.0

# ... (остальной код из предыдущих сообщений)

if __name__ == "__main__":
    main()

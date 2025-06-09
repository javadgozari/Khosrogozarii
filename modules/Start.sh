#!/bin/bash

echo "📦 در حال نصب پیش‌نیازها..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🚀 اجرای ربات خسرو از داخل پوشه modules..."
python modules/khosrow_bot.py

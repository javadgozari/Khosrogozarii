#!/bin/bash

echo "📦 در حال ارتقای pip..."
pip install --upgrade pip

echo "📥 در حال نصب پکیج‌ها..."
pip install -r requirements.txt

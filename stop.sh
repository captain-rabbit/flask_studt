#!/bin/bash

echo "停止 uWSGI..."
pkill -f uwsgi

echo "停止 Nginx..."
sudo systemctl stop nginx

echo "🛑 所有服务已停止。"

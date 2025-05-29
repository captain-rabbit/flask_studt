#!/bin/bash

echo "重启 uWSGI..."
pkill -f uwsgi
sleep 1
uwsgi --ini /my_work/flask_web/flask_studt/study_uwsgi.ini &

echo "重启 Nginx..."
sudo systemctl restart nginx

echo "✅ 所有服务已重启完成。"

#!bin/bash

echo cd /var/www/html/Interface/Front/ViaTur

echo nohup npm run dev -- --host &

echo cd /var/www/html/Interface/Back/BackViaTur

echo nohup php artisan serve &

echo "Servidores Iniciados"

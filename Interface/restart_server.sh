#!/bin/bash

cd /var/www/html/Interface/Front/ViaTur

nohup npm run dev -- --host &

cd /var/www/html/Interface/Back/BackViaTur

nohup php artisan serve --host=0.0.0.0 --port=4173 &

echo "Servidores Iniciados"

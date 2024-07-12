#!/bin/bash

# Настройка Postfix
postconf -e 'relayhost = [smtp.example.com]:587'
postconf -e 'smtp_sasl_auth_enable = yes'
postconf -e 'smtp_sasl_password_maps = static:your_email@example.com:your_password'
postconf -e 'smtp_sasl_security_options = noanonymous'
postconf -e 'smtp_tls_security_level = encrypt'
postconf -e 'smtp_tls_note_starttls_offer = yes'
postconf -e 'myhostname = localhost_post'  # Или замените на имя вашего компьютера
postconf -e 'mydestination = localhost'

# Запуск Postfix
service postfix start

# Keep container running
tail -f /var/log/mail.log

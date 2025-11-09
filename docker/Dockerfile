# Oficjalny obraz PHP z Apache
FROM php:7.4.33-apache

# Inatalacja pakietów
RUN apt-get update && apt-get install -y \
    openssl \
    unzip \
    libzip-dev \
    libicu-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev

# Konfiguracja php    
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql opcache zip intl

# Miejsce pod SSL    
RUN mkdir -p /etc/ssl/certs /etc/ssl/private

# Generowanie samopodpisanego certyfikatu SSL
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/cert.key \
    -out /etc/ssl/certs/cert.crt \
    -subj "/C=PL/ST=SelfSigned/L=Docker/O=PrestashopProject/CN=localhost"

# Włączenie modułu SSL w Apache
RUN a2enmod ssl

# Usunięcie domyślnych
RUN rm -f /etc/apache2/sites-enabled/000-default.conf
RUN rm -f /etc/apache2/sites-available/default-ssl.conf

# Nowa konfiguracja Apache
RUN cat > /etc/apache2/sites-available/prestashop.conf <<\
EOF
    <VirtualHost *:80>
        ServerName localhost
        # Przekierowanie HTTP na HTTPS (dla czystości, PrestaShop też może to zrobić)
        Redirect permanent / https://localhost/
    </VirtualHost>

    <IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName localhost
        DocumentRoot /var/www/html/

        SSLEngine on
        SSLCertificateFile    /etc/ssl/certs/cert.crt
        SSLCertificateKeyFile /etc/ssl/private/cert.key

        <Directory /var/www/html/>
            Options FollowSymlinks
            # Kluczowe dla PrestaShop i mod_rewrite
            AllowOverride All 
            Require all granted
        </Directory>
    </VirtualHost>
    </IfModule>
EOF

# Włącz nową konfiguracje
RUN a2ensite prestashop.conf

# Włącz mod_rewrite (wymagane przez PrestaShop)
RUN a2enmod rewrite

# Konfiguracja PHP dla PrestaShop
RUN echo "short_open_tag = Off" >> /usr/local/etc/php/conf.d/prestashop-custom.ini

# Pobranie i rozpakowanie PrestaShop
RUN curl -s -L "https://github.com/PrestaShop/PrestaShop/releases/download/1.7.8.11/prestashop_1.7.8.11.zip" -o /tmp/prestashop.zip \
    && unzip /tmp/prestashop.zip -d /var/www/html \
    && rm /tmp/prestashop.zip \
    && chown -R www-data:www-data /var/www/html

RUN unzip -o -q /var/www/html/prestashop.zip -d /var/www/html \
    && rm -f /var/www/html/prestashop.zip \
    && chown -R www-data:www-data /var/www/html

# Automatyczna instalacja PrestaShop
RUN php /var/www/html/install/index_cli.php \
    --domain=localhost \
    --db_server=database \
    --db_name=prestashop \
    --db_user=root \
    --db_password=root1 \
    --language=pl \
    --name=HardPC \
    --country=pl \
    --firstname=John \
    --lastname=Doe \
    --password=admin1234 \
    --email=john.doe@example.com \
    --newsletter=0 \
    --send_email=0 \
    --ssl=1

# Usuń katalog instalacyjny
RUN rm -rf /var/www/html/install

# Wystaw port 80 i 443
EXPOSE 443
EXPOSE 80
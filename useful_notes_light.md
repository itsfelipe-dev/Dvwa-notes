# other
apg secure password generator


#initial settings 
sudo adduser new_username
sudo adduser new_username root
su username

# ssh settings 
sudo vim /etc/ssh/sshd_config
sudo systemctl restart sshd



#install apache and php
https://www.cyberciti.biz/faq/install-php-8-2-with-apache-on-debian-11-linux/
sudo apt install apache2



# secure install mysql 
### config settings /etc/mysql/my.cnf 
- local-infile=0
- change port 

### other settings
- mysql_secure_installation
- rename user 'root'@'localhost' to 'new_user'@'localhost';
- flush privileges;
- ALTER USER user@localhost FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 1;

### Fix auth_socket :ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password USING PASSWORD('your-password');

# setup mysql php
sudo apt install php-mysql


#Wordpress secure settings 
chown -R www-data:www-data /var/www/html/wordpress/

### Set https config
define('WP_HOME','http://localhost');
define('WP_SITEURL','http://localhost');

## Apache Settings
sudo a2enmod ssl
### php.ini
- extension=php_mysqli.dll
- sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt


#apache settings v2 
sudo a2dissite 000-default.conf
sudo a2ensite secure_site.com.conf

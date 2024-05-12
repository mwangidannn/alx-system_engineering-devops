#This is how to  Fixes bad `phpp` extensions 500 to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

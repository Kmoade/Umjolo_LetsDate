<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'umjolo');
define('DB_USER', 'root');
define('DB_PASS', '');

// App configuration
define('APP_NAME', 'Umjolo Lets Date');
define('APP_VERSION', '1.0.0');
define('APP_DEBUG', true);

// Session configuration
ini_set('session.cookie_httponly', 1);
ini_set('session.use_only_cookies', 1);

// Start session
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>

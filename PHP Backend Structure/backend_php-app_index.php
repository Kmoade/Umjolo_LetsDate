<?php
session_start();
$page_title = "Umjolo - Find Your Perfect Match";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $page_title; ?></title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <?php include 'includes/header.php'; ?>

    <section class="hero">
        <div class="container">
            <h2>Find Your Perfect Match</h2>
            <p>Umjolo connects you with like-minded individuals based on your interests, values, and preferences. Start your journey to meaningful relationships today.</p>
            <a href="auth.php?action=signup" class="btn btn-primary">Create Your Profile</a>
        </div>
    </section>

    <?php include 'includes/footer.php'; ?>
</body>
</html>

<?php

/**
 * @package   Gantry 5 Theme
 * @author    Tiger12 http://tiger12.com
 * @originalCreator  RocketTheme (Gantry Framework) 
 * @currentDeveloper  Tiger12, LLC 
 * @copyright Copyright (C) 2007 - 2022 Tiger12, LLC
 * @copyright Copyright (C) 2026 Intense Finance (BeFree Gantry modifications)
 * @license   GNU/GPLv3 or later. Derived from the Gantry 5 Hydrogen theme (GNU/GPLv2 or later).
 *
 * https://www.gnu.org/licenses/gpl-3.0.html
 */

use Gantry\Framework\Theme;

defined('ABSPATH') or die;

/*
 * WARNING: This file will be overridden during theme update. Do not change this file!
 *
 * If you want to add your custom functions, put your code into `custom/functions.php` instead!
 */

// Helium 5.6.4 marks this file PHP 5.6 compatible. Hydrogen 5.6.4 still says PHP 5.2.
// The Gantry 5.6.4 plugin requires PHP 8.1. Minimum framework version stays 5.5.
$requiredGantryVersion = '5.5';
$translationDomain = 'befree-gantry';

// Bootstrap Gantry framework or fail gracefully.
$gantry_include = locate_template('/custom/includes/gantry.php') ?: locate_template('/includes/gantry.php');
if (!$gantry_include) {
    wp_die('Gantry theme is missing a file: includes/gantry.php');
}

$gantry = require $gantry_include;
if (!$gantry) {
    return;
}

if (!$gantry->isCompatible($requiredGantryVersion)) {
    $current_theme = wp_get_theme();
    $error = sprintf(__('Please upgrade Gantry 5 Framework to v%s (or later) before using %s theme!', $translationDomain), strtoupper($requiredGantryVersion), $current_theme->get('Name'));

    if(is_admin()) {
        add_action('admin_notices', static function () use ($error) {
            echo '<div class="error"><p>' . $error . '</p></div>';
        });
    } else {
        wp_die($error);
    }
}

/** @var Theme $theme */
$theme = $gantry['theme'];

// Theme helper files that can contain useful methods or filters
$helpers = array(
    'includes/helper.php', // General helper file
);

// Require custom Functions if the file exists (allows overriding helpers).
if ($customInclude = locate_template('custom/functions.php')) {
    require $customInclude;
}

foreach ($helpers as $file) {
    if (!$filepath = locate_template($file)) {
        trigger_error(sprintf(__('Error locating %s for inclusion', $translationDomain), $file), E_USER_ERROR);
    }

    require $filepath;
}

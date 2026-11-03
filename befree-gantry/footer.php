<?php

/**
 * @package   Gantry 5 Theme
 * @author    Intense Finance https://if.finance
 * @originalCreator  RocketTheme (Gantry Framework) 
 * @currentDeveloper  Intense Finance
 * @copyright Copyright (C) 2007 - 2022 Tiger12, LLC
 * @copyright Copyright (C) 2026 Intense Finance (BeFree Gantry modifications)
 * @license   GNU/GPLv3 or later. Derived from the Gantry 5 Hydrogen theme (GNU/GPLv2 or later).
 *
 * https://www.gnu.org/licenses/gpl-3.0.html
 */

defined('ABSPATH') or die;

use Timber\Timber;

/*
 * Third party plugins that hijack the theme will call wp_footer() to get the footer template.
 * We use this to end our output buffer (started in header.php) and render into the views/page-plugin.html.twig template.
 */

$timberContext = $GLOBALS['timberContext'];

if (!isset($timberContext)) {
    throw new RuntimeException('Timber context not set in footer.');
}

$timberContext['content'] = ob_get_clean();

$templates = ['page-plugin.html.twig'];
Timber::render($templates, $timberContext);

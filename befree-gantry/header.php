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

defined('ABSPATH') or die;

use Gantry\Framework\Gantry;
use Gantry\Framework\Theme;
use Timber\Timber;

/*
 * Third party plugins that hijack the theme will call wp_head() to get the header template.
 * We use this to start our output buffer and render into the views/page-plugin.html.twig template in footer.php
 */

$gantry = Gantry::instance();

/** @var Theme $theme */
$theme  = $gantry['theme'];

// We need to render contents of <head> before plugin content gets added.
$context              = Timber::get_context();
$context['page_head'] = $theme->render('partials/page_head.html.twig', $context);

$GLOBALS['timberContext'] = $context;

ob_start();

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

use Gantry\Framework\Gantry;
use Gantry\Framework\Theme;
use Timber\Timber;

/*
 * The template to display when page is offline
 */

$gantry = Gantry::instance();

/** @var Theme $theme */
$theme  = $gantry['theme'];
$theme->setLayout('_offline', true);

// We need to render contents of <head> before plugin content gets added.
$context              = Timber::get_context();
$context['page_head'] = $theme->render('partials/page_head.html.twig', $context);

Timber::render('offline.html.twig', $context);

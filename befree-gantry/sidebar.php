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
 * The Template for displaying sidebar
 */

Timber::render(['partials/sidebar.html.twig'], isset($context) ? $context : []);

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

use Timber\Post;
use Timber\Timber;

/*
 * The template for displaying comments
 */

$context = Timber::get_context();

$post            = new Post();
$context['post'] = $post;

if (post_password_required($post)) {
    return;
}

Timber::render(['partials/comments-' . $post->ID . '.html.twig', 'partials/comments-' . $post->post_type . '.html.twig', 'partials/comments.html.twig'], $context);

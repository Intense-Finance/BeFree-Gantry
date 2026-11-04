<?php

/**
 * @package   BeFree Gantry
 * @copyright Copyright (C) 2026 Intense Finance
 * @license   GNU/GPLv3 or later. https://www.gnu.org/licenses/gpl-3.0.html
 *
 * Latest Posts slider for MetaSlider (free).
 *
 * Keeps one MetaSlider slideshow, "BeFree Latest Posts", in sync with the latest
 * published posts that have a featured image (newest first). Each slide uses the
 * post's featured image, the post title as caption and the permalink as link.
 * The slideshow is rebuilt when a post is published, updated, unpublished,
 * deleted or its featured image changes. Slides added by hand are left alone.
 *
 * Output: shortcode [befree_latest_slider] or the "Latest Posts Slider" particle.
 * Count:  filter `befree_latest_slider_count` (default 20).
 * Does nothing when MetaSlider is not active.
 */

defined('ABSPATH') or die;

if (!function_exists('befree_latest_slider_ready')) {

    function befree_latest_slider_ready()
    {
        return post_type_exists('ml-slider') && post_type_exists('ml-slide') && taxonomy_exists('ml-slider');
    }

    function befree_latest_slider_count()
    {
        return max(1, (int) apply_filters('befree_latest_slider_count', 20));
    }

    /** Slideshow settings the theme manages. Other MetaSlider settings stay editable. */
    function befree_latest_slider_settings()
    {
        return apply_filters('befree_latest_slider_settings', array(
            'type'         => 'flex',
            'width'        => 1920,
            'height'       => 800,
            'cropMultiply' => 2,
            'smartCrop'    => 'true',
            'fullWidth'    => 'true',
            'center'       => 'false',
            'effect'       => 'slide',
            'delay'        => 6000,
            'links'        => 'true',
            'navigation'   => 'true',
            'autoPlay'     => 'true',
            'hoverPause'   => 'true',
            'printCss'     => 'true',
            'printJs'      => 'true',
        ));
    }

    /** Returns the slideshow id, creating the slideshow when $create is true. */
    function befree_latest_slider_id($create = false)
    {
        $id = (int) get_option('befree_latest_slider_id');
        if ($id && get_post_type($id) === 'ml-slider' && get_post_status($id) === 'publish') {
            return $id;
        }
        if (!$create || !befree_latest_slider_ready()) {
            return 0;
        }

        if (class_exists('MetaSlider_Slideshows')) {
            $id = MetaSlider_Slideshows::create();
        } else {
            $id = wp_insert_post(array('post_title' => 'BeFree Latest Posts', 'post_status' => 'publish', 'post_type' => 'ml-slider'));
        }
        if (!$id || is_wp_error($id)) {
            return 0;
        }
        wp_update_post(array('ID' => $id, 'post_title' => 'BeFree Latest Posts'));
        $settings = get_post_meta($id, 'ml-slider_settings', true);
        $settings = array_merge(is_array($settings) ? $settings : array(), befree_latest_slider_settings(), array('title' => 'BeFree Latest Posts'));
        update_post_meta($id, 'ml-slider_settings', $settings);
        update_option('befree_latest_slider_id', $id, false);

        return $id;
    }

    /** Rebuilds the managed slides. Returns the number of slides or 0. */
    function befree_latest_slider_sync()
    {
        $slider = befree_latest_slider_id(true);
        if (!$slider) {
            return 0;
        }

        if (!term_exists((string) $slider, 'ml-slider')) {
            wp_insert_term((string) $slider, 'ml-slider');
        }
        $term = get_term_by('name', (string) $slider, 'ml-slider');
        if (!$term) {
            return 0;
        }

        $posts = get_posts(array(
            'post_type'           => 'post',
            'post_status'         => 'publish',
            'posts_per_page'      => befree_latest_slider_count(),
            'orderby'             => 'date',
            'order'               => 'DESC',
            'ignore_sticky_posts' => true,
            'suppress_filters'    => true,
            'meta_query'          => array(array('key' => '_thumbnail_id', 'compare' => 'EXISTS')),
        ));

        // Existing managed slides, keyed by source post.
        $existing = array();
        $slides = get_posts(array(
            'post_type'        => 'ml-slide',
            'post_status'      => 'any',
            'posts_per_page'   => -1,
            'suppress_filters' => true,
            'meta_key'         => '_befree_source_post',
            'tax_query'        => array(array('taxonomy' => 'ml-slider', 'field' => 'term_id', 'terms' => $term->term_id)),
        ));
        foreach ($slides as $s) {
            $existing[(int) get_post_meta($s->ID, '_befree_source_post', true)] = $s->ID;
        }

        $kept = array();
        foreach (array_values($posts) as $i => $post) {
            $image = (int) get_post_thumbnail_id($post->ID);
            if (!$image) {
                continue;
            }
            $data = array(
                'post_title'   => 'Slider ' . $slider . ' - image',
                'post_excerpt' => esc_html(get_the_title($post)),
                'post_status'  => 'publish',
                'post_type'    => 'ml-slide',
                'menu_order'   => $i,
            );
            if (isset($existing[$post->ID])) {
                $data['ID'] = $existing[$post->ID];
                $slide = wp_update_post($data);
            } else {
                $slide = wp_insert_post($data);
            }
            if (!$slide || is_wp_error($slide)) {
                continue;
            }
            set_post_thumbnail($slide, $image);
            update_post_meta($slide, 'ml-slider_type', 'image');
            update_post_meta($slide, 'ml-slider_url', get_permalink($post));
            update_post_meta($slide, 'ml-slider_new_window', '');
            update_post_meta($slide, 'ml-slider_caption_source', 'custom');
            update_post_meta($slide, '_wp_attachment_image_alt', get_the_title($post));
            update_post_meta($slide, '_befree_source_post', $post->ID);
            wp_set_post_terms($slide, array($term->term_id), 'ml-slider', false);
            $kept[$post->ID] = true;
        }

        foreach ($existing as $source => $slide) {
            if (!isset($kept[$source])) {
                wp_delete_post($slide, true);
            }
        }

        update_option('befree_latest_slider_synced', time(), false);
        return count($kept);
    }

    /** Marks the slideshow for a rebuild at the end of the request (once per request). */
    function befree_latest_slider_queue()
    {
        static $queued = false;
        if ($queued || !befree_latest_slider_ready() || !get_option('befree_latest_slider_id')) {
            return;
        }
        $queued = true;
        add_action('shutdown', 'befree_latest_slider_sync');
    }

    add_action('transition_post_status', static function ($new, $old, $post) {
        if ($post->post_type === 'post' && ($new === 'publish' || $old === 'publish')) {
            befree_latest_slider_queue();
        }
    }, 10, 3);

    add_action('before_delete_post', static function ($id) {
        if (get_post_type($id) === 'post') {
            befree_latest_slider_queue();
        }
    });

    $befree_thumb = static function ($meta_id, $object_id, $meta_key) {
        if ($meta_key === '_thumbnail_id' && get_post_type($object_id) === 'post' && get_post_status($object_id) === 'publish') {
            befree_latest_slider_queue();
        }
    };
    add_action('added_post_meta', $befree_thumb, 10, 3);
    add_action('updated_post_meta', $befree_thumb, 10, 3);
    add_action('deleted_post_meta', $befree_thumb, 10, 3);

    add_shortcode('befree_latest_slider', static function () {
        if (!befree_latest_slider_ready() || !shortcode_exists('metaslider')) {
            return '';
        }
        $id = befree_latest_slider_id();
        if (!$id) {
            befree_latest_slider_sync();
            $id = befree_latest_slider_id();
        }
        if (!$id) {
            return '';
        }

        return '<div class="befree-latest-slider">' . do_shortcode('[metaslider id="' . (int) $id . '"]') . '</div>';
    });
}

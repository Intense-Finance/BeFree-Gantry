<?php

/**
 * @package   BeFree Gantry
 * @author    Intense Finance https://if.finance
 * @copyright Copyright (C) 2026 Intense Finance
 * @license   GNU/GPLv3 or later.
 *
 * Custom CSS saved through an HTML filter can turn a child combinator
 * `>` into `&gt;`. Gantry then compiles a selector that matches nothing.
 * Decode those entities in custom CSS/SCSS before compilation.
 */

defined('ABSPATH') or die;

/**
 * Decode HTML entities that break CSS. Repeated so `&amp;gt;` becomes `>`.
 *
 * @param string $css
 * @return string
 */
function befree_gantry_decode_css_entities($css)
{
    if (strpos($css, '&') === false) {
        return $css;
    }

    for ($i = 0; $i < 3; $i++) {
        $next = strtr($css, array(
            '&amp;' => '&',
            '&gt;' => '>',
            '&lt;' => '<',
            '&quot;' => '"',
        ));
        if ($next === $css) {
            break;
        }
        $css = $next;
    }

    return $css;
}

/**
 * Rewrite custom CSS/SCSS files that still contain encoded selectors.
 *
 * Looks in the active theme's custom directory and, when present, the
 * shared Gantry custom directory used for linked sample data.
 */
function befree_gantry_decode_custom_css_files()
{
    if (!function_exists('get_stylesheet_directory')) {
        return;
    }

    $roots = array(get_stylesheet_directory() . '/custom');
    if (defined('WP_CONTENT_DIR')) {
        $slug = function_exists('get_stylesheet') ? get_stylesheet() : 'befree-gantry';
        $roots[] = WP_CONTENT_DIR . '/gantry5/' . $slug . '/custom';
    }

    foreach ($roots as $root) {
        foreach (array('scss', 'css') as $dir) {
            befree_gantry_decode_css_tree($root . '/' . $dir);
        }
    }
}

/**
 * @param string $dir
 */
function befree_gantry_decode_css_tree($dir)
{
    if (!is_dir($dir) || !is_readable($dir)) {
        return;
    }

    $items = scandir($dir);
    if ($items === false) {
        return;
    }

    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }
        $path = $dir . '/' . $item;
        if (is_dir($path)) {
            befree_gantry_decode_css_tree($path);
            continue;
        }
        $ext = strtolower(pathinfo($path, PATHINFO_EXTENSION));
        if ($ext !== 'css' && $ext !== 'scss') {
            continue;
        }
        $css = file_get_contents($path);
        if ($css === false) {
            continue;
        }
        $decoded = befree_gantry_decode_css_entities($css);
        if ($decoded !== $css && is_writable($path)) {
            file_put_contents($path, $decoded);
        }
    }
}

/**
 * Gantry SCSS compiler that restores raw selectors in custom CSS first.
 */
class BeFree_Gantry_ScssCompiler extends \Gantry\Component\Stylesheet\ScssCompiler
{
    /**
     * @param string $in
     * @param callable $variablesCallable
     * @return bool
     */
    public function needsCompile($in, $variablesCallable)
    {
        if ($in === 'custom') {
            befree_gantry_decode_custom_css_files();
        }

        return parent::needsCompile($in, $variablesCallable);
    }

    /**
     * @param string $in
     * @return bool
     */
    public function compileFile($in)
    {
        if ($in === 'custom') {
            befree_gantry_decode_custom_css_files();
        }

        return parent::compileFile($in);
    }
}

// theme.yaml names this class. Alias it into the BeFree\Gantry namespace
// without a second copy of the compiler.
class_alias('BeFree_Gantry_ScssCompiler', 'BeFree\\Gantry\\ScssCompiler');

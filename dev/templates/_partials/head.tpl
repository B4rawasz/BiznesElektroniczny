{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
{block name='head_charset'}
  <meta charset="utf-8">
{/block}

{block name='head_ie_compatibility'}
  <meta http-equiv="x-ua-compatible" content="ie=edge">
{/block}

{block name='head_mobile_optim'}
  <meta name="MobileOptimized" content="320">
  <meta name="HandheldFriendly" content="true">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{/block}

{block name='head_theme_color'}
  <meta name="theme-color" content="#ffffff">
  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#111111" media="(prefers-color-scheme: dark)">
{/block}

{block name='head_pwa'}
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
{/block}

{block name='head_seo'}
  <title>{$page.meta.title}</title>
  <meta name="description" content="{$page.meta.description}">
  <meta name="keywords" content="{$page.meta.keywords}">
  {if $page.canonical}
    <link rel="canonical" href="{$page.canonical}">
  {/if}
{/block}

{block name='head_icons'}
  <link rel="icon" type="image/png" sizes="32x32" href="{$shop_url}/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{$shop_url}/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{$shop_url}/apple-touch-icon.png">
{/block}

{block name='stylesheets'}

  {include file="_partials/stylesheets.tpl" stylesheets=$stylesheets}

  {* SUCRO główny CSS z motywu *}
  <link rel="stylesheet"
        href="{$shop_url}themes/dev/assets/css/screen.css">

  {*<link rel="stylesheet"
        href="{$shop_url}themes/dev/assets/css/custom-disable.css">*}

  {* optional: jeśli masz product-visit-counter *}
  <link rel="stylesheet"
        href="{$shop_url}themes/dev/assets/css/product-visit-counter.css">
{/block}

{block name='javascript_head'}
  {include file="_partials/javascript.tpl" javascript=$javascript.head vars=$js_custom_vars}
{/block}

{block name='hook_header'}
  {$HOOK_HEADER nofilter}
{/block}


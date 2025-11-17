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
 {*
<div class="container">
  <div class="row">
    {block name='hook_footer_before'}
      {hook h='displayFooterBefore'}
    {/block}
  </div>
</div>
<div class="footer-container">
  <div class="container">
    <div class="row">
      {block name='hook_footer'}
        {hook h='displayFooter'}
      {/block}
    </div>
    <div class="row">
      {block name='hook_footer_after'}
        {hook h='displayFooterAfter'}
      {/block}
    </div>
    <div class="row">
      <div class="col-md-12">
        <p class="text-sm-center">
          {block name='copyright_link'}
            <a href="https://www.prestashop.com" target="_blank" rel="noopener noreferrer nofollow">
              {l s='%copyright% %year% - Ecommerce software by %prestashop%' sprintf=['%prestashop%' => 'PrestaShop™', '%year%' => 'Y'|date, '%copyright%' => '©'] d='Shop.Theme.Global'}
            </a>
          {/block}
        </p>
      </div>
    </div>
  </div>
</div>
*}
<footer id="footer">

    <ul class="list-a">
        <li><i class="icon-address"></i> Hard-Pc.pl, ul. Długa 6, 24-300 Opole lubelskie</li>
        <li><i class="icon-phone"></i> 
            <a href="tel:48813070345" class="link-phone" title="zadzwoń +48 813070345">
                <span>+48</span> 813 070 345
            </a>
        </li>
        <li><i class="icon-mail"></i> 
            <a href="mailto:info@hardpc.pl" title="napisz wiadomość e-mail">info@hardpc.pl</a>
        </li>
    </ul>

    {*
    <script src="https://rep.leaselink.pl/plugin/61add4.js"></script>
    <script src="https://rep.leaselink.pl/plugin/LeaseLinkLib.min.js"></script>
    *}

    <script src="{$link->getMediaLink('_js/linki.js')|escape:'html'}"></script>
    <script src="{$link->getMediaLink('_js/autolinker.js')|escape:'html'}"></script>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            autoLinkContent(2, 10); // 1 link na frazę, maks 3 linki na stronę
        });
    </script>

    <ul>
        <li>&copy; Hard-Pc.pl. Wszelkie prawa zastrzeżone. 
            <a href="https://www.kqs.pl" title="Oprogramowanie sklepu internetowego" rel="noopener" target="_blank">
                Oprogramowanie <span>kqs</span>.store
            </a>
        </li>
        <li>Realizacja: 
            <a href="https://www.sucro.pl" title="Grafika i wdrożenie sklepu KQS.store" rel="noopener" target="_blank">
                <span>sucro</span>.pl
            </a>
        </li>
    </ul>
</footer>
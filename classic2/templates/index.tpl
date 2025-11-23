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
{extends file='page.tpl'}

    {block name='page_content_container'}
      <section id="content" class="page-home">
        {block name='page_content_top'}{/block}
        {block name='page_content'}
          {block name='hook_home'}
            {$HOOK_HOME nofilter}
            <ul class="list-i-goowno">
							<li>
								<p><i class="icon-call-center"></i> Profesjonalne doradztwo</p>
								<p>W zakresie wyboru sprzętu</p>
							</li>
							<li>
								<p><i class="icon-security"></i> Bezpieczne zakupy</p>
								<p>W pełni szyfrowane połączenie SSL</p>
							</li>
							<li>
								<p><i class="icon-return"></i> Bezproblemowe zwroty</p>
								<p>Do 14 dni bez podania przyczyny</p>
							</li>
						</ul>
            <div id="okazje">
              <div>
                <article class="box-f">
                  <header>
                    <h2>Gorąca okazja</h2>
                  </header>
                  
                    <div class="product-a">
                      <figure>
                        <a href="p20661,zestaw-ryzen-5-8400f-rtx-5060-8gb-32gb-ddr5-1tb-ssd-650w-aramis-midi-argb.html" title="Zestaw | Ryzen 5 8400F, RTX 5060 8GB, 32GB DDR5, 1TB SSD, 650W, Aramis Midi ARGB">
                          <img src="/themes/classic2/assets/img/zestaw-ryzen-7-7800x3d-rx-907_75900_k.webp" alt="Zestaw | Ryzen 5 8400F, RTX 5060 8GB, 32GB DDR5, 1TB SSD, 650W, Aramis Midi ARGB" title="Zestaw | Ryzen 5 8400F, RTX 5060 8GB, 32GB DDR5, 1TB SSD, 650W, Aramis Midi ARGB" width="500" heigh="500">
                        </a>
                      
                      </figure>
                      <h3>
                        <a href="p20835,zestaw-ryzen-7-7800x3d-rtx-5070-12gb-32gb-ddr5-1tb-ssd-stellar-5f-argb-black.html" title="Zestaw | Ryzen 7 7800X3D, RTX 5070 12GB, 32GB DDR5, 1TB SSD, Stellar 5F ARGB Black">Zestaw | Ryzen 7 7800X3D, RTX 5070 12GB, 32GB DDR5, 1TB SSD, Stellar 5F ARGB Black</a>
                      </h3>
                      <div class="attr">
										    <p class="new">Nowość</p>    
									    </div>
                      <p class="prices">
                        <span class="default promo">6 649,00 zł</span>
	                      <span class="old">8 049,00 zł</span>
                      </p>
                      <div class="omn hit-omn">Najniższa cena z 30 dni: <span>6 099,00 zł</span></div>             
                    </div>
                  
                </article>
              </div>
              {hook h='displayHome2'}
            </div>
            {hook h='displayHome3'}
          {/block}
        {/block}
      </section>
    {/block}

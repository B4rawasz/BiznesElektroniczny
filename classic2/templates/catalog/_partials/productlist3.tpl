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

{capture assign="productClasses"}{if !empty($productClass)}{$productClass}{else}col-xs-12 col-sm-6 col-md-4 col-lg-3{/if}{/capture}

{if $products}
  <style>
    #product-carousel-wrapper2 {
      position: relative;
    }
    #product-carousel2 {
      overflow: hidden;
    }
    #product-track2 {
      display: flex;
      flex-wrap: nowrap;
      transition: transform 0.5s ease-in-out;
    }
    #product-track2 > * {
      flex: 0 0 auto;
    }
    .carousel-control-prev,
    .carousel-control-next {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      z-index: 10;
      background-color: rgba(0, 0, 0, 0.5);
      color: white;
      padding: 10px;
      text-decoration: none;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .carousel-control-prev:hover,
    .carousel-control-next:hover {
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
    }
    .carousel-control-prev {
      left: 10px;
    }
    .carousel-control-next {
      right: 10px;
    }
  </style>
  
  <div id="product-carousel-wrapper2">
    <div id="product-carousel2">
      <div class="products{if !empty($cssClass)} {$cssClass}{/if}" id="product-track2">
        {foreach from=$products item="product" key="position"}
          {include file="catalog/_partials/miniatures/product.tpl" product=$product position=$position productClasses=$productClasses}
        {/foreach}
      </div>
    </div>
    
    <a class="carousel-control-prev" href="#" role="button" id="carousel-prev2">
      <span aria-hidden="true">
        <i class="material-icons">&#xE5CB;</i>
      </span>
      <span class="sr-only">{l s='Previous' d='Shop.Theme.Global'}</span>
    </a>
    <a class="carousel-control-next" href="#" role="button" id="carousel-next2">
      <span aria-hidden="true">
        <i class="material-icons">&#xE5CC;</i>
      </span>
      <span class="sr-only">{l s='Next' d='Shop.Theme.Global'}</span>
    </a>
  </div>
  
  <script>
  {literal}
    (function() {
      if (window.productCarouselInitialized2) return;
      window.productCarouselInitialized2 = true;
      
      document.addEventListener('DOMContentLoaded', function() {
        const track2 = document.getElementById('product-track2');
        const prevBtn2 = document.getElementById('carousel-prev2');
        const nextBtn2 = document.getElementById('carousel-next2');
        const wrapper2 = document.getElementById('product-carousel-wrapper2');
        
        if (!track2 || !prevBtn2 || !nextBtn2 || !wrapper2) return;
        
        let autoScrollInterval2;
        let isAnimating2 = false;
        
        function slideNext2() {
          if (isAnimating2) return;
          isAnimating2 = true;
          
          const firstProduct2 = track2.firstElementChild;
          const productWidth2 = firstProduct2.offsetWidth;
          
          track2.style.transition = 'transform 0.5s ease-in-out';
          track2.style.transform = `translateX(-${productWidth2}px)`;
          
          setTimeout(() => {
            track2.style.transition = 'none';
            track2.style.transform = 'translateX(0)';
            track2.appendChild(firstProduct2);
            isAnimating2 = false;
          }, 500);
        }
        
        function slidePrev2() {
          if (isAnimating2) return;
          isAnimating2 = true;
          
          const lastProduct2 = track2.lastElementChild;
          const productWidth2 = lastProduct2.offsetWidth;
          
          track2.style.transition = 'none';
          track2.insertBefore(lastProduct2, track2.firstElementChild);
          track2.style.transform = `translateX(-${productWidth2}px)`;
          
          setTimeout(() => {
            track2.style.transition = 'transform 0.5s ease-in-out';
            track2.style.transform = 'translateX(0)';
          }, 10);
          
          setTimeout(() => {
            isAnimating2 = false;
          }, 500);
        }
        
        nextBtn2.addEventListener('click', function(e) {
          e.preventDefault();
          slideNext2();
          resetAutoScroll2();
        });
        
        prevBtn2.addEventListener('click', function(e) {
          e.preventDefault();
          slidePrev2();
          resetAutoScroll2();
        });
        
        function startAutoScroll2() {
          stopAutoScroll2();
          autoScrollInterval2 = setInterval(slideNext2, 3000);
        }
        
        function stopAutoScroll2() {
          if (autoScrollInterval2) {
            clearInterval(autoScrollInterval2);
            autoScrollInterval2 = null;
          }
        }
        
        function resetAutoScroll2() {
          stopAutoScroll2();
          startAutoScroll2();
        }
        
        wrapper2.addEventListener('mouseenter', stopAutoScroll2);
        wrapper2.addEventListener('mouseleave', startAutoScroll2);
        
        startAutoScroll2();
      });
    })();
  {/literal}
  </script>
{/if}

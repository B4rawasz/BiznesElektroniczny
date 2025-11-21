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
    #product-carousel-wrapper {
      position: relative;
    }
    #product-carousel {
      overflow: hidden;
    }
    #product-track {
      display: flex;
      flex-wrap: nowrap;
      transition: transform 0.5s ease-in-out;
    }
    #product-track > * {
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
  
  <div id="product-carousel-wrapper">
    <div id="product-carousel">
      <div class="products{if !empty($cssClass)} {$cssClass}{/if}" id="product-track">
        {foreach from=$products item="product" key="position"}
          {include file="catalog/_partials/miniatures/product.tpl" product=$product position=$position productClasses=$productClasses}
        {/foreach}
      </div>
    </div>
    
    <a class="carousel-control-prev" href="#" role="button" id="carousel-prev">
      <span aria-hidden="true">
        <i class="material-icons">&#xE5CB;</i>
      </span>
      <span class="sr-only">{l s='Previous' d='Shop.Theme.Global'}</span>
    </a>
    <a class="carousel-control-next" href="#" role="button" id="carousel-next">
      <span aria-hidden="true">
        <i class="material-icons">&#xE5CC;</i>
      </span>
      <span class="sr-only">{l s='Next' d='Shop.Theme.Global'}</span>
    </a>
  </div>
  
  <script>
  {literal}
    (function() {
      if (window.productCarouselInitialized) return;
      window.productCarouselInitialized = true;
      
      document.addEventListener('DOMContentLoaded', function() {
        const track = document.getElementById('product-track');
        const prevBtn = document.getElementById('carousel-prev');
        const nextBtn = document.getElementById('carousel-next');
        const wrapper = document.getElementById('product-carousel-wrapper');
        
        if (!track || !prevBtn || !nextBtn) return;
        
        let autoScrollInterval;
        let isAnimating = false;
        
        function slideNext() {
          if (isAnimating) return;
          isAnimating = true;
          
          const firstProduct = track.firstElementChild;
          const productWidth = firstProduct.offsetWidth;
          
          track.style.transition = 'transform 0.5s ease-in-out';
          track.style.transform = `translateX(-${productWidth}px)`;
          
          setTimeout(() => {
            track.style.transition = 'none';
            track.style.transform = 'translateX(0)';
            track.appendChild(firstProduct);
            isAnimating = false;
          }, 500);
        }
        
        function slidePrev() {
          if (isAnimating) return;
          isAnimating = true;
          
          const lastProduct = track.lastElementChild;
          const productWidth = lastProduct.offsetWidth;
          
          track.style.transition = 'none';
          track.insertBefore(lastProduct, track.firstElementChild);
          track.style.transform = `translateX(-${productWidth}px)`;
          
          setTimeout(() => {
            track.style.transition = 'transform 0.5s ease-in-out';
            track.style.transform = 'translateX(0)';
          }, 10);
          
          setTimeout(() => {
            isAnimating = false;
          }, 500);
        }
        
        nextBtn.addEventListener('click', function(e) {
          e.preventDefault();
          slideNext();
          resetAutoScroll();
        });
        
        prevBtn.addEventListener('click', function(e) {
          e.preventDefault();
          slidePrev();
          resetAutoScroll();
        });
        
        function startAutoScroll() {
          stopAutoScroll();
          autoScrollInterval = setInterval(slideNext, 3000);
        }
        
        function stopAutoScroll() {
          if (autoScrollInterval) {
            clearInterval(autoScrollInterval);
            autoScrollInterval = null;
          }
        }
        
        function resetAutoScroll() {
          stopAutoScroll();
          startAutoScroll();
        }
        
        wrapper.addEventListener('mouseenter', stopAutoScroll);
        wrapper.addEventListener('mouseleave', startAutoScroll);
        
        startAutoScroll();
      });
    })();
  {/literal}
  </script>
{/if}

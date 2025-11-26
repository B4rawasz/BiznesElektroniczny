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
 * @author    PrestaShop SA <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}

{if $displayedFacets|count}
  <div id="search_filters">
    {block name='facets_title'}
      <p class="text-uppercase h6 hidden-sm-down">Filtruj produkty</p>
    {/block}

    {block name='facets_clearall_button'}
      {if $activeFilters|count}
        <div id="_desktop_search_filters_clear_all" class="hidden-sm-down clear-all-wrapper">
          <button data-search-url="{$clear_all_link}" class="btn btn-tertiary js-search-filters-clear-all">
            <i class="material-icons">&#xE14C;</i>
            {l s='Clear all' d='Shop.Theme.Actions'}
          </button>
        </div>
      {/if}
    {/block}

    <div id="search_filters23">
      {foreach from=$displayedFacets item="facet"}
        <section class="facet clearfix" data-type="{$facet.type}">
          {assign var=_expand_id value=10|mt_rand:100000}
          {assign var=_collapse value=true}

          {if in_array($facet.widgetType, ['radio', 'checkbox'])}
            {block name='facet_item_other'}
              <div class="facet-toggle-wrapper">
                <button class="facet-toggle-btn" data-facet-id="facet_{$_expand_id}" data-facet-label="{$facet.label}" type="button">
                  <span class="toggle-text">{if $facet.label == 'Selections'}Opcje dodatkowe{else}{$facet.label}{/if}</span>
                </button>
                <ul id="facet_{$_expand_id}" class="facet-list collapsed" style="display: none;">
                {foreach from=$facet.filters key=filter_key item="filter"}
                  {if $filter.label == 'On sale'}
                    {continue}
                  {/if}

                  <li>
                    <label class="facet-label{if $filter.active} active {/if}" for="facet_input_{$_expand_id}_{$filter_key}">
                      {if $facet.multipleSelectionAllowed}
                        <span class="custom-checkbox">
                          <input
                            id="facet_input_{$_expand_id}_{$filter_key}"
                            data-search-url="{$filter.nextEncodedFacetsURL}"
                            type="checkbox"
                            {if $filter.active}checked{/if}
                          >
                          {if isset($filter.properties.color)}
                            <span class="color" style="background-color:{$filter.properties.color}"></span>
                          {elseif isset($filter.properties.texture)}
                            <span class="color texture" style="background-image:url({$filter.properties.texture})"></span>
                          {else}
                            <span {if !$js_enabled} class="ps-shown-by-js" {/if}><i class="material-icons rtl-no-flip checkbox-checked">&#xE5CA;</i></span>
                          {/if}
                        </span>
                      {else}
                        <span class="custom-radio">
                          <input
                            id="facet_input_{$_expand_id}_{$filter_key}"
                            data-search-url="{$filter.nextEncodedFacetsURL}"
                            type="radio"
                            name="filter {$facet.label}"
                            {if $filter.active }checked{/if}
                          >
                          <span {if !$js_enabled} class="ps-shown-by-js" {/if}></span>
                        </span>
                      {/if}

                      <a
                        href="{$filter.nextEncodedFacetsURL}"
                        class="_gray-darker search-link js-search-link"
                        rel="nofollow"
                      >
                        {if $filter.label == 'Discounted'}Promocja{elseif $filter.label == 'New product'}Nowy produkt{else}{$filter.label}{/if}
                        {if $filter.magnitude and $show_quantities}
                          <span class="magnitude">({$filter.magnitude})</span>
                        {/if}
                      </a>
                    </label>
                  </li>
                {/foreach}
              </ul>
              </div>
            {/block}

          {elseif $facet.widgetType == 'slider'}
            {block name='facet_item_slider'}
              {foreach from=$facet.filters item="filter"}
                <ul id="facet_{$_expand_id}"
                  class="faceted-slider collapse{if !$_collapse} in{/if}"
                  data-slider-min="{$facet.properties.min}"
                  data-slider-max="{$facet.properties.max}"
                  data-slider-id="{$_expand_id}"
                  data-slider-values="{$filter.value|@json_encode}"
                  data-slider-unit="{$facet.properties.unit}"
                  data-slider-label="{$facet.label}"
                  data-slider-specifications="{$facet.properties.specifications|@json_encode}"
                  data-slider-encoded-url="{$filter.nextEncodedFacetsURL}"
                >
                  <li>
                    <p id="facet_label_{$_expand_id}">
                      {$filter.label}
                    </p>

                    <div id="slider-range_{$_expand_id}"></div>
                  </li>
                </ul>
              {/foreach}
            {/block}
          {/if}
        </section>
      {/foreach}
    </div>

    <script>
      (function() {
        var currentExpandedLabel = null;
        
        function initFacetToggles() {
          var toggleBtns = document.querySelectorAll('.facet-toggle-btn');
          var container = document.getElementById('facet-content-container');
          
          if (!container) return;
          
          // Clear container first
          container.innerHTML = '';
          
          toggleBtns.forEach(function(toggleBtn) {
            var newToggleBtn = toggleBtn.cloneNode(true);
            toggleBtn.parentNode.replaceChild(newToggleBtn, toggleBtn);
            
            newToggleBtn.addEventListener('click', function() {
              var facetId = this.getAttribute('data-facet-id');
              var facetLabel = this.getAttribute('data-facet-label');
              var facetList = document.getElementById(facetId);
              var isCurrentlyExpanded = currentExpandedLabel === facetLabel;
              
              container.innerHTML = '';
              currentExpandedLabel = null;
              
              if (!isCurrentlyExpanded && facetList) {
                var clonedList = facetList.cloneNode(true);
                clonedList.style.display = 'flex';
                clonedList.classList.remove('collapsed');
                container.appendChild(clonedList);
                currentExpandedLabel = facetLabel;
                
                // Add event listeners to checkboxes and radios in cloned list
                attachInputListeners(clonedList);
              }
            });
          });
          
          // After AJAX update, find and re-expand the facet by label
          if (currentExpandedLabel) {
            container.innerHTML = '';
            var targetBtn = null;
            toggleBtns.forEach(function(btn) {
              if (btn.getAttribute('data-facet-label') === currentExpandedLabel) {
                targetBtn = btn;
              }
            });
            
            if (targetBtn) {
              var facetId = targetBtn.getAttribute('data-facet-id');
              var facetList = document.getElementById(facetId);
              if (facetList) {
                var clonedList = facetList.cloneNode(true);
                clonedList.style.display = 'block';
                clonedList.classList.remove('collapsed');
                container.appendChild(clonedList);
                attachInputListeners(clonedList);
              }
            }
          }
        }
        
        function attachInputListeners(container) {
          var inputs = container.querySelectorAll('input[type="checkbox"], input[type="radio"]');
          inputs.forEach(function(input) {
            input.addEventListener('change', function() {
              var searchUrl = this.getAttribute('data-search-url');
              if (searchUrl) {
                window.location.href = searchUrl;
              }
            });
          });
        }
        
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', initFacetToggles);
        } else {
          initFacetToggles();
        }
        
        if (typeof prestashop !== 'undefined') {
          prestashop.on('updateFacets', function() {
            setTimeout(initFacetToggles, 100);
          });
        }
      })();
    </script>
  </div>
{else}
  <div id="search_filters" style="display:none;">
  </div>  
{/if}

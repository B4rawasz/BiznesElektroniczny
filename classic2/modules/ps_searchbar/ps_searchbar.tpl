<div id="search_widget" class="search-widgets" data-search-controller-url="{$search_controller_url}">
  <form method="get" action="{$search_controller_url}">
    <input 
      type="text" 
      name="s" 
      value="{$search_string}" 
      placeholder="{l s='wpisz szukaną nazwę produktu' d='Shop.Theme.Catalog'}"
      aria-label="{l s='Search' d='Shop.Theme.Catalog'}"
    >

    <i class="material-icons clear" aria-hidden="true">clear</i>
    <input type="hidden" name="controller" value="search">

<button type="submit" class="search-btn">
  <span class="search-text">Szukaj</span>
  <i class="icon-search"></i>
</button>
  </form>
</div>

{block name='header_top'}

<header id="top">

  {* LOGO *}
  <p id="logo">
    <a href="{$urls.base_url}" title="{$shop.name}">
      {renderLogo}
    </a>
  </p>

  {* SKIP-LINKS *}
  <nav id="skip">
    <ul>
      <li><a href="#nav">Skip to navigation (n)</a></li>
      <li><a href="#content">Skip to content (c)</a></li>
      <li><a href="#footer">Skip to footer (f)</a></li>
    </ul>
  </nav>

  {* GÓRNY PASEK — kontakt + social *}
  <nav id="up">
    <div>
      <ul class="list-contact">
        <li class="link-phone">
          <a href="tel:48813070345"><span>+48</span> 813 070 345</a>
        </li>
      </ul>

      <ul class="list-social">
        <li><a href="https://www.instagram.com/hardpc.pl/" target="_blank" rel="noreferrer">
          <i class="icon-instagram"></i> <span>Instagram</span>
        </a></li>

        <li><a href="https://www.facebook.com/HardPcpl/" target="_blank" rel="noreferrer">
          <i class="icon-facebook"></i> <span>Facebook</span>
        </a></li>

        <li><a href="https://www.youtube.com/HardPcTV" target="_blank" rel="noreferrer">
          <i class="icon-youtube"></i> <span>YouTube</span>
        </a></li>
      </ul>
    </div>

    <ul class="list-log">
      <li><a href="{$urls.pages.authentication}" rel="nofollow">Zaloguj się</a></li>
      <li><a href="{$urls.pages.authentication}?create_account=1" rel="nofollow">Załóż konto</a></li>
    </ul>
  </nav>

  {* MENU GŁÓWNE — SUCRO struktura *}
  <nav id="nav">
    <ul id="ps-menu">
      {hook h='displayTopMenu'}
    </ul>
  </nav>

  {* PANEL SZUKAJ + KOSZYK *}
  <div id="panel">
    <form action="{$urls.pages.search}" method="get" class="form-search">
      <p>
        <input type="text" placeholder="wpisz szukaną nazwę produktu" name="s" id="szukaj">
        <button type="submit">Szukaj</button>
      </p>
    </form>

    <div id="mKoszyk">
      {hook h='displayCart'}
    </div>
  </div>

</header>

{/block}

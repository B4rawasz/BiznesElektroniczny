{block name='header_banner'}
  <div class="header-banner">
    {hook h='displayBanner'}
  </div>
{/block}

{block name='header_nav'}
  <nav class="header-nav">
    <div class="container">
      <div class="row">
        <div class="hidden-sm-down">
          <div class="col-md-5 col-xs-12">
            {hook h='displayNav1'}
            <div class="col-lg-4 col-md-12 col-sm-12">
              <ul class="list-social">
						<li><a href="https://www.instagram.com/hardpc.pl/" title="zobacz nasz Instagram" target="_blank"
								rel="noreferrer"><i class="icon-instagram"></i></a></li>
						<li><a href="https://www.facebook.com/HardPcpl/" title="zobacz nasz Facebook" target="_blank"
								rel="noreferrer"><i class="icon-facebook"></i></a></li>
						<li><a href="https://www.youtube.com/HardPcTV" title="zobacz kanał na YouTube" target="_blank"
								rel="noreferrer"><i class="icon-youtube"></i></a></li>
					  </ul>
            </div>
          </div>
          <div class="col-md-7 right-nav">
              {hook h='displayNav2'}
          </div>
        </div>
      </div>
    </div>
  </nav>
{/block}

{block name='header_top'}
  <div class="header-top">
    <div class="container">
       <div class="row">
        <div class="col-md-2 hidden-sm-down" id="_desktop_logo">
          {if $shop.logo_details}
            {renderLogo}
          {/if}
        </div>
        <div class="header-top-right col-md-10 col-sm-12 position-static">
          {hook h='displayTop'}
        </div>
      </div>
      <div id="mobile_top_menu_wrapper" class="row hidden-md-up" style="display:none;">
        <div class="js-top-menu mobile" id="_mobile_top_menu"></div>
        <div class="js-top-menu-bottom">
          <div id="_mobile_currency_selector"></div>
          <div id="_mobile_language_selector"></div>
          <div id="_mobile_contact_link"></div>
        </div>
      </div>
    </div>
  </div>
  {hook h='displayNavFullWidth'}
{/block}

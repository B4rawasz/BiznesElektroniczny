<div id="_desktop_user_info">
  <div class="user-info">
    {if $logged}
      <a
        class="account"
        href="{$urls.pages.my_account}"
        title="{l s='View my customer account' d='Shop.Theme.Customeraccount'}"
        rel="nofollow"
      >
        <i class="icon-user"></i>
        <span class="hidden-sm-down">Twoje konto</span>
      </a>

      <a href="/content/6-program-lojalnosciowy" title="Program lojalnościowy">
        Program lojalnościowy
      </a>

      <a href="/content/7-oferty-pracy" title="Współpraca">
        Współpraca
      </a>

      <a
        class="logout hidden-sm-down"
        href="{$urls.actions.logout}"
        rel="nofollow"
      >
        <span class="hidden-sm-down">Wyloguj się</span>
      </a>

  {else}

    <a
      href="{$urls.pages.my_account}"
      title="{l s='Log in to your customer account' d='Shop.Theme.Customeraccount'}"
      rel="nofollow"
      class="login-link"
    >
      <i class="icon-user"></i>
      <span class="hidden-sm-down">Zaloguj się</span>
    </a>

    <a
      href="/logowanie?create_account=1"
      class="register-link"
      rel="nofollow"
    >Załóż konto
    </a>
  {/if}

  </div>
</div>


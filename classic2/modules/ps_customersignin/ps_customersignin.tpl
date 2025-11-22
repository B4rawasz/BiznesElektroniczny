<div id="_desktop_user_info">
  <div class="user-info">
    <a>
    <i class="icon-user"></i>
    </a>
    {if $logged}
      <a
        class="logout hidden-sm-down"
        href="{$urls.actions.logout}"
        rel="nofollow"
      >
        <i class="material-icons">&#xE7FF;</i>
        {l s='Sign out' d='Shop.Theme.Actions'}
      </a>

      <a
        class="account"
        href="{$urls.pages.my_account}"
        title="{l s='View my customer account' d='Shop.Theme.Customeraccount'}"
        rel="nofollow"
      >
        <i class="material-icons hidden-md-up logged">&#xE7FF;</i>
        <span class="hidden-sm-down">{$customerName}</span>
      </a>

  {else}

    <a
      href="{$urls.pages.my_account}"
      title="{l s='Log in to your customer account' d='Shop.Theme.Customeraccount'}"
      rel="nofollow"
      class="login-link"
    >
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


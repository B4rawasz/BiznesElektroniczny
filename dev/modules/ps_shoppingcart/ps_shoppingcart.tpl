{* SUCRO style cart for PrestaShop *}

<div id="mKoszyk">
  <p>
    <a href="{$cart_url}" rel="nofollow">

      {* Tekst "Koszyk:" i cena *}
      <span>
        Koszyk:
        <span>
          {if $cart.totals.total.value}
            {$cart.totals.total.value}
          {else}
            0,00 zł
          {/if}
        </span>
      </span>

      {* Licznik produktów *}
      <span class="no">
        <span>{$cart.products_count}</span>
      </span>

    </a>
  </p>
</div>

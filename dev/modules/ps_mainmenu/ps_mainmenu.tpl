<ul class="sucro-menu">
  {foreach from=$menu.children item=node}
    <li>
      <a href="{$node.url}" title="{$node.label}">{$node.label}</a>

      {if $node.children|count}
        <ul class="submenu">
          {foreach from=$node.children item=sub}
            <li>
              <a href="{$sub.url}" title="{$sub.label}">{$sub.label}</a>
            </li>
          {/foreach}
        </ul>
      {/if}

    </li>
  {/foreach}
</ul>

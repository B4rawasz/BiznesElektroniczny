{block name='header_top'}

<header id="top">
    <p id="logo">
        <a href="{$link->getPageLink('index')}" accesskey="h" title="Hard-Pc Sklep komputerowy">
            Hard-Pc Sklep komputerowy 
        </a>
    </p>

    <nav id="skip">
        <ul>
            <li><a href="#nav" accesskey="n">Skip to navigation (n)</a></li>
            <li><a href="#content" accesskey="c">Skip to content (c)</a></li>
            <li><a href="#footer" accesskey="f">Skip to footer (f)</a></li>
        </ul>
    </nav>

    <nav id="up">
        <div>
            <ul class="list-contact">
                <li class="link-phone">
                    <a href="tel:48813070345" title="zadzwoń +48 813 070 345 ">
                        <span>+48</span> 813 070 345
                    </a>
                </li>
            </ul>
            <ul class="list-social">
                <li>
                    <a href="https://www.instagram.com/hardpc.pl/" title="zobacz nasz Instagram" target="_blank" rel="noreferrer">
                        <i class="icon-instagram"></i> <span>Instagram</span>
                    </a>
                </li>
                <li>
                    <a href="https://www.facebook.com/HardPcpl/" title="zobacz nasz Facebook" target="_blank" rel="noreferrer">
                        <i class="icon-facebook"></i> <span>Facebook</span>
                    </a>
                </li>
                <li>
                    <a href="https://www.youtube.com/HardPcTV" title="zobacz kanał na YouTube" target="_blank" rel="noreferrer">
                        <i class="icon-youtube"></i> <span>YouTube</span>
                    </a>
                </li>
            </ul>
        </div>

        <ul class="list-log">
            <li><a href="{$link->getPageLink('login')}" rel="nofollow">Zaloguj się</a></li>
            <li><a href="{$link->getPageLink('my-account')}" rel="nofollow">Załóż konto</a></li>
        </ul>
    </nav>

    <nav id="nav" aria-label="Navigation">
        <ul>
            <li><a href="{$link->getCategoryLink(1)}" title="Myszki">Myszki</a>
                <ul>
                    <li><a href="{$link->getCategoryLink(2)}" title="Myszki bezprzewodowe">Myszki bezprzewodowe</a></li>
                    <li><a href="{$link->getCategoryLink(3)}" title="Myszki przewodowe">Myszki przewodowe</a></li>
                    <li><a href="{$link->getCategoryLink(4)}" title="Akcesoria do myszek">Akcesoria do myszek</a></li>
                </ul>
            </li>
            <li><a href="{$link->getCategoryLink(5)}" title="Monitory">Monitory</a>
                <ul>
                    <li><a href="{$link->getCategoryLink(6)}" title="Monitory">Monitory</a></li>
                    <li><a href="{$link->getCategoryLink(7)}" title="Akcesoria do monitorów">Akcesoria do monitorów</a></li>
                    <li><a href="{$link->getCategoryLink(8)}" title="Uchwyty na monitor">Uchwyty na monitor</a></li>
                </ul>
            </li>
            <li><a href="{$link->getCategoryLink(9)}" title="Klawiatury">Klawiatury</a>
                <ul>
                    <li><a href="{$link->getCategoryLink(10)}" title="Klawiatury mechaniczne">Klawiatury mechaniczne</a></li>
                    <li><a href="{$link->getCategoryLink(11)}" title="Klawiatury magnetyczne">Klawiatury magnetyczne</a></li>
                    <li><a href="{$link->getCategoryLink(12)}" title="Akcesoria do klawiatur">Akcesoria do klawiatur</a></li>
                </ul>
            </li>
            <li><a href="{$link->getCategoryLink(13)}" title="Słuchawki">Słuchawki</a>
                <ul>
                    <li><a href="{$link->getCategoryLink(14)}" title="Słuchawki nauszne/wokółuszne">Słuchawki nauszne/wokółuszne</a></li>
                    <li><a href="{$link->getCategoryLink(15)}" title="Słuchawki dokanałowe/douszne">Słuchawki dokanałowe/douszne</a></li>
                    <li><a href="{$link->getCategoryLink(16)}" title="Słuchawki sportowe">Słuchawki sportowe</a></li>
                </ul>
            </li>
        </ul>
    </nav>

    <div id="panel">
        <form action="{$link->getPageLink('search')}" method="get" class="form-search">
            <input type="hidden" name="d" value="szukaj">
            <p>
                <input type="text" placeholder="wpisz szukaną nazwę produktu" name="szukaj" id="szukaj" onkeyup="podpowiedz(this.value);">
                <button type="submit" aria-label="szukaj">Szukaj</button>
            </p>
            <div id="podpowiedzi" style="visibility: hidden; position: absolute; width: 500px"></div>
        </form>

        {*
        <div id="mKoszyk">
           <p><a href="{$link->getPageLink('cart')}" title="Twój koszyk">
                <span>Koszyk: <span>{if $cart.total_price_tax_incl > 0}{convertPrice price=$cart.total_price_tax_incl}{else}0,00 zł{/if}</span></span> 
                <span class="no">({$cart.products|count})</span></a></p>
        </div>
        *}
    </div>
</header>

{/block}

function flip(rid) {
    current = (document.getElementById(rid).style.display == 'none') ? 'block' : 'none';
    document.getElementById(rid).style.display = current;
}
function bon() {
    var b = document.getElementById('bon_rabatowy')
      , bv = (b ? b.value : '');
    if (bv.length > 0)
        self.location.href = 'koszyk.php?akcja=bon&bon=' + bv.replace(/[^a-z0-9]+/i, '');
}
function wybierzGratis(g) {
    self.location.href = 'koszyk.php?akcja=gratis&gratis=' + g;
}
function osoba_firma() {
    zosoba = document.getElementById('zaznaczOsoba');
    dosoba = document.getElementById('daneOsoba');
    dfirma = document.getElementById('daneFirma');
    if (zosoba.checked) {
        dosoba.style.display = 'block';
        dfirma.style.display = 'none';
    } else {
        dosoba.style.display = 'none';
        dfirma.style.display = 'block';
    }
}
function ustaw_adres_dostawy(ad_id, ad_licz) {
    var ad_p, ad_i;
    for (ad_i = 1; ad_i <= ad_licz; ad_i++) {
        ad_p = document.getElementById('adres_' + ad_i);
        if (ad_i == ad_id) {
            ad_p.style.display = 'block';
        } else {
            ad_p.style.display = 'none';
        }
    }
}
function przewiniecie(start, elid) {
    if (start < document.getElementById(elid).offsetTop - (window.innerHeight / 4))
        setTimeout(function() {
            window.scrollBy(0, 10);
            przewiniecie(start + 10, elid);
        }, 5);
}
function zapiszKoszyk(pole, wartosc) {
    var post = 'pole=' + encodeURIComponent(pole) + '&wartosc=' + encodeURIComponent(wartosc)
      , p = otworzPolaczenie();
    p.open('post', 'koszyk.php', true);
    p.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    p.send(post);
}
function koszyk_przypomnienie(wartosc) {
    var post = 'kontakt=' + encodeURIComponent(wartosc)
      , p = otworzPolaczenie();
    p.open('post', 'koszyk.php?akcja=kontakt', true);
    p.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    p.send(post);
}
function PoliczRate(k, id, w) {
    var c = k > 0 ? k : document.getElementById('cena_raty').value;
    okno('https://wniosek.eraty.pl/symulator/oblicz/numerSklepu/' + id + '/wariantSklepu/' + w + '/typProduktu/0/wartoscTowarow/' + c, 'eRaty', 660, 760, 0, 1, 1, 0);
}
function mbankraty(k, id) {
    var c = k > 0 ? k : document.getElementById('cena_raty').value;
    okno('http://www.mbank.net.pl/mraty_1/?sprzedawca=' + id + '&kwota=' + c, 'mRaty', 850, 650, 0, 1, 1, 0);
}
function PoliczRateCA(k, id) {
    var c = k > 0 ? k : document.getElementById('cena_raty').value;
    okno('https://ewniosek.credit-agricole.pl/eWniosek/simulator.jsp?PARAM_TYPE=RAT&PARAM_PROFILE=' + id + '&PARAM_CREDIT_AMOUNT=' + c, 'CARaty', 800, 800, 0, 1, 1, 0);
}
function sprawdzMail(ema) {
    wz = /^[0-9a-zA-Z._-]+@[0-9a-zA-Z.-]+\.[a-zA-Z]{2,10}$/;
    spr = (wz.test(ema) == true && ema != '');
    if (spr) {
        return true;
    } else {
        return false;
    }
}
function pokaz() {
    if (document.getElementById('kup_na_firme')) {
        if (document.rejestracja.firma.checked) {
            flip('na_firme');
            flip('teleadr_firma');
        }
    }
}
function dane_firmy() {
    fr = document.rejestracja;
    if (fr.adres_firmy.checked) {
        fr.firma_ulica.value = fr.ulica.value;
        fr.firma_dom.value = fr.dom.value;
        fr.firma_kod_pocztowy.value = fr.kod_pocztowy.value;
        fr.firma_miasto.value = fr.miasto.value;
        fr.firma_wojewodztwo.value = fr.wojewodztwo.value;
        fr.firma_telefon.value = fr.telefon.value;
    }
}
function aPoleWartosc(aPole) {
    if (aPole.type != 'select-one') {
        if (aPole.length > 1) {
            for (r = 0; r < aPole.length; r++) {
                if (aPole[r].checked) {
                    return aPole[r].value;
                }
            }
        } else {
            if (aPole.checked) {
                return aPole.value;
            }
        }
        return 0;
    } else {
        return aPole.options[aPole.selectedIndex].value;
    }
}
function aCena(pID, tpl, formID) {
    var URL, formularz = ustawFormularz(formID), polaczenie = otworzPolaczenie(), aLicz = 0, aOpcje = aProduktyN[pID], aUstawione = '';
    for (klucz in aOpcje) {
        aPole = formularz['atrybuty_' + pID + '[' + aOpcje[klucz] + ']'];
        if (aPole) {
            aWartosc = aPoleWartosc(aPole);
            aUstawione += aOpcje[klucz] + '-' + aWartosc + ',';
            aLicz++;
        }
    }
    ;URL = 'acena.php?pID=' + pID + '&aUstawione=' + aUstawione + '&szablon=' + tpl;
    polaczenie.open('get', URL);
    polaczenie.onreadystatechange = function() {
        if (polaczenie.readyState == 4)
            document.getElementById('cena_' + pID + '_' + formID).innerHTML = polaczenie.responseText;
    }
    ;
    polaczenie.send(null);
}
function aMagazyn(oID, pID, divUstaw, oIDustaw, tpl, formID) {
    var URL, formularz = ustawFormularz(formID), polaczenie = otworzPolaczenie(), aLicz = 0;
    aOpcje = aProdukty[pID],
    aUstawione = '';
    for (klucz in aOpcje) {
        aPole = formularz['atrybuty_' + pID + '[' + aOpcje[klucz] + ']'];
        aWartosc = aPoleWartosc(aPole);
        if (aWartosc != 0) {
            aUstawione += aOpcje[klucz] + '-' + aWartosc + ',';
            aLicz++;
        }
        ;if (oID == aOpcje[klucz]) {
            break;
        }
    }
    ;URL = 'amagazyn.php?pID=' + pID + '&oIDustaw=' + oIDustaw + '&aUstawione=' + aUstawione + '&szablon=' + tpl + '&formID=' + formID;
    polaczenie.open('get', URL);
    polaczenie.onreadystatechange = function() {
        if (polaczenie.readyState == 4)
            document.getElementById(divUstaw).innerHTML = polaczenie.responseText;
    }
    ;
    polaczenie.send(null);
}
function aStan(pID, formID) {
    var URL, formularz = ustawFormularz(formID), polaczenie = otworzPolaczenie(), aLicz = 0, aOpcje = aProdukty[pID], aUstawione = '';
    for (klucz in aOpcje) {
        aPole = formularz['atrybuty_' + pID + '[' + aOpcje[klucz] + ']'];
        aWartosc = aPoleWartosc(aPole);
        if (aWartosc != 0) {
            aUstawione += aOpcje[klucz] + '-' + aWartosc + ',';
            aLicz++;
        } else {
            break;
        }
    }
    ;if (aLicz == aOpcje.length) {
        URL = 'astan.php?pID=' + pID + '&aUstawione=' + aUstawione;
        polaczenie.open('get', URL);
        polaczenie.onreadystatechange = function() {
            var odpStan, poleLimit = formularz['limit_' + pID], poleDostepnaIlosc = document.getElementById('dostepna_ilosc_' + pID), poleIloscWartosc, poleIlosc = formularz['ile_' + pID];
            if (poleIlosc) {
                poleIloscWartosc = poleIlosc.value;
            }
            ;if (polaczenie.readyState == 4) {
                odpStan = polaczenie.responseText;
                if (!isNaN(odpStan)) {
                    poleLimit.value = odpStan;
                    if (poleDostepnaIlosc) {
                        poleDostepnaIlosc.innerHTML = odpStan
                    }
                    ;if (poleIlosc && !isNaN(poleIloscWartosc)) {
                        if (odpStan - poleIloscWartosc < 0) {
                            poleIlosc.value = odpStan;
                        }
                    }
                }
            }
        }
        ;
        polaczenie.send(null);
    }
}
function sprawdzFormularz(pID, formID) {
    var formularz = ustawFormularz(formID), klucz, aOpcje, aPole, aPole_ile, aWartosc, aSp, czerwonyAlarm = 0, pTab = isNaN(pID) ? pID : [pID];
    for (p in pTab) {
        aSp = 1;
        aPole_ile = formularz['ile_' + pTab[p]];
        if (aPole_ile) {
            if (aPole_ile.type == 'checkbox') {
                if (aPole_ile.checked != true) {
                    aSp = 0;
                }
            } else {
                if (aPole_ile.value == 0) {
                    aSp = 0;
                }
            }
        }
        ;if (aSp == 1) {
            aOpcje = aProduktyN[pTab[p]];
            for (klucz in aOpcje) {
                aPole = formularz['atrybuty_' + pTab[p] + '[' + aOpcje[klucz] + ']'];
                if (aPole) {
                    aWartosc = aPoleWartosc(aPole);
                    if (aWartosc == 0) {
                        czerwonyAlarm = 1;
                        break;
                    }
                }
            }
        }
    }
    if (czerwonyAlarm == 1) {
        alert('Najpierw wybierz atrybuty');
    }
    return czerwonyAlarm;
}
function ustawFormularz(formID) {
    var formularze = ['listaZakupow', 'pokrewne', 'pokategorie', 'kupioneRazem', 'listaZakupowPromocje', 'listaZakupowBestsellery', 'listaZakupowWyprzedaze'];
    return document.forms[formularze[formID]];
}
function upKoszyk(pID, formID) {
    var pIloscPole, pIlosc, czerwonyAlarm = 0, formularz = ustawFormularz(formID);
    formularz.koszyk.value = pID;
    pIloscPole = formularz['ile_' + pID];
    if (pIloscPole) {
        pIlosc = pIloscPole.value;
        pIlosc = pIlosc.replace(',', '.');
        if ((pIlosc) <= 0) {
            czerwonyAlarm = 1;
            alert('Wpisz ilość');
        }
    }
    ;return czerwonyAlarm
}
function kontrola(pID, formID) {
    var formularz = ustawFormularz(formID), pStanPole, pStan, czerwonyAlarm = 0, pIloscPole, pIlosc;
    pStanPole = formularz['limit_' + pID];
    pStan = parseFloat(pStanPole.value);
    pIloscPole = formularz['ile_' + pID];
    if (pIloscPole) {
        pIlosc = parseFloat(pIloscPole.value);
        if (pIlosc > pStan) {
            pIloscPole.value = pStan;
            czerwonyAlarm = 1;
            alert('Niestety nie posiadamy takiej ilości tego produktu');
        }
    }
    ;return czerwonyAlarm;
}
function pbo(ile, limit, uchwyt) {
    if (parseFloat(ile) > limit) {
        uchwyt.value = limit;
        alert('Niestety nie posiadamy takiej ilości tego produktu');
    }
}
function koszyk_dodaj(formID) {
    var p, pID, klucz, aOpcje, aPole, aPoleNazwa, aWartosc, pUchwyt, pName, pDane = [], n = 0, formularz = ustawFormularz(formID);
    pDane[n] = 'koszyk=' + formularz['koszyk'].value;
    n++;
    if (formularz['tablicaZbiorcza']) {
        pDane[n] = 'tablicaZbiorcza=' + formularz['tablicaZbiorcza'].value;
        n++;
    }
    for (pole in formularz) {
        if (formularz[pole]) {
            pUchwyt = formularz[pole];
            if (pUchwyt.name) {
                pName = pUchwyt.name;
                if (pName.length > 0) {
                    if (pName.search('ile_') >= 0) {
                        if (pUchwyt.type == 'text' || pUchwyt.type == 'number') {
                            pDane[n] = pName + '=' + encodeURIComponent(pUchwyt.value);
                            n++;
                        } else if (pUchwyt.type == 'checkbox') {
                            if (pUchwyt.checked == true) {
                                pDane[n] = pName + '=' + encodeURIComponent(pUchwyt.value);
                                n++;
                            }
                        }
                    } else if (pName.search('atrybuty_') >= 0) {
                        if (pUchwyt.type == 'text') {
                            pDane[n] = pName + '=' + encodeURIComponent(pUchwyt.value);
                            n++;
                        } else if (pUchwyt.type == 'select-one') {
                            pDane[n] = pName + '=' + encodeURIComponent(pUchwyt.options[pUchwyt.selectedIndex].value);
                            n++;
                        }
                    }
                }
            }
        }
    }
    if (aProduktyRadio.length > 0) {
        for (pID in aProduktyRadio) {
            aOpcje = aProduktyRadio[pID];
            for (klucz in aOpcje) {
                aPoleNazwa = 'atrybuty_' + pID + '[' + aOpcje[klucz] + ']';
                aPole = formularz[aPoleNazwa];
                if (aPole) {
                    aWartosc = aPoleWartosc(aPole);
                    if (aWartosc != 0) {
                        pDane[n] = aPoleNazwa + '=' + aWartosc;
                        n++;
                    }
                }
            }
        }
    }
    p = otworzPolaczenie();
    p.open('post', 'koszyk.php?box=1', true);
    p.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    p.onreadystatechange = function() {
        if (p.readyState == 4)
            kqs_box(p.responseText, 500, 'auto', 1);
    }
    ;
    p.send(pDane.join('&'));
    setTimeout(koszyk_licznik, 500);
    setTimeout(koszyk_menu, 500);
    return 1;
}
function koszyk_usun(koszyk_id) {
    var p = otworzPolaczenie();
    p.open('get', 'koszyk.php?akcja=usun&k_id=' + koszyk_id, true);
    p.send(null);
    setTimeout(koszyk_licznik, 200);
    setTimeout(koszyk_menu, 200);
    return 1;
}
function koszyk_akcja(opcja) {
    var p, pkn = document.getElementById('koszyk_nazwa'), nazwa = (pkn ? pkn.value : ''), pkid = document.getElementById('koszyk_id'), kid = (pkid ? pkid.options[pkid.selectedIndex].value : ''), post = 'nazwa=' + encodeURIComponent(nazwa) + '&kid=' + encodeURIComponent(kid);
    if (opcja == 1 || opcja == 2) {
        p = otworzPolaczenie();
        p.open('post', 'koszyk.php?akcja=kolekcja&opcja=' + opcja, true);
        p.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        p.onreadystatechange = function() {
            if (p.readyState == 4)
                document.getElementById('koszyk_kolekcja').innerHTML = p.responseText;
        }
        ;
        p.send(post);
    } else if (opcja == 3) {
        if (kid != '' && kid != 0) {
            self.location.href = 'index.php?d=koszyk&kid=' + encodeURIComponent(kid);
        }
    }
}
function koszyk_licznik() {
    var p, pole = document.getElementById('koszyk_licznik');
    if (pole) {
        p = otworzPolaczenie();
        p.open('get', 'koszyk.php?akcja=licznik');
        p.onreadystatechange = function() {
            if (p.readyState == 4)
                pole.innerHTML = p.responseText;
        }
        ;
        p.send(null);
    }
}
function koszyk_menu() {
    var p = otworzPolaczenie();
    p.open('get', 'koszyk.php?akcja=menu');
    p.onreadystatechange = function() {
        if (p.readyState == 4)
            document.getElementById('mKoszyk').innerHTML = p.responseText;
    }
    ;
    p.send(null);
}
function otworzPolaczenie() {
    var httpRequest;
    if (window.XMLHttpRequest && !(window.ActiveXObject)) {
        httpRequest = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
    }
    ;return httpRequest;
}
function filtrujWartosc(n_window, n_docelement, n_body) {
    var n_result = n_window ? n_window : 0;
    if (n_docelement && (!n_result || (n_result > n_docelement))) {
        n_result = n_docelement;
    }
    ;return n_body && (!n_result || (n_result > n_body)) ? n_body : n_result;
}
function f_clientWidth() {
    return filtrujWartosc(window.innerWidth ? window.innerWidth : 0, document.documentElement ? document.documentElement.clientWidth : 0, document.body ? document.body.clientWidth : 0);
}
function f_clientHeight() {
    return filtrujWartosc(window.innerHeight ? window.innerHeight : 0, document.documentElement ? document.documentElement.clientHeight : 0, document.body ? document.body.clientHeight : 0);
}
function f_scrollTop() {
    return filtrujWartosc(window.pageYOffset ? window.pageYOffset : 0, document.documentElement ? document.documentElement.scrollTop : 0, document.body ? document.body.scrollTop : 0);
}
var glo = 0, setout, wcz;
function galeria_box(g, o, ow, oh, np, pid, bid) {
    if (glo == 0) {
        glo = 1;
        var obmw = ow
          , obmh = oh
          , wspob = ow / oh
          , bl = 0
          , bg = 0
          , bw = f_clientWidth()
          , bh = f_clientHeight()
          , okmaxw = bw - 40
          , okmaxh = bh - 160
          , wspok = okmaxw / okmaxh
          , polgal = otworzPolaczenie()
          , pn = document.getElementById('galeria-nazwa')
          , pgt = document.getElementById('kqs-tlo')
          , pg = document.getElementById('galeria-box')
          , po = document.getElementById('galeria-obraz')
          , pm = document.getElementById('galeria-miniatury')
          , ol = document.getElementById('loading-image');
        if (oh > okmaxh || ow > okmaxw) {
            if (wspok > 1) {
                if (wspob > 1) {
                    if (wspob < wspok) {
                        obmh = okmaxh;
                        obmw = Math.round(okmaxh * wspob);
                    } else {
                        obmw = okmaxw;
                        obmh = Math.round(okmaxw / wspob);
                    }
                } else {
                    obmh = okmaxh;
                    obmw = Math.round(okmaxh * wspob);
                }
            } else {
                if (wspob > 1) {
                    obmw = okmaxw;
                    obmh = Math.round(okmaxw / wspob);
                } else {
                    if (wspob > wspok) {
                        obmw = okmaxw;
                        obmh = Math.round(okmaxw / wspob);
                    } else {
                        obmh = okmaxh;
                        obmw = Math.round(okmaxh * wspob);
                    }
                }
            }
        }
        bg = (bh - obmh - 120) / 2;
        bl = (bw - obmw - 20) / 2;
        po.style.maxHeight = obmh + 'px';
        po.style.maxWidth = obmw + 'px';
        ol.src = 'galerie/' + (bid > 0 ? 'blog' : o.substr(0, 1)) + '/' + o;
        po.src = 'img/loading.gif';
        pn.innerHTML = np;
        polgal.open('get', 'galeria_box.php?g=' + g + '&p=' + pid + '&b=' + bid);
        polgal.onreadystatechange = function() {
            if (polgal.readyState == 4)
                pm.innerHTML = polgal.responseText;
        }
        ;
        polgal.send(null);
        pgt.style.display = 'block';
        pgt.style.opacity = 0.2;
        pg.style.display = 'block';
        pg.style.opacity = 1;
        wcz = setInterval(function() {
            if (galeria_rozmiar(obmw, obmh, bg, bl) && ol.complete) {
                po.src = 'galerie/' + (bid > 0 ? 'blog' : o.substr(0, 1)) + '/' + o;
                clearInterval(wcz);
                glo = 0;
            }
        }, 100);
    }
}
function galeria_rozmiar(wsz, wwy, wto, wle) {
    eln = document.getElementById('galeria-nazwa');
    elp = document.getElementById('galeria-podklad');
    elb = document.getElementById('galeria-box');
    asz = parseInt(elp.style.width);
    rsz = Math.round(asz - wsz);
    dsz = Math.abs(rsz) > 50 ? 5 : 1;
    awy = parseInt(elp.style.height);
    rwy = Math.round(awy - wwy);
    dwy = Math.abs(rwy) > 50 ? 5 : 1;
    ato = parseInt(elb.offsetTop);
    rto = Math.round(ato - wto);
    dto = Math.abs(rto) > 50 ? 5 : 1;
    ale = parseInt(elb.offsetLeft);
    rle = Math.round(ale - wle);
    dle = Math.abs(rle) > 50 ? 5 : 1;
    usz = rsz > 0 ? (asz - dsz) : (asz + dsz);
    uwy = rwy > 0 ? (awy - dwy) : (awy + dwy);
    uto = rto > 0 ? (ato - dto) : (ato + dto);
    ule = rle > 0 ? (ale - dle) : (ale + dle);
    akc = (rsz != 0 || rwy != 0 || rto != 0 || rle != 0) ? true : false;
    if (akc) {
        if (rsz != 0) {
            elp.style.width = usz + 'px';
            eln.style.width = usz + 'px';
        }
        if (rwy != 0)
            elp.style.height = uwy + 'px';
        if (rto != 0)
            elb.style.top = uto + 'px';
        if (rle != 0)
            elb.style.left = ule + 'px';
        setout = setTimeout(function() {
            galeria_rozmiar(wsz, wwy, wto, wle)
        }, 1);
    } else {
        return true;
    }
}
function galeria_atrybuty(pid) {
    var URL, formularz = ustawFormularz(0), p = otworzPolaczenie(), aLicz = 0, aOpcje = aProduktyN[pid], aUstawione = '';
    for (klucz in aOpcje) {
        aPole = formularz['atrybuty_' + pid + '[' + aOpcje[klucz] + ']'];
        if (aPole) {
            aWartosc = aPoleWartosc(aPole);
            aUstawione += aOpcje[klucz] + '-' + aWartosc + ',';
            aLicz++;
        }
    }
    ;URL = 'galeria_box.php?p=' + pid + '&aUstawione=' + aUstawione;
    p.open('get', URL);
    p.onreadystatechange = function() {
        var res;
        if (p.readyState == 4) {
            res = p.responseText;
            if (res.length > 0)
                document.getElementById('galeria_podglad').innerHTML = res;
        }
    }
    ;
    p.send(null);
}
function galeria_podglad(pid, g) {
    var URL = 'galeria_box.php?g=' + g + '&p=' + pid + '&podglad=1'
      , p = otworzPolaczenie();
    p.open('get', URL);
    p.onreadystatechange = function() {
        var res;
        if (p.readyState == 4) {
            res = p.responseText;
            if (res.length > 0)
                document.getElementById('galeria_podglad').innerHTML = res;
        }
    }
    ;
    p.send(null);
}
function kqs_box(oz, ow, oh, ot) {
    var tlo, box, zaw, obmw = ow == 'auto' ? 100 : (ow > 0 ? ow : f_clientWidth()), obmh = oh == 'auto' ? 100 : (oh > 0 ? oh : f_clientHeight()), wspob = obmw / obmh, bw = f_clientWidth(), bh = f_clientHeight(), okmaxw = bw - 40, okmaxh = bh - 100, wspok = okmaxw / okmaxh;
    if (obmh > okmaxh || obmw > okmaxw) {
        if (wspok > 1) {
            if (wspob > 1) {
                if (wspob < wspok) {
                    obmh = okmaxh;
                    obmw = Math.round(okmaxh * wspob);
                } else {
                    obmw = okmaxw;
                    obmh = Math.round(okmaxw / wspob);
                }
            } else {
                obmh = okmaxh;
                obmw = Math.round(okmaxh * wspob);
            }
        } else {
            if (wspob > 1) {
                obmw = okmaxw;
                obmh = Math.round(okmaxw / wspob);
            } else {
                if (wspob > wspok) {
                    obmw = okmaxw;
                    obmh = Math.round(okmaxw / wspob);
                } else {
                    obmh = okmaxh;
                    obmw = Math.round(okmaxh * wspob);
                }
            }
        }
    }
    tlo = document.getElementById('kqs-tlo');
    box_tlo = document.getElementById('kqs-box-tlo');
    box = document.getElementById('kqs-box');
    zaw = document.getElementById('kqs-box-zawartosc');
    if (ow == 'auto') {
        box.style.width = 'auto';
        box.style.maxWidth = 'auto';
    } else {
        box.style.maxWidth = obmw + 'px';
    }
    if (oh == 'auto') {
        box.style.height = 'auto';
        box.style.maxHeight = 'auto';
    } else {
        box.style.maxHeight = obmh + 'px';
    }
    if (oz != '')
        zaw.innerHTML = oz;
    if (ot == 1) {
        tlo.style.display = 'block';
        tlo.style.opacity = 0.2;
    }
    box_tlo.style.display = 'table';
    box_tlo.style.opacity = 1;
}
function kqs_off() {
    var t = document.getElementById('kqs-tlo')
      , g = document.getElementById('galeria-box')
      , b = document.getElementById('kqs-box-tlo');
    t.style.opacity = 0;
    g.style.opacity = 0;
    b.style.opacity = 0;
    setTimeout(function() {
        t.style.display = 'none';
        g.style.display = 'none';
        b.style.display = 'none';
    }, 500);
    setTimeout(function() {
        document.getElementById('kqs-box-zawartosc').innerHTML = '';
    }, 600);
}
function kqs_cookies() {
    var URL = 'interaktywne.php?akcja=cookies'
      , p = otworzPolaczenie();
    p.open('get', URL);
    p.onreadystatechange = function() {
        var res;
        if (p.readyState == 4) {
            res = p.responseText;
            if (res.length > 0)
                kqs_box(res, 600, 'auto', 1);
        }
    }
    ;
    p.send(null);
}
function kqs_cookies_off() {
    setCookie('cookie_okno', 1, 365);
    kqs_off();
}
function porownaj(id, a) {
    var ak, i, p, pp, pid, URL;
    ak = a == '1' ? 'dodaj' : 'usun';
    for (i = 0; i < id.length; i++) {
        pid = id[i];
        pp = document.getElementById('por_' + pid);
        if (pp) {
            if (a == '1') {
                pp.innerHTML = '<a rel="nofollow" target="_blank" href="porownywarka.php" onclick="porownaj_okno(); return false">Porównaj wybrane</a>';
            } else {
                pp.innerHTML = '<a rel="nofollow" href="porownywarka.php?akcja=dodaj&amp;id=' + pid + '" onclick="porownaj([' + pid + '],1); return false;">Dodaj do porównania</a>';
            }
        }
    }
    p = otworzPolaczenie();
    URL = 'porownywarka.php?akcja=' + ak + '&js=1&id=' + id.join();
    p.open('get', URL);
    p.onreadystatechange = function() {
        if (p.readyState == 4)
            document.getElementById('mPorownywarka').innerHTML = p.responseText;
    }
    ;
    p.send(null);
}
;function porownaj_okno() {
    okno('porownywarka.php', 'porownywarka', 950, 600, 0, 1, 1, 1);
}
;function przechowaj(pid, a) {
    var p, json, ak = a == '1' ? 'dodaj' : 'usun', pp = document.getElementById('prz_' + pid), pm = document.getElementById('mPrzechowalnia'), pl = document.getElementById('przechowalnia_licznik'), URL = 'interaktywne.php?d=przechowalnia&akcja=' + ak + '&id=' + pid;
    p = otworzPolaczenie();
    p.open('get', URL);
    p.onreadystatechange = function() {
        if (p.readyState == 4) {
            json = JSON.parse(p.responseText);
            if (pm)
                pm.innerHTML = json.szablon;
            if (pp)
                pp.innerHTML = json.przycisk;
            if (pl)
                pl.innerHTML = json.licznik;
        }
    }
    ;
    p.send(null);
}
function przepiszWartosc(idin, idout) {
    var idinx = document.getElementById(idin);
    var idouty = document.getElementById(idout);
    idouty.value = idinx.value;
}
;function cechy_grupy(opId) {
    var cgOpWsz = cgOpcje[0];
    var cgOpWy = cgOpcje[opId];
    var znWar, klu1, klu2, oPole, sPole;
    for (klu1 in cgOpWsz) {
        oPole = document.getElementById('tr_co_' + cgOpWsz[klu1]);
        sPole = document.getElementById('sel_co_' + cgOpWsz[klu1]);
        if (oPole) {
            znWar = 0;
            for (klu2 in cgOpWy) {
                if (cgOpWy[klu2] == cgOpWsz[klu1]) {
                    znWar = 1;
                }
            }
            if (znWar == 1) {
                oPole.style.display = 'table-row';
            } else {
                oPole.style.display = 'none';
                sPole.value = 0;
            }
        }
    }
}
function wczytajKategorie(kid, did) {
    var URL = 'interaktywne.php?d=kategorie&kid=' + kid + '&did=' + did
      , polaczenie = otworzPolaczenie();
    polaczenie.open('get', URL);
    polaczenie.onreadystatechange = function() {
        if (polaczenie.readyState == 4)
            document.getElementById(did).innerHTML = polaczenie.responseText;
    }
    ;
    polaczenie.send(null);
}
function podpowiedz(fraza) {
    var x = 0
      , y = 0
      , podp = document.getElementById('podpowiedzi')
      , inpodp = document.getElementById('input-szukaj')
      , URL = 'interaktywne.php?d=wyszukiwarka&fraza=' + fraza
      , polaczenie = otworzPolaczenie();
    if (fraza.length >= 2) {
        if (inpodp) {
            x = inpodp.offsetLeft;
            y = inpodp.offsetTop + inpodp.offsetHeight;
        }
        polaczenie.open('get', URL);
        polaczenie.onreadystatechange = function() {
            if (polaczenie.readyState == 4)
                podp.innerHTML = polaczenie.responseText;
            podp.style.top = y + 'px';
            podp.style.left = x + 'px';
            podp.style.visibility = 'visible';
        }
        ;
        polaczenie.send(null);
    } else {
        podp.style.visibility = 'hidden';
    }
}
function podpowiedz_off() {
    document.getElementById('podpowiedzi').style.visibility = 'hidden';
}
function okno(u, n, sz, w, st, sc, r, m) {
    window.open(u, n, 'width=' + sz + ',height=' + w + ',status=' + st + ',scrollbars=' + sc + ',resizable=' + r + ',menubar=' + m);
}
function formularz_platnosci_submit() {
    document.getElementById('przycisk_platnosci').style.display = 'none';
    document.getElementById('przekierowanie_platnosci').style.display = 'inline';
    document.formularz_platnosci.submit();
}
function setCookie(cn, cv, cex) {
    var d = new Date();
    d.setTime(d.getTime() + (cex * 24 * 60 * 60 * 1000));
    var ex = 'expires=' + d.toUTCString();
    document.cookie = cn + '=' + cv + '; SameSite=Lax; ' + ex;
}
function setCookieAccept() {
    setCookie('cookie_okno', 1, 365);
    document.getElementById('kqs-cookie').style.display = 'none';
}
if (!navigator.cookieEnabled) {
    alert('Aby korzystać z serwisu, należy włączyć akceptację plików cookie. Po zmianie ustawień należy ponownie uruchomić przeglądarkę.');
}
function rwd_rollMenu(cla) {
    var cur, ele = document.getElementsByClassName(cla);
    if (ele) {
        ele[0].style.display = (ele[0].style.display == 'block') ? 'none' : 'block';
    }
}

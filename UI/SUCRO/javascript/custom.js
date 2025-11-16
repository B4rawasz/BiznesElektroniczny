$(document).ready(function() {

    var 
      html_tag = $('html'),
      body_tag = $('body'),
      root_id = $('#root'),
      nav_id = $('#nav'),
      top_id = $('#top'),
      up_id = $('#up'),
      nav_sections = $('#nav-sections'),
  
      email_tag = $(document.getElementsByClassName('email')),
      featured_a = $('#featured'),
      form_children = $('form > *:not(fieldset), fieldset > *'),
      form_footer = $('.form-footer'),
      input_tag = $(':input'),
      link_discount = $('.link-discount'),
      list_blog = $('.list-blog'),
      slide_a = $('.slide-a'),
      slide_gallery = $('.slide-gallery'),
      slide_products = $('.slide-products'),
      slide_promo = $('.slide-promo'),
      loadRes = function (u, c, i) {
          if (html_tag.is('.' + i)) {
              c();
              return true;
          }
          var s = document.createElement('script');
          s.src = u;
          s.async = true;
          s.onload = c;
          document.body.appendChild(s);
          html_tag.not('.' + i).addClass(i);
          return true;
      }
    ;
  
    var Default = {
          utils : {
              links : function(){
                  $('a[rel*=external]').on('click',function(e){
                      e.preventDefault();
                      window.open($(this).attr('href'));						  
                  }).attr('rel','external noopener');
              },
              nav : function() {
                  top_id.append('<p id="menu-icon"></p>').find('#menu-icon').on('click',function(){ html_tag.toggleClass('menu-active'); return false; });
                  root_id.append('<nav id="mobile"></nav><div id="shadow"></div>');
                  $('#shadow').on('click',function(){ html_tag.toggleClass('menu-active'); return false; });
                  nav_id.each(function(){ $(this).find('ul:first').clone().addClass('clone').appendTo('#mobile'); });
                  $('#mobile > ul ul').each(function(){ $(this).parent('li:first').addClass('sub').append('<span class="toggle"></span>').children('.toggle').on('click',function (){ $(this).parent().toggleClass('toggle'); }); });
                  up_id.find('.link-btn').clone().removeClass('link-btn').addClass('link').appendTo('#mobile');
                  up_id.children('ul').clone().removeClass('list-log').addClass('log').appendTo('#mobile');
                  up_id.find('.list-social').clone().appendTo('#mobile');
                  root_id.append('<nav id="mobile-bar"><ul></ul></nav>');
                  top_id.each(function(){ $(this).find('#logo a').clone().addClass('home').appendTo('#mobile-bar ul').wrap('<li></li>'); });
                  $('#mobile-bar ul').append('<li><a href="./" class="search">Search</a></li>').find('.search').on('click',function(){ html_tag.toggleClass('search-active'); return false; });
                //  top_id.each(function(){ $(this).find('.storebox a').clone().addClass('store').appendTo('#mobile-bar ul').wrap('<li></li>'); });
                  top_id.each(function(){ $(this).find('#mKoszyk a').clone().addClass('cart').appendTo('#mobile-bar ul').wrap('<li></li>'); });
                  top_id.each(function(){ $(this).find('#up .list-log li:first a').clone().addClass('user').appendTo('#mobile-bar ul').wrap('<li></li>'); });
                  link_discount.on('click',function(){ html_tag.toggleClass('discount-active'); return false; });
                  $('#nav > ul > li').find('ul a').each(function(){ $(this).parents('#nav > ul > li').addClass('sub'); });
                  $('#nav > ul > li').find('ul ul').each(function(){ $(this).parents('#nav > ul > li').addClass('wide'); });
                  // $('.list-commentssss').each(function(){ if($(this).children('li').length>5){ $(this).parent().addClass('is-more'); } });
                  // $('.module-review .link-btn a').on('click',function(){ html_tag.toggleClass('comments-more'); return false; });
              },
              forms : function() {
                  form_children.each(function(k,v){ $(v).css('z-index',(form_children.length-k)); });
                  form_footer.find('table input').after('<div class="input"></div>');
              },
              slider : function() {
                  featured_a.each(function(){
                      var f = function(el){
                          el.find('.owl-item').each(function(){ if($(this).is('.active')){ $(this).attr('focusable',true).attr('aria-hidden',false).find('a, iframe').removeAttr('tabindex'); } else {$(this).attr('focusable',false).attr('aria-hidden',true).find('a, iframe').attr('tabindex',-1); } });
                          el.parents('.is-slider:first').find('.owl-nav button').each(function(){ if($(this).is('.disabled')){$(this).attr('tabindex',-1).attr('focusable',false).attr('aria-hidden',true); } else {$(this).removeAttr('tabindex').attr('focusable',true).attr('aria-hidden',false); } });
                          el.parents('.is-slider:first').find('.owl-dots button').each(function(){ if($(this).is('.active')){$(this).attr('aria-pressed',true); } else {$(this).attr('aria-pressed',false); } });
                          return false;
                      };
                      if($(this).children().length>1){ 
                          $(this).addClass('is-slider').wrapInner('<div class="inner owl-carousel"></div>').children('.inner').children().wrap('<div class="item"></div>');
                          $(this).children('.inner').owlCarousel({ loop: true, autoplay: true, autoplayTimeout: 3000, autoplaySpeed: 1000, nav: true, dots: true, margin: 0, items: 1, autoplayHoverPause: true, onInitialized: function(){ f($(this.$element)); }, onTranslated: function(){ f($(this.$element)); }, });
                      }
                  });
                  slide_a.each(function(){
                      var f = function(el){
                          el.find('.owl-item').each(function(){ if($(this).is('.active')){ $(this).attr('focusable',true).attr('aria-hidden',false).find('a, iframe').removeAttr('tabindex'); } else {$(this).attr('focusable',false).attr('aria-hidden',true).find('a, iframe').attr('tabindex',-1); } });
                          el.parents('.is-slider:first').find('.owl-nav button').each(function(){ if($(this).is('.disabled')){$(this).attr('tabindex',-1).attr('focusable',false).attr('aria-hidden',true); } else {$(this).removeAttr('tabindex').attr('focusable',true).attr('aria-hidden',false); } });
                          el.parents('.is-slider:first').find('.owl-dots button').each(function(){ if($(this).is('.active')){$(this).attr('aria-pressed',true); } else {$(this).attr('aria-pressed',false); } });
                          return false;
                      };
                      if($(this).children().length>0){ 
                          $(this).addClass('is-slider').find('.product-a').wrapAll('<div class="inner owl-carousel"></div>').children('.inner').children().wrap('<div class="item"></div>');
                          $(this).find('.inner').owlCarousel({ loop: false, rewind: true, autoplay: true, autoplayTimeout: 3000, autoplaySpeed: 1000, nav: true, dots: true, margin: 12, items: 7, autoplayHoverPause: true, onInitialized: function(){ f($(this.$element)); }, onTranslated: function(){ f($(this.$element)); },
                              responsive: { 0: { items: 1 }, 500: { items: 2 }, 600: { items: 3 }, 1000: { items: 5 }, 1400: { items: 7 } }
                          });
                      }
                  });
                  slide_gallery.each(function(){
                      var f = function(el){
                          el.find('.owl-item').each(function(){ if($(this).is('.active')){ $(this).attr('focusable',true).attr('aria-hidden',false).find('a, iframe').removeAttr('tabindex'); } else {$(this).attr('focusable',false).attr('aria-hidden',true).find('a, iframe').attr('tabindex',-1); } });
                          el.parents('.is-slider:first').find('.owl-nav button').each(function(){ if($(this).is('.disabled')){$(this).attr('tabindex',-1).attr('focusable',false).attr('aria-hidden',true); } else {$(this).removeAttr('tabindex').attr('focusable',true).attr('aria-hidden',false); } });
                          el.parents('.is-slider:first').find('.owl-dots button').each(function(){ if($(this).is('.active')){$(this).attr('aria-pressed',true); } else {$(this).attr('aria-pressed',false); } });
                          return false;
                      };
                      if($(this).children().length>0){ 
                          $(this).addClass('is-slider').find('li').wrapAll('<div class="inner owl-carousel"></div>').children('.inner').children().wrap('<div class="item"></div>');
                          $(this).find('.inner').owlCarousel({ loop: false, rewind: true, autoplay: true, autoplayTimeout: 3000, autoplaySpeed: 1000, nav: true, dots: true, margin: 14, items: 4, autoplayHoverPause: true, onInitialized: function(){ f($(this.$element)); }, onTranslated: function(){ f($(this.$element)); },
                              responsive: { 0: { items: 1 }, 500: { items: 2 }, 600: { items: 3 }, 1000: { items: 4 }, 1400: { items: 4 } }
                          });
                      }
                  });
                  slide_promo.each(function(){
                      var f = function(el){
                          el.find('.owl-item').each(function(){ if($(this).is('.active')){ $(this).attr('focusable',true).attr('aria-hidden',false).find('a, iframe').removeAttr('tabindex'); } else {$(this).attr('focusable',false).attr('aria-hidden',true).find('a, iframe').attr('tabindex',-1); } });
                          el.parents('.is-slider:first').find('.owl-nav button').each(function(){ if($(this).is('.disabled')){$(this).attr('tabindex',-1).attr('focusable',false).attr('aria-hidden',true); } else {$(this).removeAttr('tabindex').attr('focusable',true).attr('aria-hidden',false); } });
                          el.parents('.is-slider:first').find('.owl-dots button').each(function(){ if($(this).is('.active')){$(this).attr('aria-pressed',true); } else {$(this).attr('aria-pressed',false); } });
                          return false;
                      };
                      if($(this).children().length>0){ 
                          $(this).addClass('is-slider').find('.product-a').wrapAll('<div class="inner owl-carousel"></div>').children('.inner').children().wrap('<div class="item"></div>');
                          $(this).find('.inner').owlCarousel({ loop: false, rewind: true, autoplay: true, autoplayTimeout: 3000, autoplaySpeed: 1000, nav: true, dots: true, margin: 12, items: 4, autoplayHoverPause: true, onInitialized: function(){ f($(this.$element)); }, onTranslated: function(){ f($(this.$element)); },
                              responsive: { 0: { items: 1 }, 500: { items: 2 }, 600: { items: 3 }, 1000: { items: 2 }, 1400: { items: 4 } }
                          });
                      }
                  });
                  slide_products.each(function(){
                      var f = function(el){
                          el.find('.owl-item').each(function(){ if($(this).is('.active')){ $(this).attr('focusable',true).attr('aria-hidden',false).find('a, iframe').removeAttr('tabindex'); } else {$(this).attr('focusable',false).attr('aria-hidden',true).find('a, iframe').attr('tabindex',-1); } });
                          el.parents('.is-slider:first').find('.owl-nav button').each(function(){ if($(this).is('.disabled')){$(this).attr('tabindex',-1).attr('focusable',false).attr('aria-hidden',true); } else {$(this).removeAttr('tabindex').attr('focusable',true).attr('aria-hidden',false); } });
                          el.parents('.is-slider:first').find('.owl-dots button').each(function(){ if($(this).is('.active')){$(this).attr('aria-pressed',true); } else {$(this).attr('aria-pressed',false); } });
                          return false;
                      };
                      if($(this).children().length>0){ 
                          $(this).addClass('is-slider').find('.product-a').wrapAll('<div class="inner owl-carousel"></div>').children('.inner').children().wrap('<div class="item"></div>');
                          $(this).find('.inner').owlCarousel({ loop: false, rewind: true, autoplay: true, autoplayTimeout: 3000, autoplaySpeed: 1000, nav: true, dots: true, margin: 12, items: 6, autoplayHoverPause: true, onInitialized: function(){ f($(this.$element)); }, onTranslated: function(){ f($(this.$element)); },
                              responsive: { 0: { items: 1 }, 500: { items: 2 }, 600: { items: 3 }, 1000: { items: 5 }, 1400: { items: 6 } }
                          });
                      }
                  });
              },			
              gallery : function(){
                  $('.gallery-thumbs a').on("click", function (e) {e.preventDefault();});
                  $('.gallery-thumbs figure a').each(function(){$(this).removeAttr("data-fancybox");});
                  $('.main-pic').slick({ infinite: false, slidesToShow: 1, slidesToScroll: 1, arrows: false, fade: false, asNavFor: '.gallery-thumbs' });
                  $('.gallery-thumbs').slick({ infinite: false, arrows: true, slidesToShow: 4, slidesToScroll: 1, asNavFor: '.main-pic', dots: false, centerMode: false, focusOnSelect: true, responsive: [{breakpoint: 1450, settings: {slidesToShow: 4}},{breakpoint: 1200, settings: {slidesToShow: 4,slidesToScroll: 1,}},{breakpoint: 700, settings: {slidesToShow: 3,slidesToScroll: 1,}},{breakpoint: 500, settings: {slidesToShow: 2,slidesToScroll: 1,}},],    });
              },
              filters : function(){
                  if ( $('.filters-box').length ) {
                       $('.filters-box').appendTo('.module-filters .inner');
                       $('#filters .item').each(function(i){
                            $('.filters-box form').append('<div class="item" id="srt'+i+'"></div>');
                            $(this)
                            .find('.name')
                            .appendTo('#srt'+i)
                            .attr('divid', i)
                            .addClass('name--js');
                            $(this)
                            .find('.box-attrs')
                            .appendTo('.module-filters')
                            .attr('boxid', i);
                       });
                       $('.activeFilters').prependTo('.filters-box');
                  }
                  $('.name--js').click(function(e){
                       e.preventDefault();
                       var id = $(this).attr('divid');
                       $('.name').removeClass('active');
                       $('.box-attrs').slideUp();
                       if ( $('.box-attrs[boxid="'+id+'"]').css('display') != 'block' )
                       {
                            $(this).addClass('active');
                            $('.box-attrs[boxid="'+id+'"]')
                            .slideDown();
                       }
                       else
                       {
                            $('.box-attrs[boxid="'+id+'"]')
                            .slideUp();
                       }
                  });
              },
              mask : function(){
                  $('input[name="telefon"]').inputmask('999-999-999');
                  $('input[name="kod_pocztowy"]').inputmask('99-999');
              },
              codes : function(){
                  var productPrice = window.cena_nieformatowana;
                  var productPriceFloat = parseFloat(productPrice);
                  if(productPriceFloat >= 300 && productPriceFloat <= 9259 ) {
                      $('.pops').addClass('show');
                  }
                  $(".points-a").each(function(){
                  //      <div class="prices" rawPrice="{CENA_NIEFORMATOWANA}">
                      var unitsForPoint = 100.0;
                       console.log(".point-qyt");
                       $(".point-qty",this).html("100");
                       var sRawPrice = $(this).attr("rawPrice");
                       var price = parseInt(sRawPrice);
                       var pointQty = parseInt(price/unitsForPoint);
                  //      console.log(price);
                  //      console.log(pointQty);
                       $(".point-qty",this).html(pointQty);
                   });
                  if ( $('.shipping span').length ) {
                      var availbility = $('.shipping span').html();
                      var isUnavailable = false;
                      if (availbility.indexOf('48h') > -1) {
                          $('.shipping span').addClass('a');
                      }
                      else if(availbility.indexOf('24h') > -1)
                           { $('.shipping span').addClass('a'); }
                      else if(availbility.indexOf('5 dni') > -1)
                           { $('.shipping span').addClass('a'); }
                      else if(availbility.indexOf('7 dni') > -1)
                           { $('.shipping span').addClass('a'); }
                      else if(availbility.indexOf('niedostępny') > -1)
                           { $('.shipping span').addClass('b');
                           isUnavailable  = true;
                      } else { }
                      $('.availability button').on('click', function() {
                          if(isUnavailable == true) {
                              if(!confirm("Produkt, który chcesz dodać do koszyka jest aktualnie niedostępny. Jeśli zdecydujesz się złożyć zamówienie, zostaniesz poinformowany przez obsługę sklepu o możliwie najszybszej dostawie"))  
                          return false;
                          } 
                        });
                  }
                  
              },
              otherA: function () {
                  var loadOtherA = function (id) {
                      loadRes('https://rep.leaselink.pl/plugin/61add4.js', function() { }, 'other-A'); },
                      dt = decodeURIComponent(document.location.hash.substring(1));
                  setTimeout(loadOtherA, 5000);
              },
              otherB: function () {
                  var loadOtherB = function (id) {
                      loadRes('https://rep.leaselink.pl/plugin/LeaseLinkLib.min.js', function() { }, 'other-B'); },
                      dt = decodeURIComponent(document.location.hash.substring(1));
                  setTimeout(loadOtherB, 5000);
              },
              misc : function(){
                  $('.page-navigation ul').scrollLeft(3000);
                  list_blog.find('li').each(function(){ $(this).find(':header a').clone().addClass('clone').prependTo($(this)); });
                  var singleStar = function () { return $('<span class="star"><span class="fill"></span></span>'); };
                  $('[data-val][data-of]').wrapInner('<span class="label"></span>').prepend('<span class="rating"></span>').each(function () {var i = 1, ss, rateContainer = $(this), maxStars = $(this).attr('data-of'), rate = rateContainer.data('val').toString().split('.'); while (i <= maxStars) {ss = singleStar(); rateContainer.children('.rating').append(ss); if (i <= rate[0]) {ss.children().css('width', '100%'); } else if (+rate[1] > 0) {ss.children().css('width', (rate[1] * (rate[1].length === 1 ? 10 : 1)) + '%'); rate[1] = 0; } i = i + 1; } });
                  var gn;
                  $('.amount-a input').wrap('<span class="number"></span>').parent('.number').append('<a class="plus-one">+</a><a class="minus-one">-</a>');
                  $('.amount-a a[class$="-one"]').on('click',function(){gn = $(this).parent().children('input');if($(this).attr('class').split('-')[0]=='minus'){if((gn.val()*1) >= 2){gn.val((gn.val()*1)-1);}} else gn.val((gn.val()*1)+1); $(this).closest('form').submit(); return false;});
                  $('.module-blog .nav-blog').scrollToFixed({ limit: function() { return $('.module-pattern').offset().top - $('.nav-blog').outerHeight() - 20; }, });
                  $('.module-categories').mCustomScrollbar({ axis:"x", theme:"light-3", advanced:{autoExpandHorizontalScroll:true}, scrollbarPosition:"outside" });
                  $('.rating-a a[href^="#"][href!="#"], .link-btn a[href^="#"][href!="#"], .link-a a[href^="#"][href!="#"], #mobile a[href^="#"][href!="#"]').on('click',function(e){ 
                      $('html, body').animate({'scrollTop': $($(this).attr('href')).offset().top - $('.steps-a').outerHeight() + 10+'px'});
                      if($(this).attr('href') != '#root' && $(this).attr('href') != '#top'){
                          document.location.hash = '!'+$(this).attr('href').split('#')[1];
                      }
                      e.preventDefault(); 
                  });
                  nav_sections.scrollToFixed({ });
                  $('[id^="section-"]').addClass('is-anchor').each(function(){
                      var self = $(this);
                      $(this).append('<div class="anchor" id="'+$(this).attr('id')+'"></div>');
                      $(this).attr('data-id',$(this).attr('id'));
                      $(this).waypoint(function(direction){ 
                          if (direction === 'down'){
                              nav_sections.children('ul').children('li.active').removeClass('active');
                              nav_sections.find('a[href="#'+ self.attr('data-id') +'"]').parent().addClass('active');	
                          }					
                      }, { offset: 32 });
                      $(this).waypoint(function(direction){ 
                          if (direction === 'up'){
                              nav_sections.children('ul').children('li.active').removeClass('active');
                              nav_sections.find('a[href="#'+ self.attr('data-id') +'"]').parent().addClass('active');	
                          }					
                      }, { offset: -self.innerHeight() +55+'px' }); 
                  });
                  $('.steps-a a[href^="#"][href!="#"], #mobile a[href^="#"][href!="#"]').on('click',function(e){ 
                      $('html, body').animate({'scrollTop': $($(this).attr('href')).offset().top - $(this).outerHeight() + 10+'px'});
                      html_tag.removeClass('menu-active');
                      $('.sub').removeClass('toggle');
                      if($(this).attr('href') != '#root' && $(this).attr('href') != '#top'){
                          document.location.hash = '!'+$(this).attr('href').split('#')[1];
                      }
                      e.preventDefault(); 
                  });
                  $(window).scroll(function(){
                      if($(window).scrollTop() <= 0){
                          if ('pushState' in history)
                              history.pushState("",document.title,window.location.pathname+window.location.search);
                          else{
                              window.location.hash = '';
                              document.body.scrollTop = document.body.scrollTop;
                              document.body.scrollLeft = document.body.scrollLeft;
                          }
                          $('#nav-sections .active').removeClass('active');
                          $('#nav-sections li:first-child').addClass('active');
                      }
                  });
  
                  $('#valuation').find('input[type="checkbox"]').each(function(){ $(this).removeAttr('name'); })
                  $('#valuation').find('input[type="checkbox"]').each(function(){ $(this).on('click',function(){ if ($(this).is("[name]")) { $(this).removeAttr('name'); } else { $(this).attr('name', 'zastosowanie[]'); } }); })
                  $('#valuation').each(function(){ 
                      {
  
                          const form = document.querySelector('#valuation');
                          const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
  
                          form.setAttribute('novalidate', true);
  
                          const displayFieldError = function(elem) {
                              const fieldRow = elem.closest('.form-row');
                              const fieldError = fieldRow.querySelector('.field-error');
                              // if (fieldError === null) {
                              //     const errorText = elem.dataset.error;
                              //     const divError = document.createElement('div');
                              //     divError.classList.add('field-error');
                              //     divError.innerText = errorText;
                              //     fieldRow.appendChild(divError);
                              // }
                          };
  
                          const hideFieldError = function(elem) {
                              const fieldRow = elem.closest('.form-row');
                              const fieldError = fieldRow.querySelector('.field-error');
                              if (fieldError !== null) {
                                  fieldError.remove();
                              }
                          };
  
                          [...inputs].forEach(elem => {
                              elem.addEventListener('input', function() {
                                  if (!this.checkValidity()) {
                                      this.classList.add('error');
                                  } else {
                                      this.classList.remove('error');
                                      hideFieldError(this);
                                  }
                              });
  
                              if (elem.type === "checkbox") {
                                  elem.addEventListener('click', function() {
                                      const formRow = this.closest('.form-row');
                                      if (this.checked) {
                                          this.classList.remove('error');
                                          hideFieldError(this);
                                      } else {
                                          
                                          this.classList.add('error');
                                      }
                                  });
                              }
                          });
  
                          const checkFieldsErrors = function(elements) {
                              let fieldsAreValid = true;
  
                              [...elements].forEach(elem => {
                                  if (elem.checkValidity()) {
                                      hideFieldError(elem);
                                      elem.classList.remove('error');
                                  } else {
                                      displayFieldError(elem);
                                      elem.classList.add('error');
                                      fieldsAreValid = false;
                                  }
                              });
  
                              return fieldsAreValid;
                          };
  
                          form.addEventListener('submit', function(e) {
                              e.preventDefault();
  
                              if (checkFieldsErrors(inputs)) {
                                  const elements = form.querySelectorAll('input:not(:disabled), textarea:not(:disabled), select:not(:disabled), input:not(:checked)');
  
                                  const dataToSend = new FormData();
                                  [...elements].forEach(el => dataToSend.append(el.name, el.value));
                                  // [...elements].forEach(el => dataToSend.append(el.name, el.value));
  
                                  const url = form.getAttribute('action');
                                  const method = form.getAttribute('method');
  
                                  const submit = form.querySelector('[type="submit"]');
                                  submit.disabled = true;
                                  submit.classList.add('element-is-busy');
  
                                  fetch(url, {
                                      method: method.toUpperCase(),
                                      body: dataToSend
                                  })
                                  .then(ret => ret.json())
                                  .then(ret => {
                                      submit.disabled = false;
                                      submit.classList.remove('element-is-busy');
  
                                      if (ret.errors) {
                                          ret.errors.map(function(el) {
                                              return '[name="'+el+'"]'
                                          });
                                          const selector = ret.errors.join(',');
                                          checkFieldsErrors(form.querySelectorAll(sekector));
  
                                      } else {
                                          if (ret.status === 'ok') {
                                              // window.scrollTo(0,0);
                                              const div = document.createElement('div');
                                              div.classList.add('form-send-success');
  
                                              div.innerHTML = '<strong>Wiadomość została wysłana</strong><span>Dziękujemy za kontakt. Postaramy się odpowiedzieć jak najszybciej</span>';
                                              form.parentElement.insertBefore(div, form);
                                              form.remove();
                                          }
  
                                          if (ret.status === 'error') {
                                              const div = document.createElement('div');
                                              div.classList.add('send-error');
                                              div.innerText = 'Wysłanie wiadomości się nie powiodło';
                                          }
                                      }
                                  }).catch(_ => {
                                      submit.disabled = false;
                                      submit.classList.remove('element-is-busy');
                                  });
                              }
                          });
                      }
                  });
              },
          }
    };
  
    Default.utils.links();
    Default.utils.nav();
    Default.utils.forms();
    Default.utils.slider();
    Default.utils.gallery();
    Default.utils.filters();
    Default.utils.mask();
    Default.utils.misc();
    Default.utils.otherA();
    Default.utils.otherB();
    Default.utils.codes();
  
  });
  
  $.fancybox.defaults.hash = false;
  
  jQuery.event.special.touchstart = {
      setup: function( _, ns, handle ) {
          this.addEventListener("touchstart", handle, { passive: !ns.includes("noPreventDefault") });
      }
  };
  jQuery.event.special.touchmove = {
      setup: function( _, ns, handle ) {
          this.addEventListener("touchmove", handle, { passive: !ns.includes("noPreventDefault") });
      }
  };
  jQuery.event.special.wheel = {
      setup: function( _, ns, handle ){
          this.addEventListener("wheel", handle, { passive: true });
      }
  };
  jQuery.event.special.mousewheel = {
      setup: function( _, ns, handle ){
          this.addEventListener("mousewheel", handle, { passive: true });
      }
  };
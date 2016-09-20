/* Copyright (c) The Internet Movie Database, 2010 */if(document.getElementById('quicksearch')){var host_prefix='';if(typeof $("#nb_search").attr("data-hostname")!='undefined'){host_prefix='http://'+$("#nb_search").attr("data-hostname");}
var advancedSearchOption=document.createElement("option");advancedSearchOption.className="advancedSearch";advancedSearchOption.setAttribute("value",host_prefix+"/search/");advancedSearchOption.innerHTML="Advanced Search &raquo;";document.getElementById('quicksearch').appendChild(advancedSearchOption);}
function jumpMenu(selObj){var myIndex=selObj.selectedIndex;var myObj=selObj[myIndex];if("advancedSearch"==selObj[myIndex].className){selObj.selectedIndex=0;document.location=myObj.value;}}
function navBuilder(test){var NavBuilder={};test.onmouseover=function(){if(true==buttonHistory){mouseOver();}else{inTimeOut=setTimeout(mouseOver,100);}}
function mouseOver(){buttonHistory=true;clearTimeout(outTimeOut);for(var i=0;i<test.parentNode.childNodes.length;i++){if("nb_home"==test.className){if("nb_home"==test.parentNode.childNodes[i].className){test.parentNode.childNodes[i].className="nb_home";}else{test.parentNode.childNodes[i].className="";}
test.className="nb_home";}else if("nb_home"!=test.parentNode.childNodes[i].className){test.parentNode.childNodes[i].className="";test.className="nb_hover";}}}
test.onmouseout=function(){outTimeOut=setTimeout(mouseOut,500);clearTimeout(inTimeOut);};function mouseOut(){buttonHistory=false;if("nb_home"!=test.className){test.className="";}}
return NavBuilder;}
var buttonHistory=false;var outTimeOut;var inTimeOut;function triggerNav(){var mainNav=document.getElementById("main_nav");if(mainNav!=null){for(var i=0;i<mainNav.childNodes.length;i++){if("LI"==mainNav.childNodes[i].tagName){var test=mainNav.childNodes[i];var newButton=new navBuilder(test);}}}}
triggerNav();if(jQuery){(function($){$(document).ready(function(){"use strict";$('#navbar-query').click(function(){var i=new Image();i.src='/rg/search-box/click/images/b.gif?cb='+Math.random();return 1;});$('#navbar-submit-button').click(function(){var i=new Image();i.src='/rg/search-button/click/images/b.gif?cb='+Math.random();return 1;});$('#consumer_main_nav, #consumer_user_nav, #nb_extra_nav').children('.css_nav_item').removeClass('css_nav_item').addClass('js_nav_item');if($('#megaMenu').length){window.navMouseEnterTimers={};window.navMouseOutTimers={};$('.js_nav_item, .sub_nav').hover(function(){var menuItem=this;if((window.navMouseOutItem&&(window.navMouseOutItem.id==menuItem.id))||window.navMouseOutTimers[menuItem.id]){clearTimeout(window.navMouseOutTimers[menuItem.id]);window.navMouseOutTimers[menuItem.id]=undefined;}
window.navMouseEnterTimers[menuItem.id]=setTimeout(function(){window.navMouseOutItem=undefined;clearTimeout(window.navMouseOutTimers[menuItem.id]);window.navMouseOutTimers[menuItem.id]=undefined;$(menuItem).children('.sub_nav').css('display','block');},350);},function(){var menuItem=window.navMouseOutItem=this;clearTimeout(window.navMouseEnterTimers[menuItem.id]);window.navMouseEnterTimers[menuItem.id]=undefined;window.navMouseOutTimers[menuItem.id]=setTimeout(function(){$(menuItem).children('.sub_nav').css('display','none');},350);});}else{$('.js_nav_item').hover(function(){window.menuItem=this;window.displayMenu=setTimeout(function(){$(menuItem).children('.sub_nav').css('display','block');},100);},function(){try{clearTimeout(displayMenu);}catch(e){};$(this).children('.sub_nav').css('display','none');});}
if(!('isTouchDevice'in window)){window.isTouchDevice=function(){return(('ontouchstart'in window)||(navigator.maxTouchPoints>0)||(navigator.mxMaxTouchPoints>0));};}
if(isTouchDevice()){$('.js_nav_item > a').click(function(e){if($(this).data('hovered')==='true'){$(this).data('hovered',null);return true;}else{$(this).parent().trigger('mouseenter').siblings().trigger('mouseout');$('.js_nav_item > a').each(function(){$(this).data('hovered',null);});$(this).data('hovered','true');e.preventDefault();}});}
var navbarImagesLoaded=false,navbar_ads={impressionEvents:{title:{trackers:null},name:{trackers:null}},clickEvents:{title:{trackers:null},name:{trackers:null}},secondaryClickEvents:{title:{trackers:null},name:{trackers:null}},impressionHandler:function(impressionSet){if(!impressionSet.fired&&impressionSet.trackers){for(var i=0;i<impressionSet.trackers.length;i++){(new Image()).src=impressionSet.trackers[i].url;}}
impressionSet.fired=true;},readTrackersFromData:function(navbarAdSlotsData,menuName,trackingData,trackingName){if(navbarAdSlotsData[menuName].clickTrackers){trackingData.clickEvents[trackingName].trackers=navbarAdSlotsData[menuName].clickTrackers;}
if(navbarAdSlotsData[menuName].impressionTrackers){trackingData.impressionEvents[trackingName].trackers=navbarAdSlotsData[menuName].impressionTrackers;}
if(navbarAdSlotsData[menuName].secondaryClickTrackers){trackingData.secondaryClickEvents[trackingName].trackers=navbarAdSlotsData[menuName].secondaryClickTrackers;}}};if(window.imdb.navbarAdSlots&&window.location.protocol!=="https:"){navbar_ads.readTrackersFromData(window.imdb.navbarAdSlots,'titleAd',navbar_ads,'title');navbar_ads.readTrackersFromData(window.imdb.navbarAdSlots,'nameAd',navbar_ads,'name');}
var loadNavbarImages=function(){if(navbarImagesLoaded){return;}
if(window.imdb.navbarAdSlots){var data=window.imdb.navbarAdSlots;for(var i in data){var $slot=$('#'+i);if('rank'in data[i]){if(window.location.protocol==="https:"){data[i].imageUrl=data[i].imageUrl.replace("http://ia.media-imdb.com","https://images-na.ssl-images-amazon.com");}
if(i==='titleAd'){$('#titleAd').css('background','url('+data[i].imageUrl+')');var tpl='<a title="'+data[i].headline+', #'+data[i].rank+' on IMDb Top Rated Movies" href="'
+data[i].clickThru+'?ref_=nv_mv_dflt_1" class="fallback"></a>'
+'<div class="overlay">'
+'<p>'
+'<a href="'+data[i].clickThru+'?ref_=nv_mv_dflt_2" id="titleAdClick">'
+'<strong>'+data[i].headline+'</strong> ('+data[i].titleYears
+')</a>'
+'<br />'
+'<a href="http://www.imdb.com/chart/top?ref_=nv_mv_dflt_3" id="titleAdSecondaryClick">'
+'#<strong>'+data[i].rank+'</strong> on IMDb Top Rated Movies</a> &raquo;'
+'</p>'
+'</div>';}else{$('#nameAd').css('background','url('+data[i].imageUrl+')');var tpl='<a title="'+data[i].headline+', #'+data[i].rank+' on STARmeter" href="'
+data[i].clickThru+'?ref_=nv_cel_dflt_1" class="fallback"></a>'
+'<div class="overlay">'
+'<p>'
+'<a href="'+data[i].clickThru+'?ref_=nv_cel_dflt_2" id="nameAdClick">'
+'<strong>'+data[i].headline+'</strong>'
+'</a> &raquo;'
+'<br />'
+'#<strong>'+data[i].rank+'</strong> on STARmeter</p>'
+'</div>';}
$tpl=$(tpl);$slot.append($tpl);}else if('coords'in data[i]){var tpl='<img class="sideCar" src="'+data[i].sideCarImageUrl+'" />'
+'<img alt="Advertisement" class="mainImage" src="'+data[i].imageUrl+'" useMap="#'+i+'Map" />'
+'<map name="'+i+'Map">'
+'<area target="_blank" shape="'+(data[i].shape||'poly')
+'" coords="'+data[i].coords
+'" href="'+data[i].clickThru
+'" id="'+i+'Click">'
+'</map>',$tpl=$(tpl);$slot.append($tpl);}else{$slot.css('background','url('+data[i].imageUrl+') #ddd');var tpl='<a href="'+data[i].clickThru+'?ref_=nv_cel_fallback_1" class="fallback"></a>';$tpl=$(tpl);$slot.append($tpl);}
if(i==='titleAd'){$("#titleAd > a").one('click',function(){navbar_ads.impressionHandler(navbar_ads.clickEvents.title);});$("#titleAdClick").one('click',function(){navbar_ads.impressionHandler(navbar_ads.clickEvents.title);});$("#titleAdSecondaryClick").one('click',function(){navbar_ads.impressionHandler(navbar_ads.secondaryClickEvents.title);});}else{$("#nameAd > a").one('click',function(){navbar_ads.impressionHandler(navbar_ads.clickEvents.name);});$("#nameAdClick").one('click',function(){navbar_ads.impressionHandler(navbar_ads.clickEvents.name);});}}}
if(window.imdb.watchlistTeaserData){var $navWatchlist=$('#navWatchlist'),data=window.imdb.watchlistTeaserData;for(var i=0;i<3;i++){var $li=$('<li />'),$a=$('<a id="'+(data[i].id||'')+'" href="'+data[i].href+'?ref_=nv_wl_img_'+(i+1)+'"/>'),imgSrc=window.location.protocol==="https:"?data[i].src.replace("http://ia.media-imdb.com","https://images-na.ssl-images-amazon.com"):data[i].src,titleTag=(data[i].title?data[i].title+' ('+data[i].year+') in your Watchlist':'Add items to your watchlist'),className=(data[i].title?'watchListItem':''),$img=$('<img alt="'+titleTag+'" class="'+className+'" src="'+imgSrc
+'" height="209" width="140" title="'+titleTag+'" />');$a.append($img);if(imgSrc.match('/nopicture/')){var $noPosterText=$('<span class="noPosterText">'+titleTag+'</span>');$a.append($noPosterText);}
$li.append($a);$navWatchlist.append($li);}
$('#wlLogin').click(function(e){e.preventDefault();$(window).trigger('initiate_login');});}
if(window.imdb.proMenuTeaser){var $proMenu=$('#proAd'),data=window.imdb.proMenuTeaser,$img=$('<img alt="Go to IMDbPro" src="'+data.imageUrl+'" />');$proMenu.append($img);}
navbarImagesLoaded=true;};if($('#megaMenu').length){$('#consumer_main_nav, #nb_extra_nav').on("mouseenter",loadNavbarImages);$('#navTitleMenu').one('mouseenter',function(){navbar_ads.impressionHandler(navbar_ads.impressionEvents.title);});$('#navNameMenu').one('mouseenter',function(){navbar_ads.impressionHandler(navbar_ads.impressionEvents.name);});$(window).load(loadNavbarImages);$('#nblogout').click(function(e){e.preventDefault();if($('#logoutFrame').length){return;}
$('#navUserMenu .sub_nav').css('display','none');var logoutUrl=this.href;$('<div class="message_box">'
+'<div class="success">'
+'<h2>Logging Out...</h2>'
+'<p>Page will refresh when complete.</p>'
+'</div>'
+'</div>').prependTo('#pagecontent');$('<iframe id="logoutFrame" src="'+logoutUrl+'" height="0" width="0" />')
.appendTo('body')
.load(function(){location.reload();});});if($('#supertab > iframe').length){var $logoTreatment=$('#supertab > iframe'),marginTop=parseInt($logoTreatment.css('margin-top'));$logoTreatment.css('margin-top',marginTop+11);}}
var hasOldNav=false,hasMegaMenu=false;$('link[rel=stylesheet').each(function(){if(this.href.match(/navbar.css$/)){hasOldNav=true;}
if(this.href.match(/navbar-mega.css$/)){hasMegaMenu=true;}});if(hasOldNav&&hasMegaMenu&&'csm'in window){generic.monitoring.record_event('nav_both_css_error');}});})(jQuery);}
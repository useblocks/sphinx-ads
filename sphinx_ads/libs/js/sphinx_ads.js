var sphinx_ads_id = document.querySelector("#sphinx_ads");
let isSelectorAttrSet = sphinx_ads_id.getAttribute("data-sphinx-ads-selector");
var sphinx_ads_selector = isSelectorAttrSet ? isSelectorAttrSet : "div.sphinxsidebar";

function reposition_ads_element(ads_element, ads_selector) {
    ads_element.style.display = "block";
    let append_ads_toElement = document.querySelector(ads_selector);
    append_ads_toElement.appendChild(ads_element);
}

reposition_ads_element(sphinx_ads_id, sphinx_ads_selector);

let sa_items = document.querySelectorAll("div.sphinx-ads-item");

let current_item = document.getElementById("ads_link_1");
current_item.classList.toggle("scale-in-br");
current_item.classList.toggle("sa_is_hidden");
window.localStorage.setItem("current_num", 1);

let total_ads = sa_items.length + 1;
setInterval(myCarousel, 5000, total_ads);

function getRandomInt(min, max) {
  return parseInt(Math.random() * (max - min) + min);
}

function myCarousel(total_ads)
{
    let new_num = getRandomInt(1, total_ads);
    var current_num = window.localStorage.getItem("current_num");

    let old_item = document.getElementById(`ads_link_${current_num}`);
    let new_item = document.getElementById(`ads_link_${new_num}`);

    old_item.classList.toggle("scale-in-br");
    old_item.classList.toggle("slide-out-left");
    new_item.classList.toggle("scale-in-br");
    new_item.classList.toggle("sa_is_hidden");
    old_item.classList.toggle("sa_is_hidden");

    window.localStorage.setItem("current_num", new_num);
}

document.addEventListener("DOMContentLoaded", function () {
    reposition_ads_element()    // Call function to reposition ads element

    // Default layout carousel behavior
    var sa_items = document.querySelectorAll("div.sphinx-ads-item");
    var current_item = document.getElementById("ads_link_1");

    current_item.classList.toggle("scale-in-br");
    current_item.classList.toggle("sa_is_hidden");
    window.localStorage.setItem("current_num", 1);

    var total_ads = sa_items.length + 1;
    setInterval(myCarousel, 5000, total_ads);

});

 
// Reposition ad elements
function reposition_ads_element() {
    var sphinx_ads_id = document.querySelector("#sphinx_ads");
    var isSelectorAttrSet = sphinx_ads_id.getAttribute("data-sphinx-ads-selector");
    var docHTMLtheme = sphinx_ads_id.getAttribute("data-sphinx-ads-docs-html_theme");
    var selectorAttrExist = document.querySelector(isSelectorAttrSet);
    var sphinx_ads_selector = (selectorAttrExist != null) ? isSelectorAttrSet : "div.sphinxsidebar";

    if (selectorAttrExist != null) {
        sphinx_ads_id.style.display = "block";
        var append_ads_toElement = document.querySelector(sphinx_ads_selector);
        append_ads_toElement.appendChild(sphinx_ads_id);
    } else {
        if (docHTMLtheme == "alabaster") {
            sphinx_ads_id.style.display = "block";
            var append_ads_toElement = document.querySelector(sphinx_ads_selector);
            append_ads_toElement.appendChild(sphinx_ads_id);
        }
    }
}

function getRandomInt(min, max) {
    return parseInt(Math.random() * (max - min) + min);
}

function myCarousel(total_ads) {
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

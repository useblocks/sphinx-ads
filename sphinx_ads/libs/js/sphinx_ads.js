var sphinx_ads_id = document.querySelector("#sphinx_ads");
let isSelectorAttrSet = sphinx_ads_id.getAttribute("data-sphinx-ads-selector");
var sphinx_ads_selector = isSelectorAttrSet ? isSelectorAttrSet : "div.sphinxsidebar";

function reposition_ads_element(ads_element, ads_selector) {
    ads_element.style.display = "block";
    let append_ads_toElement = document.querySelector(ads_selector);
    append_ads_toElement.appendChild(ads_element);
}

reposition_ads_element(sphinx_ads_id, sphinx_ads_selector);

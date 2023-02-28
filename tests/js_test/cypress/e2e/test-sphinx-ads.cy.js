describe('Test Sphinx Ads HTML', () => {
  it('Visit Sphinx Ads Homepage', () => {
    // 1. Given a user visits http://localhost:8080/
    cy.visit('/')

    cy.get('#sphinx_ads').each(($el, index, $list) => {
    // 2. When page loads, select all elements that matches the selector `#sphinx_ads`

        var isSelectorAttrSet = $el.attr("data-sphinx-ads-selector");
        var docHTMLtheme = $el.attr("data-sphinx-ads-docs-html_theme");
        var selectorAttrExist = document.querySelector(isSelectorAttrSet);
        var sphinx_ads_selector = (selectorAttrExist != null) ? isSelectorAttrSet : "div.sphinxsidebar";

        cy.get(sphinx_ads_selector).within(() => {
          cy.get($el).should('have.css' ,'display', 'block')   // 3. Check if div#sphinx_ads has display:block
          cy.get('.sphinx-ads-item').should('have.length', 2)   // 4. Check if number of ad elements == 2
        })
    })
  })
})

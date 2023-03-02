import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_basic"}], indirect=True)
def test_build_html_static_files_copied(test_app):
    app = test_app
    app.builder.build_all()

    # Check if static files got copied correctly.
    build_dir = Path(app.outdir) / "_static" / "sphinx_ads"
    files = [f for f in build_dir.glob("**/*") if f.is_file()]
    assert build_dir / "sphinx_ads.css" in files
    assert build_dir / "sphinx_ads.js" in files


@pytest.mark.skipif(sys.platform == "win32", reason="assert fails on windows, need to fix later.")
@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_basic"}], indirect=True)
def test_html_head_files(test_app):
    app = test_app
    app.builder.build_all()

    from lxml import html as html_parser

    # check usage in project root level
    html_path = str(Path(app.outdir, "index.html"))
    root_tree = html_parser.parse(html_path)
    script_nodes = root_tree.xpath("/html/head/script")
    script_files = [x.attrib["src"] for x in script_nodes]
    assert script_files.count("_static/sphinx_ads/sphinx_ads.js") == 1

    link_nodes = root_tree.xpath("/html/head/link")
    link_files = [x.attrib["href"] for x in link_nodes]
    assert link_files.count("_static/sphinx_ads/sphinx_ads.css") == 1

    # Checks if not \ (Backslash) is found as path of js/css files
    # This can happen when working on Windows (would be a bug ;) )
    for head_file in script_files + link_files:
        assert "\\" not in head_file


@pytest.mark.skipif(sys.platform == "win32", reason="assert fails on windows, need to fix later.")
@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_basic"}], indirect=True)
def test_build_html(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()

    assert '<b style="margin-bottom: 3px;">Sphinx Needs</b>' in html
    assert '<b style="margin-bottom: 3px;">Sphinx Test Reports</b>' in html
    assert "ads_link_1" in html
    assert "ads_link_3" in html
    assert (
        "<div id='sphinx_ads' style='display:none;margin-top:5px;padding:0 2px' "
        "data-sphinx-ads-docs-html_theme='alabaster' "
        "data-sphinx-ads-selector='div.sphinxsidebar'>\n"
        "\n"
        "\n"
        "    \n"
        "        \n"
        '            <div id="ads_link_1" class="sphinx-ads-item sa_is_hidden">\n'
        '                <a href="https://sphinx-needs.readthedocs.io" title="Sphinx '
        'Needs">\n'
        '<!--                    <div class="sphinx-ads-img"><img '
        'src="_static/img/download.svg" width="150" height="150"></div>-->\n'
        '                    <b style="margin-bottom: 3px;">Sphinx Needs</b>\n'
        "                    <p>Sphinx-Needs is an extension for the Python "
        "based...</p>\n"
        "                </a>\n"
        "            </div>\n"
        "        \n"
        "    \n"
        "        \n"
        '            <div id="ads_link_2" class="sphinx-ads-item sa_is_hidden">\n'
        '                <a href="https://useblocks.com/sphinx-needs-enterprise/" '
        'title="Sphinx Needs Enterprise">\n'
        '<!--                    <div class="sphinx-ads-img"><img '
        'src="_static/img/download.svg" width="150" height="150"></div>-->\n'
        '                    <b style="margin-bottom: 3px;">Sphinx Needs '
        "Enterprise</b>\n"
        "                    <p>Sphinx-Needs Enterprise package provides "
        "enterprise...</p>\n"
        "                </a>\n"
        "            </div>\n"
        "        \n"
        "    \n"
        "        \n"
        '            <div id="ads_link_3" class="sphinx-ads-item sa_is_hidden">\n'
        '                <a href="https://sphinx-test-reports.readthedocs.io" '
        'title="Sphinx Test Reports">\n'
        '<!--                    <div class="sphinx-ads-img"><img '
        'src="_static/img/download.svg" width="150" height="150"></div>-->\n'
        '                    <b style="margin-bottom: 3px;">Sphinx Test Reports</b>\n'
        "                    <p>Sphinx-Test-Reports shows test results inside "
        "Sphinx...</p>\n"
        "                </a>\n"
        "            </div>\n"
        "        \n"
        "    \n"
        "\n"
        "<div "
        'style="text-align:right;margin-bottom:10px;font-size:10pt;color:#787878;"><i> '
        "With 💛 by&nbsp;<a "
        'href="http://sphinx-ads.useblocks.com/">Sphinx-Ads</a></i></div></div>\n' in html
    )


# TODO: Test to check if JSON file imported exist
# TODO: Test to check if URL response was JSON
# TODO: Test to check if JSON file imported exist
# TODO: Test to check the console output for hints about json schema validation errors

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JSON-to-Excel 文档'
copyright = '2026, WTSolutions'
author = 'WTSolutions'
release = '6.1.0.0'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinx_sitemap']
html_baseurl = 'https://json-to-excel.wtsolutions.cn/zh-cn/latest/'
sitemap_url_scheme = "{link}"
html_extra_path = ['robots.txt','ads.txt','llms.txt']
myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "shibuya"
html_static_path = ['_static']

# 自定义导航链接
# shibuya 主题的导航链接配置项
html_theme_options = {
    "nav_links": [
        {
            "title": "产品介绍",
            "url": "https://s.wtsolutions.cn/excel-json-product.html",
            "external": True
        },
        {
            "title": "JSON-to-Excel 在线应用",
            "url": "https://s.wtsolutions.cn/json-to-excel.html",
            "external": True
        },
        {
            "title": "相关产品",
            "url": "products",
            "children": [
                {
                    "title": "Excel-to-JSON",
                    "url": "https://s.wtsolutions.cn/excel-json-product.html",
                    "external": True
                },
                {
                    "title": "Sheet-to-Doc",
                    "url": "https://s.wtsolutions.cn/sheet-to-doc-product.html",
                    "external": True
                }
            ]
        }
    ]
}

html_context = {
    "languages": [
        ("English", "/en/latest/%s.html", "en"),
        ("中文", "/zh-cn/latest/%s.html", "zh-cn"),
    ]
}

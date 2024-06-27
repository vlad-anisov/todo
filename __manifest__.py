{
    "name": "TODO",
    "version": "17.0",
    "category": "",
    "summary": "Summary",
    "description": """ Description """,
    "depends": [
        # "website",
        "web",
        # "stock",
        "autologin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/todo_page.xml",
        "views/todo_page_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "todo/static/src/**/*",
        ],
    },
    "application": True,
}


# Jazzmin Settings
JAZZMIN_SETTINGS = {
    "site_title": "Kvadrat.uz Admin",
    "site_header": "Kvadrat.uz",
    "site_brand": "Kvadrat.uz",
    "welcome_sign": "Welcome to Kvadrat.uz Admin Panel",
    "copyright": "Kvadrat.uz Ltd",
    "search_model": ["auth.User", "blog.Blog"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Site", "url": "/"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "common", "faq", "investment", "blog", "contact"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "common.PrivacyPolicy": "fas fa-file-contract",
        "faq.FAQ": "fas fa-question-circle",
        "investment.InvestmentStat": "fas fa-chart-line",
        "investment.TeamMember": "fas fa-user-tie",
        "blog.Blog": "fas fa-newspaper",
        "contact.ContactSubmission": "fas fa-envelope",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "darkly",
}

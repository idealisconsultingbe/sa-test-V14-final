{
    "name": "Smart analytics - Dashboard Frame",
    'version': '1.0',
    'category': 'Reporting',
    "summary": "Dashboards for Smart Analytics",
    'description': """
        This module allows the seamless integration of external dashboards in Odoo
    """,
    "author": "Idealis Consulting",
    'website': "https://idealisconsulting.com",
    "depends": ["base", "web"],
    "data": [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',
        # Wizards
        'wizards/create_menu.xml',
        # Views
        'views/assets.xml',
        'views/menuitems.xml',
        'views/smart_analytics_dashboard.xml',
        'views/res_config_settings.xml',
    ],
    'qweb': [
        'static/src/xml/smart_analytics.xml',
    ],
    "installable": True,
}

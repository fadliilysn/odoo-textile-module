
{
    'name': 'Textile Production Management',
    'version': '19.0.1.0',
    'summary': 'Manage textile production orders',
    'description': """
        A learning project for managing textile production orders.
    """,
    'author': 'Fadliilysn',
    'category': 'Manufacturing',
    'depends': ['base', 'product'],
    'data': [
        "security/ir.model.access.csv",
        "views/production_order_views.xml",
        "data/sequence.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

{
    'name' : 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description' : """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license' : 'OPL-1',
    'author' : 'levm-odoo',
    'website' : 'https://www.github.com/levm-odoo',
    'category' : 'Customized Apps/Kawiil',
    'depends' : ['stock'],
    'data' : [
        # Security
        #   Groups and access rights
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        #   Record rules
        'security/registry_security.xml',
        # Data
        'data/registry_data.xml',
        # Views
        'views/registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_template_views_inherits.xml',
    ],
    'demo' : [
        'demo/registry_demo.xml'
    ],
    'application' : True,
}
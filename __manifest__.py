###########################################################################################
# Application that includes all the Odoo customisations
###########################################################################################

{
    'name': 'MM V14 Customisations',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'summary': 'Odoo customisations',
    'sequence': '1',
    'author': 'Martynas Minskis',
    'depends': [],
    'demo': [],
    'data': [
#        Security files should be placed on the top
#        Sequence: security, data, wizards, views
        
        # 'security/ir.model.access.csv',
        # 'wizard/change_task_due_date.xml',
        # 'views/patient.xml',
    ],
    'demo': [],
    'qweb': [],
#     'external_dependencies': {'python': ['pysftp']},
#     'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
#     'licence': 'OPL-1',
}
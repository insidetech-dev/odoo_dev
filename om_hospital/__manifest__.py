# -*- coding: utf-8 -*-
{
    'name' : 'hospital management',
    'version' : '1.1',
    'summary': 'hospital management software',
    'sequence': 1,
    'description': """hospital managemenst software
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['mail',],
    'data': ['security/ir.model.access.csv',
            'views/patient.xml',
             'views/doctor.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

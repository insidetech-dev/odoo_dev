# -*- coding: utf-8 -*-
{
    'name' : 'college management',
    'version' : '1.1',
    'summary': 'college management software',
    'sequence': 1,
    'description': """college management software
    """,
    'category': '',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['mail',],
    'data': ['views/college.xml',
             'views/student.xml',
             'reports/report.xml',
             'reports/college.xml',
             'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

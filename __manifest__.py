# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Software - Empresa de Desarrollo',
    'version': '16.0.1.0.0',
    'category': 'Project',
    'summary': 'Gestión de proyectos para empresa de desarrollo de software',
    'description': """
        Módulo personalizado para gestionar una empresa de desarrollo de software.

        Características:
        - Gestión de empresas contratadoras
        - Gestión de proyectos y tareas
        - Gestión de subtareas
        - Roles: Jefe de proyectos, Analista, Programador
    """,
    'author': 'Richard Ortiz',
    'website': 'https://www.ordidev.com',
    'depends': ['base', 'project', 'mail'],
    'data': [
        # Security
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',

        # Views
        'views/empresa_contratadora_views.xml',
        'views/subtarea_views.xml',
        'views/project_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

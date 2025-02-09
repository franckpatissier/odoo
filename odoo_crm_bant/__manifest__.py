# -*- coding: utf-8 -*-
{
    'name': 'CRM BANT Qualification',
    'version': '18.0.1.0',
    'category': 'CRM',
    'description': u"""
Adds BANT (Budget, Authority, Need, Timing) fields to CRM opportunities for better lead qualification.

Enhance your CRM with a structured BANT qualification field. Easily assess prospects based on Budget, Authority, Need, and Timing. Filter, sort, and prioritize opportunities efficiently to focus on high-potential leads.
""",
    'author': 'Franck Patissier',
    'depends': [
        'crm',
        'web_grid',
        'web_hierarchy',
        'web_studio',
    ],
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/ir_model_access.xml',
        'data/ir_default.xml',
        'data/x_bant.xml',
    ],
    'license': 'OPL-1',
    'images': ['static/description/cover.png'],
}

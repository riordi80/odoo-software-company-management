# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    empresa_contratadora_id = fields.Many2one(
        'gestion_software.empresa_contratadora',
        string='Empresa Contratadora',
        required=True,
        help="Empresa que ha contratado este proyecto"
    )
    
    fecha_contratacion = fields.Date(
        string='Fecha de Contratación',
        default=fields.Date.context_today
    )
    presupuesto = fields.Monetary(
        string='Presupuesto', 
        currency_field='currency_id'
    )
    currency_id = fields.Many2one(
        'res.currency', 
        string='Moneda', 
        default=lambda self: self.env.company.currency_id
    )

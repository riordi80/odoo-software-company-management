# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EmpresaContratadora(models.Model):
    _name = 'gestion_software.empresa_contratadora'
    _description = 'Empresa Contratadora'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Nombre', required=True, index=True, tracking=True)
    cif = fields.Char(string='CIF/NIF', index=True, tracking=True)
    direccion = fields.Text(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    contacto = fields.Char(string='Persona de Contacto')
    notas = fields.Text(string='Notas')
    active = fields.Boolean(string='Activo', default=True)

    # RELACIÓN: Listado de proyectos asociados (One2many)
    # Apunta al campo 'empresa_contratadora_id' que creamos en project_project.py
    project_ids = fields.One2many(
        'project.project',
        'empresa_contratadora_id',
        string='Proyectos Contratados'
    )

    # Campo calculado para mostrar el número de proyectos en el botón de la vista
    project_count = fields.Integer(
        string='Número de Proyectos',
        compute='_compute_project_count'
    )

    @api.depends('project_ids')
    def _compute_project_count(self):
        for record in self:
            record.project_count = len(record.project_ids)

    def action_view_projects(self):
        """ Acción para el Smart Button: Abre la lista filtrada de sus proyectos """
        self.ensure_one()
        return {
            'name': 'Proyectos de ' + self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'view_mode': 'tree,form',
            'domain': [('empresa_contratadora_id', '=', self.id)],
            'context': {'default_empresa_contratadora_id': self.id}
        }

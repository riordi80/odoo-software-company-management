# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    subtarea_ids = fields.One2many(
        'gestion_software.subtarea',
        'task_id',
        string='Subtareas'
    )

    subtarea_count = fields.Integer(
        string='Número de Subtareas',
        compute='_compute_subtarea_count'
    )

    @api.depends('subtarea_ids')
    def _compute_subtarea_count(self):
        for record in self:
            record.subtarea_count = len(record.subtarea_ids)

    def action_view_subtareas(self):
        """Acción para ver todas las subtareas de esta tarea"""
        self.ensure_one()
        return {
            'name': 'Subtareas de ' + self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'gestion_software.subtarea',
            'view_mode': 'tree,form',
            'domain': [('task_id', '=', self.id)],
            'context': {'default_task_id': self.id}
        }

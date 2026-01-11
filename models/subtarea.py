# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError

class Subtarea(models.Model):
    _name = 'gestion_software.subtarea'
    _description = 'Subtarea de Desarrollo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, id'

    name = fields.Char(string='Título', required=True, tracking=True)
    sequence = fields.Integer(string='Secuencia', default=10)
    description = fields.Html(string='Descripción')

    task_id = fields.Many2one(
        'project.task',
        string='Tarea Principal',
        required=True,
        ondelete='cascade',
        index=True
    )

    user_id = fields.Many2one(
        'res.users',
        string='Programador Asignado',
        index=True,
        tracking=True,
        default=lambda self: self.env.user
    )

    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('bloqueada', 'Bloqueada')
    ], string='Estado', default='pendiente', required=True, tracking=True)

    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Normal'),
        ('2', 'Alta'),
        ('3', 'Urgente')
    ], string='Prioridad', default='1', tracking=True)

    date_deadline = fields.Date(string='Fecha Límite')
    date_start = fields.Datetime(string='Fecha Inicio')
    date_end = fields.Datetime(string='Fecha Fin')

    project_id = fields.Many2one(
        'project.project',
        related='task_id.project_id',
        string='Proyecto',
        store=True,
        readonly=True
    )

    notas = fields.Text(string='Notas Adicionales')
    active = fields.Boolean(string='Activo', default=True)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    subtarea_ids = fields.One2many(
        'gestion_software.subtarea', 
        'task_id', 
        string='Subtareas de Desarrollo'
    )
    
    subtarea_count = fields.Integer(
        string='Nº Subtareas', 
        compute='_compute_subtarea_count'
    )

    @api.depends('subtarea_ids')
    def _compute_subtarea_count(self):
        for task in self:
            task.subtarea_count = len(task.subtarea_ids)

    def action_view_subtareas(self):
        self.ensure_one()
        return {
            'name': 'Subtareas de ' + self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'gestion_software.subtarea',
            'view_mode': 'kanban,tree,form',
            'domain': [('task_id', '=', self.id)],
            'context': {'default_task_id': self.id}
        }

    @api.model_create_multi
    def create(self, vals_list):
        """Bloquear creación de tareas para programadores"""
        # Verificar si el usuario es solo programador (no analista ni jefe)
        if self.env.user.has_group('gestion_software.group_programador') and \
           not self.env.user.has_group('gestion_software.group_analista') and \
           not self.env.user.has_group('gestion_software.group_jefe_proyectos'):
            raise AccessError('Los programadores no pueden crear tareas. Solo pueden modificarlas.')
        return super(ProjectTask, self).create(vals_list)

    def unlink(self):
        """Bloquear eliminación de tareas para programadores"""
        # Verificar si el usuario es solo programador (no analista ni jefe)
        if self.env.user.has_group('gestion_software.group_programador') and \
           not self.env.user.has_group('gestion_software.group_analista') and \
           not self.env.user.has_group('gestion_software.group_jefe_proyectos'):
            raise AccessError('Los programadores no pueden eliminar tareas. Solo pueden modificarlas.')
        return super(ProjectTask, self).unlink()

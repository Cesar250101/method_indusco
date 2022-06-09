# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crm(models.Model):
    _inherit = 'crm.lead'

    interesado_en = fields.Char(string='Interesado en')
    tipo_casa = fields.Char(string='Tipo Casa')
    tiene_planos = fields.Char(string='Tiene Planos')
    como_cotizar = fields.Char(string='Como Cotizar')
    tipo_panel = fields.Char(string='Tipo Panel')
    

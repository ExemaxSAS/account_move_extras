# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    expiration_date = fields.Date('Fecha de Vencimiento')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    expiration_date = fields.Date('Fecha de Vencimiento', related='move_id.expiration_date', store=True)

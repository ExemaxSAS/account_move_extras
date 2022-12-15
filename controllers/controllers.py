# -*- coding: utf-8 -*-
# from odoo import http


# class AccountMoveExtras(http.Controller):
#     @http.route('/account_move_extras/account_move_extras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_move_extras/account_move_extras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_move_extras.listing', {
#             'root': '/account_move_extras/account_move_extras',
#             'objects': http.request.env['account_move_extras.account_move_extras'].search([]),
#         })

#     @http.route('/account_move_extras/account_move_extras/objects/<model("account_move_extras.account_move_extras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_move_extras.object', {
#             'object': obj
#         })

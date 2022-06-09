# -*- coding: utf-8 -*-
from odoo import http

# class MethodIndusco(http.Controller):
#     @http.route('/method_indusco/method_indusco/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_indusco/method_indusco/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_indusco.listing', {
#             'root': '/method_indusco/method_indusco',
#             'objects': http.request.env['method_indusco.method_indusco'].search([]),
#         })

#     @http.route('/method_indusco/method_indusco/objects/<model("method_indusco.method_indusco"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_indusco.object', {
#             'object': obj
#         })
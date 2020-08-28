# -*- coding: utf-8 -*-
# from odoo import http


# class TechReclamation(http.Controller):
#     @http.route('/tech_reclamation/tech_reclamation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_reclamation/tech_reclamation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_reclamation.listing', {
#             'root': '/tech_reclamation/tech_reclamation',
#             'objects': http.request.env['tech_reclamation.tech_reclamation'].search([]),
#         })

#     @http.route('/tech_reclamation/tech_reclamation/objects/<model("tech_reclamation.tech_reclamation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_reclamation.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class L10nClRrhh(http.Controller):
#     @http.route('/l10n_cl_rrhh/l10n_cl_rrhh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_rrhh/l10n_cl_rrhh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_rrhh.listing', {
#             'root': '/l10n_cl_rrhh/l10n_cl_rrhh',
#             'objects': http.request.env['l10n_cl_rrhh.l10n_cl_rrhh'].search([]),
#         })

#     @http.route('/l10n_cl_rrhh/l10n_cl_rrhh/objects/<model("l10n_cl_rrhh.l10n_cl_rrhh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_rrhh.object', {
#             'object': obj
#         })

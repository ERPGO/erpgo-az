# -*- coding: utf-8 -*-
from odoo import http

# class MailingSplitter(http.Controller):
#     @http.route('/mailing_splitter/mailing_splitter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mailing_splitter/mailing_splitter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mailing_splitter.listing', {
#             'root': '/mailing_splitter/mailing_splitter',
#             'objects': http.request.env['mailing_splitter.mailing_splitter'].search([]),
#         })

#     @http.route('/mailing_splitter/mailing_splitter/objects/<model("mailing_splitter.mailing_splitter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mailing_splitter.object', {
#             'object': obj
#         })
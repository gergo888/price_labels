# -*- coding: utf-8 -*-
# from odoo import http


# class PriceLabels(http.Controller):
#     @http.route('/price_labels/price_labels', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/price_labels/price_labels/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('price_labels.listing', {
#             'root': '/price_labels/price_labels',
#             'objects': http.request.env['price_labels.price_labels'].search([]),
#         })

#     @http.route('/price_labels/price_labels/objects/<model("price_labels.price_labels"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('price_labels.object', {
#             'object': obj
#         })


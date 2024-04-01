# -*- coding: utf-8 -*-

from odoo import models, fields, api


_sel_property_orientations = [
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
]

_sel_property_state = [
    ('new', 'New'),
    ('offer_received', 'Offer received'),
    ('offer_accepted', 'Offer accepted'),
    ('sold', 'Sold'),
]


class estate_property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'estate.property.type'

    name = fields.Char(string=u'Name', required=False, help=u'')
    description = fields.Char(string=u'Description', help=u'')


class estate_property_tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'estate.property.tag'

    name = fields.Char(string=u'Name', required=False, help=u'')
    description = fields.Char(string=u'Description', help=u'')
    color = fields.Integer()


class estate_property(models.Model):
    _name = 'estate.property'
    _description = 'Estate properties'

    _order = 'name ASC'

    name = fields.Char(string='Title')
    description = fields.Text()
    post_code = fields.Char()
    date_availability = fields.Date(default=fields.Datetime.now)
    expected_price = fields.Float(default=0.0, help='Precio estimado')
    selling_price = fields.Float(default=0.0)
    bedrooms = fields.Integer(default=0)
    living_area = fields.Integer(default=0, string="Living area (M2)")
    facades_area = fields.Integer(default=0)
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(default=0)
    garden_orientation = fields.Selection(selection=_sel_property_orientations)
    state = fields.Selection(selection=_sel_property_state)
    active = fields.Boolean(default=True)
    type_id = fields.Many2one('estate.property.type', string=u'Type', required=True, help=u'')
    tag_ids = fields.Many2many('estate.property.tag', 'estate_property_tag_rel', 'property_id', 'tag_id', string='Tags', help=u'')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', u'Offers', help=u'')


class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'estate.property.offer'

    property_id = fields.Many2one('estate.property', string=u'Property', required=True, help=u'')
    price = fields.Float(string=u'Price', default=0.0, help=u'')
    _status_sel = [
        ('accepted', u'Accepted'),
        ('refused', u'refused')
    ]
    status = fields.Selection(selection=_status_sel, string=u'Status', required=False, help=u'')
    partner_id = fields.Many2one('res.partner', string=u'Partner', required=True, help=u'')

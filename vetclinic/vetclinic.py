# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
    _name_="vetclinic_animal"
    _columns = {
        'name': fields.char('Name', size=64),
        'birthdate':fields.date('Birth Date')
    }
    
##vetclinic_animal() ##optinal in version 7
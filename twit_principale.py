from openerp.osv import osv, fields

class twit_principale(osv.osv):
    _name = 'twit.principale'
    _columns = {
        'twit' : fields.char('twit', size = 128)
    }
    
twit_principale()
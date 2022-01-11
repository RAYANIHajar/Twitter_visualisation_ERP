from openerp.osv import osv , fields


class twit_visuel(osv.osv):
    _name = 'twit.visuel'
    _columns = {
        'id_pub': fields.char('Tweet Id',size=700),
        'like_count': fields.integer('Like Count')
    }
    
    
twit_visuel()
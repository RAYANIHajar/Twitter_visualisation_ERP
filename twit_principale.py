from openerp.osv import osv, fields


class twit_principale(osv.osv):
    def _draft_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'draft'})
        return True 
    def _redact_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'redact'})
        return True
    def _publish_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'publish'})
        return True

    _name = 'twit.principale'
    _columns = {
        'id_pub': fields.char('Tweet Id',size=700),
        'author_id':fields.char('Author_Id',size=700) ,
        'text': fields.char('Text',size=555),
        'created_at': fields.char('Creation Date',size=555),
        'source': fields.char('Source',size=555),
        'retweet_count': fields.integer('Retweet Count'),
        'reply_count': fields.integer('Reply Count'),
        'like_count': fields.integer('Like Count'),
        'quote_count': fields.integer('Quote Count'),
        'state': fields.selection([
            ('draft','Brouillant'),
            ('redact','Rediger'),
            ('publish','Publier')
        ],'State',readonly=True)
    }
    
twit_principale()


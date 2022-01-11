from openerp.osv import osv, fields 




class twit_terme(osv.osv):
    _name = 'twit.terme'
    _columns = {
        'id_pub': fields.char('Tweet Id',size=700),
        'author_id':fields.char('Author_Id',size=700) ,
        'text': fields.char('Text',size=555),
        'created_at': fields.char('Creation Date',size=555),
        'source': fields.char('Source',size=555),
        'retweet_count': fields.integer('Retweet Count'),
        'reply_count': fields.integer('Reply Count'),
        'like_count': fields.integer('Like Count'),
        'quote_count': fields.integer('Quote Count')
    }


twit_terme()
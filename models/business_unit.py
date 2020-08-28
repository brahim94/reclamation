from odoo import fields, api, models, _

class business_unit(models.Model): 
    _inherit = "res.partner"

    sms_authorisation = fields.Boolean('SMS AUTORISÉ ?')
    
    @api.onchange('business_unit_id')
    def onchange_business_unit(self):
        for rec in self:
            return {'domain': {'magasin_id': [('team_id', '=', rec.business_unit_id.id)]}}
            
    business_unit_id = fields.Many2one('crm.team', string='BU')
    magasin_id = fields.Many2one('crm.magasin', string='Magasin')

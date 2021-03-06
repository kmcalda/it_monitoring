from odoo import fields, models, api


class desktops_devices(models.Model):
    _name = 'desktops.devices'
    _description = 'Desktop record'
    _rec_name = 'desktop_model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    desktop_user = fields.Many2one('res.users', string='User', track_visibility='always', required=1, ondelete='set null')
    desktop_image = fields.Binary(string='Image')
    desktop_serial_number = fields.Char(string='Serial Number', track_visibility='always', required=1)
    desktop_model = fields.Char(string='Model name', track_visibility='always')
    desktop_os = fields.Char(string='Operating System', track_visibility='always')
    desktop_processor = fields.Char(string='Processor', track_visibility='always')
    laptop_hdd = fields.Char(string='HDD', track_visibility='always')
    desktop_ram = fields.Char(string='RAM', track_visibility='always')
    desktop_office = fields.Char(string='Office', track_visibility='always')
    desktop_supplier = fields.Many2one('res.partner', string='Supplier', track_visibility='always', ondelete='set null')
    desktop_market_value = fields.Float(string='Market Value', digit=(12,2), track_visibility='always')
    desktop_purchase_date = fields.Date(string='Purchase Date', track_visibility='always')
    desktop_warranty_expiration = fields.Date(string='Warranty Expiration', track_visibility='always')
    desktop_condition = fields.Boolean(string='Unit in use', default=1)
    desktop_age = fields.Char(string='Age')
    desktop_issued = fields.Date(string='Date issued', track_visibility='always')
    desktop_brand = fields.Char(string='Brand', track_visibility='always')
    desktop_note = fields.Text(string='Internal Note')

    _sql_constraints = [
        ('desktop_serial_number_unique',
         'unique(desktop_serial_number)',
         "Error! serial number already exist!"),
    ]

    @api.onchange('desktop_serial_number')
    def _make_uppercase(self):
        if self.desktop_serial_number:
            self.desktop_serial_number = str(self.desktop_serial_number).upper()

    @api.onchange('laptop_hdd')
    def _make_uppercase(self):
        if self.laptop_hdd:
            self.laptop_hdd = str(self.laptop_hdd).upper()

    @api.onchange('laptop_brand')
    def _make_uppercase(self):
        if self.laptop_brand:
            self.laptop_brand = str(self.laptop_brand).upper()

    @api.onchange('desktop_ram')
    def _make_uppercase(self):
        if self.desktop_ram:
            self.desktop_ram = str(self.desktop_ram).upper()
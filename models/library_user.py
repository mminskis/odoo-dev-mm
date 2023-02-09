from odoo import api, fields, models

class LibraryUser(models.Model):
    _name = "library.user"
    _description = "Library User"
    
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], default='other')
    favorite_genres = fields.Text(string="Favorite genres of literature")
   
   #Test 1234
    test = fields.Text(string="Test")
        
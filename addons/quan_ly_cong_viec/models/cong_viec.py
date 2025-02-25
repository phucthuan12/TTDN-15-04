from odoo import models, fields, api


class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công Việc'
    _rec_name = 'ten_cong_viec'

    ten_cong_viec = fields.Char("Tên công việc", required=True, tracking=True)
    du_an = fields.Many2one('project.project', string="Dự án", required=True, tracking=True)
    nguoi_phu_trach = fields.Many2one('res.users', string="Người phụ trách", tracking=True)
    han_chot = fields.Date("Hạn chót", tracking=True)
from odoo import models, fields, api


class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công Việc'

    ten_cong_viec = fields.Char("Tên công việc", required=True)
    han_hoan_thanh = fields.Date("Hạn hoàn thành", required=True)
    tien_do = fields.Float("Tiến độ %", required=True)
    ngay_bat_dau = fields.Date("Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date("Ngày kết thúc", required=True)
    mo_ta = fields.Text("Mô tả công việc", required=True)
    trang_thai = fields.Selection(
        [
            ('moi', 'Mới'),
            ('dang_thuc_hien', 'Đang thực hiện'),
            ('dang_cho', 'Đang chờ '),
            ('tam_hoan', 'Tạm hoãn'),
            ('hoan_thanh', 'Hoàn thành'),
            ('da_huy', 'Đã hủy'),
            ('qua_han', 'Quá hạn'),
            ('da_duyet', 'Đã duyệt'),
            ('can_sua_doi', 'Cần sửa đổi'),
            
        ],
        string= "Trạng thái", default="moi"
    )
    cong_viec_con_ids = fields.One2many ("cong_viec_con", inverse_name="cong_viec_id", string="Công việc con")
    nhan_vien_id = fields.Many2one('nhan_vien',string="Nhân viên phụ trách")
    ghi_nhan_thoi_gian_ids = fields.One2many ("ghi_nhan_thoi_gian", inverse_name="cong_viec_id", string="Ghi nhận thời gian")
    danh_gia_cong_viec_ids = fields.One2many ("danh_gia_cong_viec", inverse_name="cong_viec_id", string="Đánh giá công việc")
    
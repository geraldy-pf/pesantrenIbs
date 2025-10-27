# -*- coding: utf-8 -*-
from odoo import models, fields


class CdnPerijinan(models.Model):
    _name = "cdn.perijinan"
    _description = "Perijinan Santri"

    name = fields.Char(string="Nomor Izin", required=True, copy=False)
    santri_id = fields.Many2one(
        "res.partner", string="Santri", required=True #, domain=[("is_santri", "=", True)]#
    )
    tujuan = fields.Char(string="Tujuan Izin", required=True)
    tanggal_mulai = fields.Date(string="Tgl Mulai", required=True)
    tanggal_selesai = fields.Date(string="Tgl Selesai", required=True)
    keterangan = fields.Text(string="Keterangan")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("approved", "Disetujui"),
            ("rejected", "Ditolak"),
            ("proses_keluar", "Proses Keluar"),
            ("selesai", "Selesai"),
        ],
        string="Status",
        default="draft",
        required=True,
    )
    reject_reason = fields.Text(string="Alasan Penolakan")

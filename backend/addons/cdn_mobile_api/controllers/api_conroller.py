# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class MagangAPIController(http.Controller):

    # ---------- LIST + FILTER (wajib login) ----------
    @http.route(
        "/api/perijinan",
        type="json",
        auth="user",  # wajib login
        methods=["POST"],
        csrf=False,
    )
    def list_perijinan(self, **kw):
        # manual parse JSON-RPC body
        try:
            body = json.loads(request.httprequest.get_data(as_text=True))
        except Exception:
            body = {}
        params = body.get("params", {})

        domain = []
        state = params.get("state")
        if state:
            domain.append(("state", "=", state))

        # tidak perlu .sudo() – user sudah tervalidasi
        records = request.env["cdn.perijinan"].search_read(
            domain,
            [
                "id",
                "name",
                "santri_id",
                "tujuan",
                "tanggal_mulai",
                "tanggal_selesai",
                "state",
                "reject_reason",
            ],
            limit=20,
        )
        return {"status": "ok", "count": len(records), "data": records}

    # ---------- CREATE (wajib login) ----------
    @http.route(
        "/api/perijinan/create",
        type="json",
        auth="user",  # wajib login
        methods=["POST"],
        csrf=False,
    )
    def create_perijinan(self, **kw):
        try:
            body = json.loads(request.httprequest.get_data(as_text=True))
        except Exception:
            body = {}
        params = body.get("params", {})

        new_rec = request.env["cdn.perijinan"].create(
            {
                "name": params.get("name"),
                "santri_id": params.get("santri_id"),
                "tujuan": params.get("tujuan"),
                "tanggal_mulai": params.get("tanggal_mulai"),
                "tanggal_selesai": params.get("tanggal_selesai"),
                "keterangan": params.get("keterangan", ""),
                "state": "draft",
            }
        )
        return {"status": "ok", "id": new_rec.id}

    # ---------- LOGIN (tidak perlu login – gateway) ----------
    @http.route("/api/login", type="json", auth="none", methods=["POST"], csrf=False)
    def login(self, **kw):
        try:
            body = json.loads(request.httprequest.get_data(as_text=True))
        except Exception:
            body = {}
        params = body.get("params", {})

        db = request.env.cr.dbname
        login = params.get("username")
        password = params.get("password")

        try:
            uid = request.session.authenticate(db, login, password)
        except Exception as e:
            return {"status": "error", "message": str(e)}

        if not uid:
            return {"status": "error", "message": "Invalid credentials"}

        user = request.env["res.users"].sudo().browse(uid)
        groups = user.groups_id.mapped("name")

        return {
            "status": "ok",
            "uid": uid,
            "username": user.login,
            "groups": groups,
        }

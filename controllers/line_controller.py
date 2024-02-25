# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)

class LineController(http.Controller):
    @http.route("/line/action", type="http", auth="user")
    def action_line(self, **kw):
        return "action for line"

    @http.route(
        "/line/api/list",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET"],
    )
    def api_list_line(self, **kw):
        _logger.info("LineController.api_list_line")
        records = request.env["interest.line"].sudo().search([])
        data_list = []
        for record in records:
            data_list.append(
                {
                   "id": record.id,
                    "name": record.name,

                }
            )
        return data_list

    @http.route(
        "/line/api/create",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET", "POST"],
    )
    def api_create_line(self, **post):
        _logger.info("LineController.api_create_line")
        new_line = {
            "name": post.get("name"),
       
        }
        try:
            record = request.env["interest.line"].sudo().create(new_line)
            return {
                "id": record.id,
                "name": record.name,
            }
        except Exception as e:
            _logger.error("LineController.api_create_line error: %s", e)
            return {"error": str(e)}
    @http.route(
        "/line/api/delete/<int:id>",
        type="json",
        auth="public",
        methods=["DELETE"]
    )
    def api_delete_line(self, id, **post):
        _logger.info("LineController.api_delete_line")
        record = request.env["interest.line"].sudo().browse(id)
        record.unlink()
        return "Task deleted"

    @http.route("/api/update/<int:id>", type="json", auth="public", methods=["PUT"])
    def api_update_line(self, id, **post):
        _logger.info("LineController.api_update_line")
        record = request.env["interest.line"].sudo().browse(id)
        record.write(
            {
                "name": post.get("name"),
            }
        )
        return "Task updated"
    
    @http.route("/api/read/<int:id>", type="json", auth="public", methods=["GET"])
    def api_read_line(self, id, **post):
        _logger.info("LineController.api_read_line")
        record = request.env["interest.line"].sudo().browse(id)
        return {
            "id": record.id,
            "name": record.name,
        }

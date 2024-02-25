# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)

class RuleController(http.Controller):
    @http.route("/rule/action", type="http", auth="user")
    def action_rule(self, **kw):
        return "action for rule"

    @http.route(
        "/rule/api/list",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET"],
    )
    def api_list_rule(self, **kw):
        _logger.info("RuleController.api_list_rule")
        records = request.env["interest.rule"].sudo().search([])
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
        "/rule/api/create",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET", "POST"],
    )
    def api_create_rule(self, **post):
        _logger.info("RuleController.api_create_rule")
        new_rule = {
            "name": post.get("name"),
        }
        try:
            record = request.env["interest.rule"].sudo().create(new_rule)
            return {
                "id": record.id,
                "name": record.name,
            }
        except Exception as e:
            _logger.error("RuleController.api_create_rule error: %s", e)
            return {"error": str(e)}
    @http.route(
        "/rule/api/delete/<int:id>",
        type="json",
        auth="public",
        methods=["DELETE"]
    )
    def api_delete_rule(self, id, **post):
        _logger.info("RuleController.api_delete_rule")
        record = request.env["interest.rule"].sudo().browse(id)
        record.unlink()
        return "Task deleted"

    @http.route("/api/update/<int:id>", type="json", auth="public", methods=["PUT"])
    def api_update_rule(self, id, **post):
        _logger.info("RuleController.api_update_rule")
        record = request.env["interest.rule"].sudo().browse(id)
        record.write(
            {
                "name": post.get("name"),
            }
        )
        return "Task updated"
    
    @http.route("/api/read/<int:id>", type="json", auth="public", methods=["GET"])
    def api_read_rule(self, id, **post):
        _logger.info("RuleController.api_read_rule")
        record = request.env["interest.rule"].sudo().browse(id)
        return {
            "id": record.id,
            "name": record.name,
        }

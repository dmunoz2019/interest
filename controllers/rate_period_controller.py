# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
import logging

_logger = logging.getLogger(__name__)

class Rate_periodController(http.Controller):
    @http.route("/rate_period/action", type="http", auth="user")
    def action_rate_period(self, **kw):
        return "action for rate_period"

    @http.route(
        "/rate_period/api/list",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET"],
    )
    def api_list_rate_period(self, **kw):
        _logger.info("Rate_periodController.api_list_rate_period")
        records = request.env["interest.rate.period"].sudo().search([])
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
        "/rate_period/api/create",
        type="json",
        auth="public",
        website=False,
        crsf=False,
        methods=["GET", "POST"],
    )
    def api_create_rate_period(self, **post):
        _logger.info("Rate_periodController.api_create_rate_period")
        new_rate_period = {
            "name": post.get("name"),
        }
        try:
            record = request.env["interest.rate.period"].sudo().create(new_rate_period)
            return {
                "id": record.id,
                "name": record.name,
            }
        except Exception as e:
            _logger.error("Rate_periodController.api_create_rate_period error: %s", e)
            return {"error": str(e)}
    @http.route(
        "/rate_period/api/delete/<int:id>",
        type="json",
        auth="public",
        methods=["DELETE"]
    )
    def api_delete_rate_period(self, id, **post):
        _logger.info("Rate_periodController.api_delete_rate_period")
        record = request.env["interest.rate.period"].sudo().browse(id)
        record.unlink()
        return "Task deleted"

    @http.route("/api/update/<int:id>", type="json", auth="public", methods=["PUT"])
    def api_update_rate_period(self, id, **post):
        _logger.info("Rate_periodController.api_update_rate_period")
        record = request.env["interest.rate.period"].sudo().browse(id)
        record.write(
            {
                "name": post.get("name"),
            }
        )
        return "Task updated"
    
    @http.route("/api/read/<int:id>", type="json", auth="public", methods=["GET"])
    def api_read_rate_period(self, id, **post):
        _logger.info("Rate_periodController.api_read_rate_period")
        record = request.env["interest.rate.period"].sudo().browse(id)
        return {
            "id": record.id,
            "name": record.name,
        }

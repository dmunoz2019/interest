// JavaScript file for RuleComponent
odoo.define('interest.RuleComponent', function (require) {
    'use strict';
    const { Component, useState, xml } = owl;
    const { useService } = require('@web/core/utils/hooks');

    class RuleComponent extends Component {
        setup() {
            this.orm = useService('orm');
            this.state = useState({ records: [] });
            this.loadRecords();
        }

        async loadRecords() {
            const records = await this.orm.call('interest.rule', 'search_read', [[]]);
            this.state.records = records;
        }
    }

    RuleComponent.template = 'interest.RuleComponent';


    return RuleComponent;
});

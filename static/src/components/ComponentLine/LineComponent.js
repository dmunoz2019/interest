// JavaScript file for LineComponent
odoo.define('interest.LineComponent', function (require) {
    'use strict';
    const { Component, useState, xml } = owl;
    const { useService } = require('@web/core/utils/hooks');

    class LineComponent extends Component {
        setup() {
            this.orm = useService('orm');
            this.state = useState({ records: [] });
            this.loadRecords();
        }

        async loadRecords() {
            const records = await this.orm.call('interest.line', 'search_read', [[]]);
            this.state.records = records;
        }
    }

    LineComponent.template = 'interest.LineComponent';


    return LineComponent;
});

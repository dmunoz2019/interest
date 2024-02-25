// JavaScript file for RatePeriodComponent
odoo.define('interest.RatePeriodComponent', function (require) {
    'use strict';
    const { Component, useState, xml } = owl;
    const { useService } = require('@web/core/utils/hooks');

    class RatePeriodComponent extends Component {
        setup() {
            this.orm = useService('orm');
            this.state = useState({ records: [] });
            this.loadRecords();
        }

        async loadRecords() {
            const records = await this.orm.call('interest.rate.period', 'search_read', [[]]);
            this.state.records = records;
        }
    }

    RatePeriodComponent.template = 'interest.RatePeriodComponent';


    return RatePeriodComponent;
});

"use strict";
//import * as _WidgetBase from "../../../../resources/dojo-release-1.16.0/dijit/_WidgetBase";
var require_1 = require("../../../../resources/dojo-release-1.16.0/dojo/require");
require_1["default"].require([
    'dojo/parser',
    'dojo/_base/declare',
    'dojo/dom',
    'dojo/dom-construct',
    'dijit/_TemplatedMixin',
    'dijit/_WidgetBase',
    'dojo/ready',
], function (parser, declare, dom, domConstruct, _TemplatedMixin, _WidgetBase, template) {
    var proto = {
        total_processes: 55,
        finished_processes: Number,
        running_processes: Number,
        templateString: template,
        buildRendering: function () {
            this.PTable = domConstruct.create("div", { innerHTML: this.total_processes });
            domConstruct.place('<em> Dojo!</em>', this);
        },
        constructor: function (params, srcNodeRef) {
            console.log("creating widget with params on node " + srcNodeRef);
        }
    };
    declare("ProcessTable", [_WidgetBase], proto);
});

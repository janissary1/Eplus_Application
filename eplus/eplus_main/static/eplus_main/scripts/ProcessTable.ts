//import * as _WidgetBase from "../../../../resources/dojo-release-1.16.0/dijit/_WidgetBase";
import dojo from "./dojo-release-1.16.0/dojo/require";


dojo.require([
    'dojo/parser',
    'dojo/_base/declare',
    'dojo/dom',
    'dojo/dom-construct',
    'dijit/_TemplatedMixin',
    'dijit/_WidgetBase',
    'dojo/ready',
    '../../../templates/eplus_main/ProcessTable.html',
], function (parser, declare, dom, domConstruct, _TemplatedMixin, _WidgetBase,template) {
    var proto = {
        total_processes: 55,//Number,
        finished_processes: Number,
        running_processes: Number,
        templateString: template,
        buildRendering: function(){
            this.PTable = domConstruct.create("div",{innerHTML:this.total_processes});
            domConstruct.place('<em> Dojo!</em>', this);
            console.log("kek");
        },

        constructor: function(params,srcNodeRef){
            console.log("creating widget with params on node " + srcNodeRef);
        },
    };

    declare("ProcessTable",[_WidgetBase],proto);
});

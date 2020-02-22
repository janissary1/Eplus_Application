define([
        "dojo/parser", 
        "dojo/_base/declare", 
        "dijit/_WidgetBase", 
        "dijit/_TemplatedMixin",
        "../ProcessTable"
    ], function(parser ,declare, _WidgetBase, _TemplatedMixin){
            parser.parse();
            return declare("processes",[_WidgetBase, _TemplatedMixin], {});
    });
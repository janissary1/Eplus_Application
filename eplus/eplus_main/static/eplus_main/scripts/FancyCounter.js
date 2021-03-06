require([
    "dojo/_base/declare", "dojo/parser", "dojo/ready",
    "dijit/_WidgetBase", "dijit/_TemplatedMixin"
], function(declare, parser, ready, _WidgetBase, _TemplatedMixin){

    declare("FancyCounter", [_WidgetBase, _TemplatedMixin], {
        // counter
        _i: 0,

        templateString: "<div>" +
            "<button data-dojo-attach-event='onclick: increment'>press me</button>" +
            "&nbsp; count: <span data-dojo-attach-point='counter'>0</span>" +
            "</div>",

        increment: function(){
            this.counter.innerHTML = ++this._i;
            console.log("kek");
        }
    });

    ready(function(){
        // Call the parser manually so it runs after our widget is defined, and page has finished loading
        parser.parse();
    });
});
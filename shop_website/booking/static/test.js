 var counter = 1;$(document).ready(function () {       $("#addrow").on("click", function () {        var newRow = $("<tr>");        var cols = "";        cols += '<td><input id="item_'+counter+'" type="text" name="item_'+counter+'" class="form-control"/></td>';        cols += '<td><input id="quantity_'+counter+'" onkeyup="calculate(this.id);calculateTotal();" onchange="calculate(this.id);calculateTotal();"" type="number" name="quantity_'+counter+'"  class="form-control"/></td>';        cols += '<td><input id="rate_'+counter+'" onkeyup="calculate(this.id);calculateTotal();" onchange="calculate(this.id);calculateTotal();" type="number" name="rate_'+counter+'" class="form-control" /></td>';        cols += '<td><input value="0" id="amount_'+counter+'" type="number" name="amount_'+counter+'"  value="" class="form-control" readonly/></td>';        cols += '<td><input type="button" class="ibtnDel btn btn-md btn-danger do_not_print"  value="Delete"></td>';        newRow.append(cols);        $("table.order-list").append(newRow);           counter++;           });    $("table.order-list").on("click", ".ibtnDel", function (event) {        $(this).closest("tr").remove();               counter -= 1        calculateTotal();    });});var sum = 0;function calculate(id){    var field_number = id.match(/\d+/)[0];        var quantity_id = "quantity_"+ field_number    var quantity_field = document.getElementById(quantity_id);        var rate_id = "rate_"+ field_number    var rate_field = document.getElementById(rate_id);        var amount_id = "amount_"+ field_number    var amount_field = document.getElementById(amount_id);    var sum = 0;    var quantity = 0;    var rate = 0;        if(quantity_field.value)        quantity = parseInt(quantity_field.value);            if(rate_field.value)         rate = parseInt(rate_field.value);        sum = quantity*rate;        amount_field.value = sum  ;       console.log(quantity)    console.log(rate)}function calculateTotal(){        var final_amount_field = document.getElementById("final_amount");        var discount_field = document.getElementById("discount");        var sum = 0;        for(var i=0;i<counter;i++)        {            id = "amount_"+i;            var amount_field = document.getElementById(id);            if(amount_field.value)                sum += parseInt(amount_field.value);        }        if(discount_field.value)                sum -= parseInt(discount_field.value);        final_amount_field.value = sum;       // console.log(sum) ;}function save(){    var message = "Rainbow Dry Cleaners %0a";    var billing_date = new Date();    billing_date = billing_date.toString();    billing_date = billing_date.split(' ', 4).join(' ');    message += "Billing Date : " + billing_date + "%0a";    message += "Items";    message +="   ";    message += "Quantity";    message +="   ";    message += "Amount";    message +="   ";    message +="%0a";    for(var i=0;i<counter;i++)        {            item_id = "item_"+i;            var item_field = document.getElementById(item_id);            quantity_id = "quantity_"+i;            var quantity_field = document.getElementById(quantity_id);            amount_id = "amount_"+i;            var amount_field = document.getElementById(amount_id);                        if(item_field.value){                message += item_field.value;                message +="   ";            }            if(quantity_field.value){               message += quantity_field.value;               message +="   ";              }            if(amount_field.value){                message += amount_field.value;                message +="   ";            }                            message += "%0a";            }    var final_amount_field = document.getElementById("final_amount");        var discount_field = document.getElementById("discount");    if(discount_field.value)         message += "Discount : " + discount_field.value;    if(final_amount_field.value)         message += "Total amount : " + final_amount_field.value;             var message_field = document.getElementById("message");    message_field.value = message}function printBooking() {     //var printContents = document.getElementById(divName).innerHTML;   //  var originalContents = document.body.innerHTML;   //  document.body.innerHTML = printContents;     window.print();   //  document.body.innerHTML = originalContents;}
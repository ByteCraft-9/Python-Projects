$(function () {
    // JSON data by API call for order table
    $.get(orderListApiUrl, function (response) {
        if (response) {
            var table = '';
            var totalCost = 0;

            $.each(response, function (index, order) {
                var total = parseFloat(order.total) || 0; // Ensure total is a number
                totalCost += total;

                table += '<tr>' +
                    '<td>' + order.datetime + '</td>' +
                    '<td>' + order.order_id + '</td>' +
                    '<td>' + order.customer_name + '</td>' +
                    '<td>' + total.toFixed(2) + ' Rs</td></tr>';
            });

            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' + totalCost.toFixed(2) + ' Rs</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});

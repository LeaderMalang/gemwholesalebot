$(document).ready(function() {
    $('.table').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            url: $SCRIPT_ROOT+"/_getListing"
            },
            "columns": [
            { data: 'id' },
            { data: 'title' },
            { data: 'image_url' },
            { data: 'cost_price' },
            { data: 'sold_at' },
            { data: 'stock_list' },
            { data: 'parent_page' },
            { data: 'stock_link' },
            { data: 'updated_at' },
            { data: 'created_at' },
        ],
        "columnDefs": []
    });

    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_getListing', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
} );
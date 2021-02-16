$(document).ready(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_getListing', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
    function getImg(data, type, full, meta) {
        var html="<img  src='"+data+"' class='w-100'/>"
              return html;
    }
    function getNew(data,type,full,meta){
        if (data==1)
            return "Yes";
        return "No";
    }
    function getLink(data,type,full,meta){
        if (meta['col']==5)
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Stock List</a>";
        else if(meta['col']==7)
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Parent Page</a>";
        else
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Stock Link</a>";
        return html
    }
    $('#myTable').DataTable( {
        "processing": true,
        "serverSide": true,
        "pagingType": "full_numbers",
        "paging":true,
        "ajax":$SCRIPT_ROOT+"/_getListing",
        //
        // add column definitions to map your json to the table
        "columns": [
            {data: "title"},
            {data: "image_url", render: getImg},
            {data: "cost_price"},
            {data: "catalogue_value"},
            {data: "sold_at"},
            {data: "stock_list",render:getLink},
            {data: "new",render: getNew},
            {data: "parent_page",render:getLink},
            {data: "stock_link",render:getLink},
            {data: "created_at"},
            {data: "updated_at"},
        ]
    } );


} );
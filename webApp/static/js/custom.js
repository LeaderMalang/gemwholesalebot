$(document).ready(function() {
    function BuyListings(){

    }
    $(document).on('click','.BuyListings', function() {
        var link =$(this).attr('link');
        var title=$(this).parent().next().html();
        console.log(title,link)
      $.getJSON($SCRIPT_ROOT + '/buyListing', {
        lk: link,
        tile: title
      }, function(data) {
        alert('Going to leave this page')
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
    function getLinkBuy (data,type,full,meta) {
        var html="<a  href='#' link='"+data+"''  class='btn btn-primary btn-sm BuyListings'>Buy</a>";
        return html
    }
    function getLink(data,type,full,meta){
        if (meta['col']==6)
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Stock List</a>";
        else if(meta['col']==8)
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Parent Page</a>";
        else
            var html="<a target='_blank' href='"+data+"' class='btn btn-primary btn-sm'>Stock Link</a>";
        return html
    }
    var table=$('#myTable').DataTable( {
        "processing": true,
        "serverSide": true,
        "pagingType": "full_numbers",
        "paging":true,
        "ajax":$SCRIPT_ROOT+"/_getListing",
        //
        // add column definitions to map your json to the table
        "columns": [
            {data: "parent_page",render:getLinkBuy},
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
    // } );
        } );
    setInterval( function () {
    table.ajax.reload();

}, 30000 );


} );
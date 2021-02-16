from flask import Flask,render_template,request,jsonify
from db import con
import requests
app = Flask(__name__)


@app.route('/_getListing')
def getListing():
    #datatable parameters
    draw = request.args.get('draw')
    start = request.args.get("start")
    rowperpage = request.args.get("length")

    columnIndex_arr = request.args.get('order')
    columnName_arr = request.args.get('columns')
    order_arr = request.args.get('order')
    searchValue = request.args.get('search[value]')

    # columnIndex = columnIndex_arr[0]['column']
    # columnName = columnName_arr[columnIndex]['data']
    # columnSortOrder = order_arr[0]['dir']
    # searchValue = search_arr['value']
    print(draw)

    cnn=con()
    cr =cnn.cursor
    query = """SELECT `title`,`image_url`, `cost_price`, `catalogue_value`,
         `sold_at`, `stock_list`, `new`,`parent_page`,stock_link, `created_at`, `updated_at` 
        
        
        FROM `stocks` where title like %s or cost_price like %s order by created_at limit %s offset %s"""
    allQuery="""SELECT `title`, `image_url`, `cost_price`, `catalogue_value`,
         `sold_at`, `stock_list`, `new`,`parent_page`,stock_link, `created_at`, `updated_at` 
        
        
        FROM `stocks` order by created_at limit %s offset %s"""
    allparam=(int(rowperpage),int(start))
    rrd=(searchValue,searchValue,int(rowperpage),int(start))
    res = False
    try:
        if searchValue!='':
          cr.execute(query,rrd)
        cr.execute(allQuery,allparam)
        res = cr.with_rows
    except Exception as ex:
        cnn.connection.rollback()
    print(res)
    data=cr.fetchall()
    listings=[]

    for title,image_url,cost_price,catalogue_value,sold_at,stock_list,new,parent_page,stock_link,created_at,updated_at in data:
        listings.append({"title":title,
                         "image_url":image_url,
                         "cost_price":cost_price,
                         "catalogue_value":catalogue_value,
                         "sold_at":sold_at,
                         "stock_list":stock_list,
                         "new":new,
                         "parent_page":parent_page,
                         "stock_link":stock_link,
                         "created_at":created_at,
                         "updated_at":updated_at

                         })

    print(listings)
    itotalQ="""select count(*) from stocks"""
    param=(searchValue,searchValue)
    try:
        cr.execute(itotalQ)
    except Exception as ex:
        print(ex)
        cnn.connection.rollback()
    itotalrecords=cr.fetchall()
    itotalr=itotalrecords[0][0]
    total=len(listings)
    response = {
        "draw":int(draw),
        "iTotalRecords":total,
        "iTotalDisplayRecords":itotalr,
        "aaData":listings



    }

    return jsonify(response)

@app.route('/send_message')
def send_message():



    bot_token = '1598350721:AAFA4YMJBqxeVfzIjfMzqbP3PMtsMZSvdsk'
    bot_chatID = '1644262765'
    bot_message="Hello Message Up."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    print(response)

    return response.json()



@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
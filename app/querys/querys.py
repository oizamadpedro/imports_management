from utils.tools import selDB, insDB

def getRecentBuys():
    query = "SELECT buy_products.id, buy_products.order_id, products.product, products.quantity, buy_products.price, buy_products.rate_product, "
    query += "buy_products.shop, buy_products.buy_date "
    query += "FROM buy_products INNER JOIN products ON buy_products.product_id = products.id; "
    recentBuys = selDB(query)
    return recentBuys

def allSells():
    query = "SELECT sell_products.id as sell_id, sell_products.price, products.product, "
    query += "clients.counterpart_name, clients.cel_number FROM sell_products "
    query += "INNER JOIN clients ON sell_products.client_id = clients.client_id "
    query += "INNER JOIN products ON products.id = sell_products.product_id;"
    allSells = selDB(query)
    return allSells
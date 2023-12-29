from utils.tools import selDB, insDB

def getRecentBuys():
    query = "SELECT buy_products.id, buy_products.order_id, products.product, products.quantity, buy_products.price, buy_products.rate_product, "
    query += "buy_products.shop, buy_products.buy_date "
    query += "FROM buy_products INNER JOIN products ON buy_products.product_id = products.id; "
    recentBuys = selDB(query)
    return recentBuys
import json, os

#đọc dữ liệu 
def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)
        
def load_category():
    return read_json('data/category.json')

def load_product(cate_id=None, kw=None, from_price=None, to_price=None):
    products =  read_json('data/product.json')

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    if from_price:
        products = [p for p in products if p['price'] >= float(from_price)]
    if to_price:
        products = [p for p in products if p['price'] <= float(to_price)]
    return products

def get_product_by_id(product_id):
    products =  read_json('data/product.json')
    for p in products:
        if p['id'] == product_id:
            return p
    return None
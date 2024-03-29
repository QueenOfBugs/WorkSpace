import json
from jsonpath import jsonpath

book_dict = '''{
        "store": {
            "book": [
                {
                    "category": "reference",
                    "author": "Nigel Rees",
                    "title": "Sayings of the Century",
                    "price": 8.95
                }, 
                {
                    "category": "fiction",
                    "author": "Evelyn Waugh",
                    "title": "Sword of Honour",
                    "price": 12.99
                }, 
                {
                    "category": "fiction",
                    "author": "Herman Melville",
                    "title": "Moby Dick",
                    "isbn": "0-553-21311-3",
                    "price": 8.99
                }, 
                {
                    "category": "fiction",
                    "author": "J. R. R. Tolkien",
                    "title": "The Lord of the Rings",
                    "isbn": "0-395-19395-8",
                    "price": 22.99
                }
            ],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }'''


# 将json字符串转化为字典
data = json.loads(book_dict)
# 获取自行车颜色
print(jsonpath(data, '$..bicycle.color'))

# 获取所有商品的价格
print(jsonpath(data, '$..price'))

# 获取所有书的作者

# 获取第二本书的书名和作者
print(jsonpath(data, '$..book[:2][author,title,price]'))
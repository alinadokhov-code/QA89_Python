from urllib import response

books = {
    'Harry Potterr and ....' : 'J.K.Rowling',
    'To kill a mockingbird': 'Harper Lee'
}

books1 = {
    'Harry Potterr and ....',
    'To kill a mockingbird'
}
print(books1)

response = {
    'statusCode': 'success',
    'user': {
        'id':1,
        'name':'Kris'
    }
}
print(response['user']['name'])


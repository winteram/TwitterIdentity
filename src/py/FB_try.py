



import facebook

token = 'CAACEdEose0cBAAZBgzkcXBd3XlXQPgvi1ZAW6h41hW13xCtWdPZCjxPWHswcCM0YXmtB0x7W56Pxbe2bpaXUxPZBKX7OSS20aj4TkVSZALVtwilDgZCACgcGBi7QyxAAykxLlaQXvjj0LETlZBOcZASZCSqxOPYXkojmx2JWAHBAffS7iPh9udksZALjzgGohiXe9bpcazkmltIAZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "likes")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list
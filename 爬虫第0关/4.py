import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
movie = res.content
movies = open('aa.mp3','wb')
movies.write(movie)
movies.close()
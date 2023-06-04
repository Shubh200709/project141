from flask import Flask, request, jsonify
import pandas as pd

df1 = pd.read_csv('shared_articles.csv')

app = Flask(__name__)


headers = df1[['timestamp','eventType','contentId','authorPersonId','authorSessionId','authorUserAgent','authorRegion','authorCountry','contentType','url','title','text','lang']]
head = df1[1:]
liked_articles = []
not_liked_articles = []

def assign_val():
    m_data = {
        "original_title": headers.iloc[0,0],
        "poster_link": headers.iloc[0,1],
        "release_date": headers.iloc[0,2] or "N/A",
        "duration": headers.iloc[0,3],
        "rating":headers.iloc[0,4]/2
    }
    return m_data

@app.route("/movies")
def get_movie():
    movie_data = assign_val()

    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/like")
def liked_movie():
    global all_movies
    movie_data=assign_val()
    liked_articles.append(movie_data)
    all_movies.drop([0], inplace=True)
    all_movies = all_movies.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

@app.route('/liked')
def liked():
    global liked_articles   

    return jsonify({
        'data' : liked_articles, 
        'status' : 'success'
    })

@app.route("/dislike")
def unliked_movie():
    global all_movies

    movie_data=assign_val()
    not_liked_articles.append(movie_data)
    all_movies.drop([0], inplace=True)
    all_movies=all_movies.reset_index(drop=True)
    
    return jsonify({
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
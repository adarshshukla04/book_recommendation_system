from flask import Flask, render_template
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
# Send each columns of popular_df to index.html
def index():
    return render_template('index.html',
    book_name = list(popular_df['Book-Title'].values),
    author    = list(popular_df['Book-Author'].values),
    image     = list(popular_df['Image-URL-M'].values),
    votes     = list(popular_df['num_ratings'].values),
    rating    = list(popular_df['avg_ratings'].values)
    )

@app.route('/recommend')
def recommend():
    return render_template('recommend_page.html')

if __name__ == '__main__':
    app.run(debug=True)
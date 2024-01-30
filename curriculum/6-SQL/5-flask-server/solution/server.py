from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/gaming_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Models
class Game(db.Model):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    genre = db.relationship('Genre', backref='games')

class Genre(db.Model):
    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(255), unique=True)

# API Endpoints
@app.route('/api/games', methods=['GET'])
def get_all_games():
    games = Game.query.all()
    return jsonify({'games': [{'game_title': game.game_title, 'quantity': game.quantity, 'price': game.price} for game in games]})

@app.route('/api/games/genre/<genre_name>', methods=['GET'])
def get_games_by_genre(genre_name):
    genre = Genre.query.filter_by(genre_name=genre_name).first()
    if genre:
        games = Game.query.filter_by(genre_id=genre.genre_id).all()
        return jsonify({'games': [{'game_title': game.game_title, 'quantity': game.quantity, 'price': game.price} for game in games]})
    else:
        return jsonify({'message': 'Genre not found'}), 404

@app.route('/api/games/<game_id>', methods=['GET'])
def get_game_details(game_id):
    game = Game.query.get(game_id)
    if game:
        return jsonify({'game_title': game.game_title, 'quantity': game.quantity, 'price': game.price, 'genre': game.genre.genre_name})
    else:
        return jsonify({'message': 'Game not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

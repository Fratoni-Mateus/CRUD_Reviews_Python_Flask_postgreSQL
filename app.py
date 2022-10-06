from types import NoneType
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# ----- To-Do -----
# Separação de rotas e configs
# Criar testes da API


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    pros = db.Column(db.String(70), nullable=True, default="")
    cons = db.Column(db.String(70), nullable=True, default="")
    comment = db.Column(db.String(1000), nullable=True, default="")

    def __init__(self, name, rating, pros, cons, comment):
        self.name = name
        self.rating = rating
        self.pros = pros
        self.cons = cons
        self.comment = comment


db.create_all()


class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'rating', 'pros', 'cons', 'comment')


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)


@app.route('/reviews', methods=['POST'])
def create_review():

    name = request.json['name']
    rating = request.json['rating']
    try:
        pros = request.json['pros']
    except:
        pros = ""
    try:
        cons = request.json['cons']
    except:
        cons = ""
    try:
        comment = request.json['comment']
    except:
        comment = ""

    if rating > 5 or rating < 1:
        return "", 406

    new_review = Review(name, rating, pros, cons, comment)
    db.session.add(new_review)
    db.session.commit()
    return review_schema.jsonify(new_review), 201


@app.route('/reviews', methods=['GET'])
def get_reviews():
    all_reviews = Review.query.all()
    result = reviews_schema.dump(all_reviews)
    return jsonify(result)


@app.route('/reviews/<id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    if review is None:
        return "", 404
    return review_schema.jsonify(review)


@app.route('/reviews/<id>', methods=['PUT'])
def update_review(id):
    review = Review.query.get(id)
    if review is None:
        return "", 404

    name = request.json['name']
    rating = request.json['rating']
    try:
        pros = request.json['pros']
    except:
        pros = ""
    try:
        cons = request.json['cons']
    except:
        cons = ""
    try:
        comment = request.json['comment']
    except:
        comment = ""

    if rating > 5 or rating < 1:
        return "", 406

    review.name = name
    review.rating = rating
    review.pros = pros
    review.cons = cons
    review.comment = comment

    db.session.commit()
    return review_schema.jsonify(review)


@app.route('/reviews/<id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if review is None:
        return "", 404

    db.session.delete(review)
    db.session.commit()

    return review_schema.jsonify(review)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'}), 200


if __name__ == "__main__":
    app.run(debug=True)

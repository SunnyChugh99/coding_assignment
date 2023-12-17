from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
# from moviepy.editor import VideoFileClip, TextClip
from io import BytesIO
import moviepy.config as mp_config

import moviepy.editor as me

import os
mp_config.change_settings({'IMAGEMAGICK_BINARY': '/usr/bin/convert'})
mp_config.change_settings({'IMAGEMAGICK_TEMP_DIR': '/tmp'})

# Set the ImageMagick temporary directory
os.environ['MAGICK_TMPDIR'] = '/tmp'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)
jwt = JWTManager(app)


# Framework Setup
# Task 1: Framework Setup
@app.route('/')
def hello_flask():
    return 'Hello, Flask!'
# Movie Model
class Movie(db.Model):
    __tablename__ = 'movie'  # Explicitly set the table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    lead_actor = db.Column(db.String(80), nullable=False)


# Create the database tables
db.create_all()
# Routes for RESTful API Development

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{'title': movie.title, 'genre': movie.genre, 'lead_actor': movie.lead_actor} for movie in movies])

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()

    # Check if a movie with the same title already exists
    existing_movie = Movie.query.filter_by(title=data['title']).first()
    if existing_movie:
        return jsonify(message='Movie with the same title already exists, call update api if you want to update movie info'), 400

    # If the movie with the same title doesn't exist, add the new movie
    new_movie = Movie(title=data['title'], genre=data['genre'], lead_actor=data['lead_actor'])
    db.session.add(new_movie)
    db.session.commit()

    return jsonify({'title': new_movie.title, 'genre': new_movie.genre, 'lead_actor': new_movie.lead_actor}), 201

@app.route('/movies', methods=['PUT'])
def update_movie():
    title = request.args.get('title')
    if not title:
        return jsonify(message='Title parameter is required'), 400

    data = request.get_json()

    movie_to_update = Movie.query.filter_by(title=title).first()

    if not movie_to_update:
        return jsonify(message='Movie with title "{}" not found'.format(title)), 404

    movie_to_update.genre = data.get('genre', movie_to_update.genre)
    movie_to_update.lead_actor = data.get('lead_actor', movie_to_update.lead_actor)

    db.session.commit()

    return jsonify({'title': movie_to_update.title, 'genre': movie_to_update.genre, 'lead_actor': movie_to_update.lead_actor}), 200

# Routes for Token-based Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('username') == 'your_username' and data.get('password') == 'your_password':
        # Create a token with identity (can be any data you want to store in the token)
        access_token = create_access_token(identity=data['username'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

@app.route('/protected', methods=['GET'])
@jwt_required()  # This route requires a valid access token
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/process_video', methods=['POST'])
def process_video():
    # Ensure the request contains a file
    if 'file' not in request.files:
        return jsonify(message='No file provided'), 400

    file = request.files['file']

    # Ensure the file has an allowed extension (e.g., MP4)
    allowed_extensions = {'mp4'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify(message='Invalid file format'), 400

    # Save the file to a temporary location
    file_path = 'temp_video.mp4'
    file.save(file_path)

    # Process the video using MoviePy (add text to the video)
    try:
        vid = me.VideoFileClip(file_path)
        vid.write_videofile("/tmp/sample_video_output.mp4")
        os.remove(file_path)
        return send_file("/tmp/sample_video_output.mp4", as_attachment=True),  200
    except Exception as e:
        return jsonify(message='Error processing video: {}'.format(str(e))), 500



if __name__ == '__main__':
    app.run(debug=True)

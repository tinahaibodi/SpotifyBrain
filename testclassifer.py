import sys
import spotipy
import spotipy.util as util
import json

scope = 'user-library-read'
client_id = <insert client id here>
client_secret = <insert client secret here>
redirect_uri = <insert redirect uri here>

username = raw_input("Enter your spotify email:")

token = util.prompt_for_user_token(username, scope, client_id,
	client_secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)

    raw_json = sp.current_user_saved_tracks(limit=50)

    items = raw_json['items']
    song_list = []

    genre_list = []

    for item in items :
    	song = item['track']

    	song_uri = song['uri']
    	song_list.append(song_uri)

    	album_uri = song['album']['uri'] 
    	album = sp.album(album_uri)
    	genres = album['genres']
    	genre_list.append(genres)

    print(genre_list)

    features_list = sp.audio_features(song_list)
    song_dict = {}

    for features in features_list :
    	song_uri = features['uri']

    	attributes_array = []
    	attributes_array.append(features['energy'])
    	attributes_array.append(features['liveness'])
    	attributes_array.append(features['tempo'])
    	attributes_array.append(features['speechiness'])
    	attributes_array.append(features['acousticness'])
    	attributes_array.append(features['instrumentalness'])
    	attributes_array.append(features['time_signature'])
    	attributes_array.append(features['danceability'])
    	attributes_array.append(features['key'])
    	attributes_array.append(features['duration_ms'])
    	attributes_array.append(features['loudness'])
    	attributes_array.append(features['valence'])
    	attributes_array.append(features['mode'])

    	song_dict[song_uri] = attributes_array

	for key in song_dict.keys() :
		print(song_dict[key])





else:
    print "Can't get token for", username

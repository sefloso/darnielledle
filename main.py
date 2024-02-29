from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/lyrics')
def render_lyrics():
      return render_template('lyrics.html')

@app.route('/audio')
def render_audio():
      return render_template('audio.html')

@app.route('/timed_lyrics')
def render_timed_lyrics():
      return render_template('timed_lyrics.html')

@app.route('/timed_audio')
def render_timed_audio():
      return render_template('timed_audio.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1', port = 5000)

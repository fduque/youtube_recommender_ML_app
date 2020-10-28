import os.path
from flask import Flask
import os
import json
import run_backend

import time

app = Flask(__name__)

def get_predictions():
    
    videos = []

    novos_videos_json = "data/novos_videos.json"
    if not os.path.exists(novos_videos_json):
        run_backend.update_db()

    last_update = os.path.getmtime(novos_videos_json) * 1e9

    #if time.time_ns() - last_update > (720*3600*1e9): #when the range is > than aprox. 1 month
    #    run_backend.update_db()
    
    with open(novos_videos_json, 'r')as data_files:
        for line in data_files:
            line_json = json.loads(line)
            videos.append(line_json)

    predictions = []
    for video in videos:
        predictions.append((video['video_id'], video['title'], float(video['score'])))

    #Getting only the 30 recomendations with highest score
    predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:30]

    #Creating html code for each video recommended
    predictions_formatted = []
    for e in predictions:
        predictions_formatted.append("<tr><th><a href=\"{link}\">{title}<a/></th><th>{score}<\th><\tr>".format(title=e[1], link=e[0], score=e[2]))
    
    return '\n'.join(predictions_formatted),last_update

@app.route('/')
def main_page():
    preds, last_update = get_predictions() #it will return a list with predictions and last datetime update
    return """<head><h1>YouTube Recommender App</h1></head>
    <body>
    Seconds since the last update: {}
    <table>
        {}
    </table>
    </body>""".format((time.time_ns() - last_update) / 1e9, preds)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
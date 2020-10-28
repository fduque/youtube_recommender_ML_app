from get_data import *
from ml_utils import *
import time

queries = ["machine+learning", "data+science", "kaggle"]

def update_db():
    with open("novos_videos.json", 'w+') as output:
        for query in queries:
            for page in range(1,4):
                #will return html code
                search_page = download_search_page(query, page)
                #will return video list
                video_list = parse_search_page(search_page)

                for video in video_list:

                    video_page = download_video_page(video['link'])
                    video_json_data = parse_video_page(video_page)

                    #Todo: fix be more reliable
                    if 'watch-time-text' not in video_json_data:
                        continue
                    #returning score
                    p = compute_prediction(video_json_data)

                    #preparing data to be shown on html page
                    video_id = video_json_data.get('og:video:url', '')
                    data_front = {"title": video_json_data['watch-title'], "score":float(p), "video_id": video_id}
                    data_front['update_time'] = time.time_ns()

                    print(video_id, json.dumps(data_front))
                    output.write("{}\n".format(json.dumps(data_front)))
    return True
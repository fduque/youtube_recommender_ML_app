# youtube_recommender_ML_app

## A E2E project for creating a video recommender app based on YouTube videos.

## Project NOTES:
- As final project from course provided by Kagglemaster Mario Filho, the target of this project is to implement a bunch of shortcuts and best practices learned in his course.
- From data extraction to deploying model, the project uses an ensemble model (LightGBM and RandomForest) to predict which ytube video would be interesting based on three keywords ["machine+learning", "data+science", "kaggle"].

### Project link: https://mltubeapp.herokuapp.com/

## Check below a high-level diagram of the project:
![alt text](https://github.com/fduque/youtube_recommender_ML_app/blob/9180e60b10f13faf071ccd0b010599c507d429a7/projeto_ML_youtube.png)


## Project next steps:
- [x] Data Extraction
- [x] EDA
- [x] Modeling
- [x] Simple Front Page
- [x] Heroku Deploy
- [x] API Prediction
- [ ] Data Extractor broken! - Fix Data Extractor
- [ ] Implement some Database
- [ ] Implement Cloud of words chart based on TFIDVectorizer

## Packages used:
- gunicorn==20.0.4
- Flask==1.1.2
- requests==2.25.0
- beautifulsoup4==4.9.3
- pandas==1.1.4
- joblib==0.17.0
- numpy==1.19.4
- scipy==1.5.4
- scikit-learn==0.23.2
- lightgbm==2.3.0


## Running project:
Running local with Flask:
1 - Git clone repository
2 - Create venv
3 - Activate venv
4 - Install requirements
5 - Start Flask server

```console
git clone https://github.com/fduque/youtube_recommender_ML_app.git ytube
cd ytube
python -m venv .ytube 
source .ytube/bin/activate
pip install -r requirements.txt
flask run
```

Running local with Docker:
1 - Turn on Docker Desktop
2 - Execute build docker 
3 - Run docker

```console 
docker build . -t appinstance1
docker run -e PORT=80 -p 80:80 appinstance1
```
### Related links:
- https://github.com/ledmaster


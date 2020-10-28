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
- [ ] API Prediction
- [ ] Implement some Database
- [ ] Implement Cloud of words chart based on TFIDVectorizer

## Packages used:
- gunicorn==20.0.4
- Flask==1.1.1
- requests==2.22.0
- beautifulsoup4==4.7.1
- pandas==0.25.1
- joblib==0.13.2
- numpy==1.17.2
- scipy==1.3.0
- scikit-learn==0.20.3
- lightgbm==2.3.0

### Related links:
- https://github.com/ledmaster

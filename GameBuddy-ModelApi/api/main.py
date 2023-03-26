from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is working"}

@app.post("/predict")
async def predict(username: int):
    with open("/Users/burak/Developer/MachineLearning/GameBuddy/GameBuddy-Matching/pickle/games-encoded.pkl", "rb") as f:
        df_games_encoded = pickle.load(f)

    with open("/Users/burak/Developer/MachineLearning/GameBuddy/GameBuddy-Matching/pickle/matching.pkl", "rb") as f:
        df_user = pickle.load(f)

    matching_list = getCluster(df_user, df_games_encoded, username)
    #return Response(matching_list.to_json(orient="records"), media_type='application/json')
    return matching_list

def getCluster(df_user, df_games_encoded, username=1):
    user_cluster_id = df_user.iloc[username]['Cluster Score']
    vectorizer = CountVectorizer()

    group = df_user[df_user['Cluster Score'] == user_cluster_id].drop('Cluster Score', axis=1)
    group = group.join(df_games_encoded, how='inner', lsuffix='_left', rsuffix='_right')
    corr_group = group.T.corr()
    top_sim = corr_group[[username]].sort_values(by=[username],axis=0, ascending=False)[1:101]
    return top_sim


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4567)
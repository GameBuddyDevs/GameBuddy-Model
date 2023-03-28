from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is working"}

@app.post("/predict")
async def predict(username: int):
    path = os.path.abspath("pickle")

    with open(path + "/games-encoded.pkl", "rb") as f:
        df_games_encoded = pickle.load(f)

    with open(path + "/matching.pkl", "rb") as f:
        df_matching = pickle.load(f)

    with open(path + "/users.pkl", "rb") as f:
        df_users = pickle.load(f)

    matching_list = getCluster(df_matching, df_games_encoded, df_users, username)

    return matching_list

def getCluster(df_matching, df_games_encoded, df_users, user_id=1):
    user_cluster_id = df_matching.iloc[user_id]['Cluster Score']
    vectorizer = CountVectorizer()

    group = df_matching[df_matching['Cluster Score'] == user_cluster_id].drop('Cluster Score', axis=1)
    group = group.join(df_games_encoded, how='inner', lsuffix='_left', rsuffix='_right')
    corr_group = group.T.corr()
    top_sim = corr_group[[user_id]].sort_values(by=[user_id],axis=0, ascending=False)[1:101]

    top_sim['username'] = df_users.loc[df_users.index]
   

    return top_sim


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4567)
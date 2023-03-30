from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Api is working"}

@app.get("/updateData")
async def updateData():
    path = os.path.abspath("GameBuddy-Matching/models")
    with open(path + "/test.ipynb", "rb") as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': path}})
    return {"message": "Data updated"}


@app.post("/predict")
async def predict(user_id: str):
    path = os.path.abspath("GameBuddy-ModelApi/api/pickle")

    with open(path + "/games-encoded.pkl", "rb") as f:
        df_games_encoded = pickle.load(f)

    with open(path + "/matching.pkl", "rb") as f:
        df_matching = pickle.load(f)

    with open(path + "/users.pkl", "rb") as f:
        df_users = pickle.load(f)

    matching_list = getCluster(df_matching, df_games_encoded, df_users, user_id)

    return matching_list

def getCluster(df_matching, df_games_encoded, df_users, user_id):
    user_cluster_id = df_matching.at[user_id, 'Cluster Score']
    vectorizer = CountVectorizer()

    group = df_matching[df_matching['Cluster Score'] == user_cluster_id].drop('Cluster Score', axis=1)
    group = group.join(df_games_encoded, how='inner', lsuffix='_left', rsuffix='_right')
    corr_group = group.T.corr()
    top_sim = corr_group[[user_id]].sort_values(by=[user_id],axis=0, ascending=False)[1:101]
    sim_users = top_sim.index.tolist()
    content = {
        "user_id": user_id,
        "sim_users": sim_users
    }

    return JSONResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4567)
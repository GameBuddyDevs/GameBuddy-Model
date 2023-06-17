# ML Project: Gamer Matching

This repository contains the source code and data for a machine learning project aimed at matching gamers based on their information. The project includes data preprocessing, model training, and an API for retrieving matching users.

## Folder Structure

The project's folder structure is organized as follows:

```	
- Matching
    - dataset
          gamers-info.csv
    - models
          matching-model.ipynb
          test.ipynb
- Api
    - pickle
          games-encoded.pkl
          matching.pkl
          users.pkl
      main.py
      test.py
.gitignore
Dockerfile
requirements.txt
```	


- **Matching**: This directory contains the code and data related to the matching algorithm.
  - **dataset**: This directory contains the dataset used for training the model. The file `gamers-info.csv` contains mock data about gamers' information.
  - **models**: This directory contains Jupyter Notebook files (`matching-model.ipynb` and `test.ipynb`) used for data preprocessing and model training.

- **Api**: This directory contains the code and files related to the API implementation.
  - **pickle**: This directory contains the pickle files used by the API.
    - `games-encoded.pkl`: A pickle file containing encoded information about games.
    - `matching.pkl`: A pickle file containing the trained matching model.
    - `users.pkl`: A pickle file containing user data.
  - `main.py`: The main file for the API implementation.
  - `test.py`: A file containing test cases for the API.

- `.gitignore`: This file specifies which files and directories should be ignored by Git version control.

- `Dockerfile`: A Dockerfile that specifies the Docker image configuration for the project.

- `requirements.txt`: A file listing the Python dependencies required to run the project.

## Getting Started

To run the project and utilize the API, follow the instructions below:

1. Clone this repository to your local machine:

   ```shell
   git clone <repository-url>

2. Install the required Python dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Preprocess the data and train the matching model by executing the matching-model.ipynb and test.ipynb notebooks located in the Matching/models directory.

4. Generate the necessary pickle files (games-encoded.pkl, matching.pkl, and users.pkl) by running the code in the matching-model.ipynb notebook.

5. Start the API server by running the main.py file in the Api directory. Do not forget the give your own password.

   ```shell
   uvicorn main:app --reload
   ```

6. The API will be accessible at http://localhost:8000 by default. You can test the API by using the provided endpoints. Refer to the documentation or the code in main.py for details on available endpoints and their usage.

## Docker Support
This project includes a Dockerfile, allowing you to containerize the application. To use Docker, follow these steps:

1. Build the Docker image using the provided Dockerfile:
    ```shell
   docker build -t gamer-matching .
   ```

2. Run a container using the built image:
    ```shell
   docker run -d -p 8000:8000 gamer-matching
   ```
   The API will be accessible at http://localhost:8000 within the Docker container, and you can access it through the same URL on your host machine.

## LICENSE
This project is licensed under the MIT License.

## Contributing
Contributions to this project are welcome. If you find any.
#Insurance Price Prediction

Application URL: https://premium-price-prediction.herokuapp.com/

Requirements:
1) Github account
2) Heroku account (or any other cloud service platform)
3) VScode (or any other IDE)
4) GIT CLI

Creating virtual environment and requirements.txt:
1) conda create -p <env_name> python==3.7 -y
2) conda activate <env_name>
3) pip freeze > requirements.txt
4) pip install -r requirements.txt

To setpup CI/CD pipeline in heroku we need following information:
1) HEROKU_EMAIL: singhmohan1998july@gmail.com
2) HEROKU_API_KEY: <API_KEY>
3) HEROKU_APP_NAME: premium-price-prediction

BUILD DOCKER IMAGE:
1) docker build -t <image_name>:<tag_name> .
2) docker images To list Docker Image and get IMAGE_ID
3) Run Docker Image docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>
4) docker ps To check running container in docker
5) docker stop <container_id> to stop docker container



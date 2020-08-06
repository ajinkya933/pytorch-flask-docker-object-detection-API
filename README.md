# pytorch-flask-docker-object-detection-API

## Docker image is available :

```
docker pull ajinkyabobade93/ssd-detection-app
sudo docker run -it -d -p 5000:5000 ajinkyabobade93/ssd-detection-app
```
API call:

```
git clone https://github.com/ajinkya933/pytorch-flask-docker-object-detection-API
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
```
# If you want to build from source 
___

## Install weights

```
mkdir weights
cd weights
wget https://s3.amazonaws.com/amdegroot-models/ssd300_mAP_77.43_v2.pth
```
## Docker build image

```
sudo docker build -t ssd-detection-app:latest .
```

## Docker ssh into image
```
sudo docker build -t ssd-detection-app:latest . \bin\bash
```

## Docker demo run flask server(used to check if the flask server works)
```
sudo docker run -it ssd-detection-app
```
## After confirming that the flask server works do:
```
sudo docker run -it -d -p 5000:5000 ssd-detection-app
```
## Inference
Now your docker runs and to get inference use below command:
```
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
```
example:response:
```
{"predictions":[{"coords":"((1606.664, 432.6262), 2050.30419921875, 2590.77685546875)","label":"dog","probability":0.9925073981285095}],"success":true}
```

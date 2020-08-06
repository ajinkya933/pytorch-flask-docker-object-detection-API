FROM anibali/pytorch:cuda-10.0

WORKDIR /ssd-det

COPY requirement.txt /ssd-det
RUN sudo apt-get update
RUN sudo apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
RUN sudo apt-get -y install sqlite3 libsqlite3-dev

RUN pip install -r ./requirement.txt

COPY . /ssd-det
RUN sudo chmod -R a+rwx /ssd-det/
RUN mkdir /home/user/data
RUN mkdir /home/user/data/coco
RUN cp data/coco_labels.txt /home/user/data/coco

EXPOSE 5000

CMD ["python","app.py"]~

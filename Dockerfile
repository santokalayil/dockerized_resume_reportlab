FROM ubuntu

# RUN apt-get update
# RUN sudo apt update && sudo apt upgrade -y
# RUN apt install software-properties-common -y
# RUN add-apt-repository ppa:deadsnakes/ppa -y
# RUN apt update
# RUN apt install python3.10 -y
# RUN apt install python3-pip -y

# RUN mkdir project 

COPY files_to_be_copied/install.sh /project/install.sh
COPY files_to_be_copied/requirements.txt /project/requirements.txt

RUN cd project

RUN chmod +x /project/install.sh
RUN /project/install.sh
RUN python3 -m pip install -r /project/requirements.txt

RUN rm /project/install.sh
RUN rm /project/requirements.txt

# mounting folder directly using dockerfile
# ADD project/ /project/

# RUN cd project && python3 main.py
#!/bin/bash
PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env

if [ ! -e ${VENV} ];then
    virtualenv ${VENV} 
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}
export PROJ_DIR

export MAIL_USERNAME=<your username>
export MAIL_PASSWORD=<your password>
export FLASK_ADMIN=<your emailaddress>

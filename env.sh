#!/bin/bash
PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env

if [ ! -e ${VENV} ];then
    virtualenv ${VENV} 
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}/app/:${PROJ_DIR}
export PROJ_DIR

#export MAIL_USERNAME='1505586488'
#export MAIL_PASSWORD='qcegjiyfdpxnjcab'
#export FLASK_ADMIN='1505586488@qq.com'

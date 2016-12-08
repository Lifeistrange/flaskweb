#!/bin/bash
PROJ_DIR=`pwd`
VENV=${PROJ_DIR}/.env

if [ ! -e ${VENV} ];then
    virtualenv ${VENV} 
fi

source ${VENV}/bin/activate 

export PYTHONPATH=${PROJ_DIR}/www/:${PROJ_DIR}
export PROJ_DIR


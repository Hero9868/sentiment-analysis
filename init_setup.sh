echo [$(date)]: "START"


echo [$(date)]: "creating env with python" 


conda create --prefix ./env python=3.12 -y

# pixi init env
# cd env
# pixi add python


echo [$(date)]: "activating the environment" 

source activate ./env

# pixi shell

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements_dev.txt

echo [$(date)]: "END" 
#! /bin/bash

pip3 install pytest
python -m pytest --version
python -m pytest ./service1 --cov ./service1/application
python -m pytest ./service2 --cov ./service2/application

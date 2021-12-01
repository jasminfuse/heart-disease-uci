# Heart Disease Prediction 

This repository contains the implementation of heart disease prediction system on [Heart Disease UCI](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

## Build on Local Device

The easiest way to do this is in a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). 

### Create a Virtual Environment

Once you have `virtualenv` installed, create a virtual environment to hold Pelican and its dependencies:

    $ virtualenv .venv
    $ source .venv/bin/activate

This creates a virtual environment and then activates it. If you want to exit the virtual environment, type:

    $ deactivate

### Clone the Repository

    $ git clone https://github.com/jasminfuse/heart-disease-uci.git

Now get inside the project folder

    $ cd heart-disease-uci

### Install Pelican & Dependancies
Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

    $ pip install -r requirements.txt

### Run Flask Application

    $ python app.py

This runs the project in port [5000](http://localhost:5000/) of your local device.
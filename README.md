# rasa-weather-assistant

This is a demo weather assistant created with [Rasa](https://rasa.com/) framework.

This system uses the [OpenWeatherMap](https://openweathermap.org/) API to fetch real time weather data. You just need to sign up there and provide `actions/actions.py` with your personal API token.

## Installation

Install Rasa in a clean virtual environment using pip.

```
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip3 install -U pip
$ pip3 install rasa
```

## Usage

Train your model using:
```
$ rasa train
```

Start the API action server with which the model communicates:
```
$ rasa run actions
```

Talk with your bot throught command line with:
```
$ rasa shell
```

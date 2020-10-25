[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/yanehi/raspberrypi-cocktailmachine)]()
[![Forks](https://img.shields.io/github/forks/yanehi/raspberrypi-cocktailmachine)]()
[![Forks](https://img.shields.io/github/stars/yanehi/raspberrypi-cocktailmachine)]()
[![Cocktailmachine](https://img.shields.io/badge/cocktailmachine-mixing-blueviolet)]()

# Project Cocktailmachine

If you've always wanted to build your own cocktailmachine, then you've come to the right place. Here you find all you need, from the accesoires to the code. 
More specific information about testing, existing routes and our data model you will find in our wiki.

## Build status

For continuous integration we use Travis-CI. In our pipeline we use [flake8](https://flake8.pycqa.org/en/latest/), [pytest](https://docs.pytest.org/en/stable/) and [codecav](https://codecov.io/).

[![Build Status](https://travis-ci.com/yanehi/raspberrypi-cocktailmachine.svg?branch=master)](https://travis-ci.org/yanehi/raspberrypi-cocktailmachine)

## Code style

In our python backend we use flake8 for coding guidelines. 

[![codecov](https://codecov.io/gh/yanehi/raspberrypi-cocktailmachine/branch/master/graph/badge.svg?token=7J43OC52VU)](https://codecov.io/gh/yanehi/raspberrypi-cocktailmachine)

## Tech/framework used

* *Backend*
    * Python: [Fastapi](https://fastapi.tiangolo.com/), [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
    * MongoDB
* *Frontend*
    * ...

## Screenshots

For the access of the GPIOs from the raspberry we use [RPi.GPIO](https://pypi.org/project/RPi.GPIO/).
We use the GPIOS: 18, 23, 24, 25.

![Fritzing](cocktail_leds_bb.png)

## API Reference

For the REST API we use [FastAPI](https://fastapi.tiangolo.com/)

## Commit Guide and Branching

* we use the [Angular commit guide](https://github.com/angular/angular/blob/master/CONTRIBUTING.md).
* branch names: `<issue-number>`-issue-name

## How to use?

Look at  [setup pi](./setup pi_three.sh) to prepare your `RaspberryPi3+` with the prerequisites you need.
* try also with [setup pi](./setup pi_zero.sh) to prepare your `RaspberryPi Zero W`

### Local development

* install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)
* run the containers in `docker/development`

```
docker-compose up
```

* access `mongo-express`

```
http://0.0.0.0:8081
```

* fastapi `mongo-express`

```
http://0.0.0.0:8000
```

## License

MIT

## Contributors

* [Janosch Fischer](https://github.com/janosch09)
* [Yannic Nevado](https://github.com/yanehi)




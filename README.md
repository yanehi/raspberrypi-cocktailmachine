# Projekt Cocktailmachine

## How to Run

* install python3.8
    * windows: https://www.djangoproject.com/download/
    * debian/ubuntu: `apt-get install python3.8`

* clone project
    * `git clone git@github.com:janosch09/cocktail-pi.git`

* create `virtualenv` for your project dependencies

* install dependencies

    * `pip install -r requirements.txt`

* make and apply migrations
    ```
    python manage.py migrate
    ```

* run your application and access over `http://localhost:8000 aufrufen`
`python manage.py runserver`

## UI Framework

https://materializecss.com

## Model

**Ingredient**

- name (String) : Name of the ingredient (Example: "Cola")
- position (int): To which Dispenser is the ingredient connected. If not connected the value is -1

**Recipe**

- name (String) : Name of Cocktail / Recipe
- ingredients (List<Ingredient>): list of all Ingredients


## Backend

For the access of the GPIOs from the raspberry we use [RPi.GPIO](https://pypi.org/project/RPi.GPIO/).
We use the GPIOS: 18, 23, 24, 25

![Fritzing](cocktail_leds_bb.png)

## API

## Commit Guide

We use the [Angular commit guide](https://github.com/angular/angular/blob/master/CONTRIBUTING.md).

## RaspberryPi Zero Setup

Prepare your RaspberryPi Zero with our [setup file](./Setup_pi.md).

## Contributors

Janosch Fischer
Yannic Nevado




# proj4-brevets

_Kory Schneider_

_CIS 322, Fall 2016_


## What is this?

This is a Randonneurs USA (RUSA) controle time calculator made with flask and ajax.

## Installation

Clone the repository:

    $ cd where/you/want/it
    $ git clone https://github.com/koryschneider/proj4-brevets
    $ cd proj4-brevets

Then set it up and run it:

    $ bash ./configure && make service


## Usage
`$ make service` will start a Green Unicorn (gunicorn) server, which is more suitable for running over a long period of time.

`$ make run` will launch the server in debugging mode.

`$ make test` will run the test suite.

## Algorithm & Rules

For an explanation of the algorithms used, see https://rusa.org/octime\_alg.html. For an in-depth look at the rules, see https://rusa.org/pages/rulesForRiders.

## Credit

Forked from Michal Young at https://github.com/UO-CIS-322/proj4-brevets for CIS 322: Intro to Software Engineering.

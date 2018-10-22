# Dash Table 3.0
Advanced Table component for [Dash](https://dash.plot.ly/).

## Setup
1. Install Node v8+
2. Install CircleCI CLI (https://circleci.com/docs/2.0/local-cli/)

`npm install`

## Local Demo 
#### Local Server JS Example (Hot reload)
Use to verify the frontend functionality of the table during development or initial testing. This will run the example in the `/demo` directory.

1. Run `npm run build.watch`
2. Visit [http://localhost:8080/](http://localhost:8080/)
#### Local Server Review Apps
Use the review apps to verify callback functionality (note these examples are written in python: the end-user syntax). This will run `index.py` found in the root of the directory and run the examples found in: `/tests/dash/`. To add more examples create a .py file in the `/tests/dash/` directory prepended with `app_` ie: `app_your_example.py`. This example will automatically get added to the example index page.
1. From the root of the directory run `gunicorn index:server`
2. Visit [http://127.0.0.1:8000](http://localhost:8000)

## Running Tests
#### Run tests locally
`npm test`
#### Run locally with hot reload:
`npm run test.watch`
#### Run tests in CircleCI CLI
`circleci build --job test`

## Local Build
`npm run build:js && npm run build:py`

## Local Dist Build
python setup.py sdist

Note: Distributable file will be located in ./dist

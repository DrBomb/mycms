# MyCMS

## What is my cms?

My CMS will be a Content-Managin-System developed by myself, using Flask as a backend and React as a frontend.

I'm making this out or a personal project, I know there must be multitude of CMS' which can do better than mine, but this is an excercise for me too.

## Environment

As I plan to use React, both node and python are needed for compiling/developing MyCMS.

The environment right now has webpack configured as a webserver for the compiled JS files, with the added value of reloading even when using Flask's dev server.
This is done by requesting only the compiled JS to the webpack dev server and the rest being served by flask, this is only enabled by setting the REACT env variable to the 
webpack address:

```
export REACT=http://localhost:3333
```

This is managed all automatically by Python's [Honcho](https://pypi.python.org/pypi/honcho)

## Setting up the test enviroment

1. First clone the repository
   ```
   git clone X
   cd mycms
   ```

2. Install nodejs, then the dependencies
   ```
   sudo apt-get install nodejs
   
   ```
   Which will install nodejs and the package manager `npm`

3. Install globally webpack and webpack-dev-server, then the rest of dependencies locally
   ```
   sudo npm install webpack webpack-dev-server -g
   npm install
   ```

4. Now make a virtualenv and store our python packages
   ```
   virtualenv mycms
   cd mycms
   source ./bin/activate
   pip install -r requirements.txt
   ```

5. That's it! Now from the root directory run `honcho start` to start both the webpack server and the flask dev server
   * Access your website via `http://localhost:5000`

## Structure

* /
*   /mycms
*   /mycms/App.py           Flask App
*   /mycms/entry.py         Entry point from which the app's WSGI object is exposed
*   /mycms/jsx              JSX (React) Sources, they all get compiled to:
*   /mycms/static/bundles   This folder, which is not watched by version control
*   /mycms/templates        Jinja templates

## Reloading

Running the dev server via `honcho start` will enable reloading, so if you make changes to any file on the jsx folder, they will get compiled and shown back!

## Production

If you want to compile the final .js needed for actual deployment, run `webpack` on the root of the repo and it'll compile them for you

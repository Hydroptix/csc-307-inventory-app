# Song Playlist Manager

View songs, and add them to playlists! Register a username, then login and view a global list of user-created playlists. View the entire list of songs, then add them to each playlist as you see fit. Got tired of one of the songs in a playlist? Just open the playlist and remove it. Want a new category to organize some songs? Just add a new playlist! Playlist management made simple.

## Travis CI Builds

![](https://travis-ci.org/Hydroptix/csc-307-inventory-app.svg?branch=master)

[https://travis-ci.org/github/Hydroptix/csc-307-inventory-app](https://travis-ci.org/github/Hydroptix/csc-307-inventory-app)

## Project diagrams

[https://github.com/Hydroptix/csc-307-inventory-app/wiki/Diagrams](https://github.com/Hydroptix/csc-307-inventory-app/wiki/Diagrams)

## Code Style:
  We have decided to use the original Python style guide and the JavaScript standard style.

## IDE Setup:

### Initial repo setup

Clone the repo with `git clone https://github.com/Hydroptix/csc-307-inventory-app.git`!

### Python/Pycharm

#### Open the project

1. Open Pycharm
2. Click Open
3. Navigate to your local copy of the repo
4. Select the backend folder and click Ok (ensures your project root is correct)

#### Pipenv/virtualenv setup

1. Open the settings dialog (File->Setting or Ctrl+Alt+S on Windows)
2. Navigate to Project: backend->Python Interpreter
3. Click the gear icon in the top right of the windown and select Add...
4. Select Pipenv Environment from the left menu
5. Select a Python 3.7 base interpreter from your system
6. Click Ok
7. On the Python Interpreter page, select the new Pipenv (backend) interpreter from the dropdown at the top of the window
8. Click Ok
8. Pycharm will now create a virtual environment and install all the dependencies needed to run the backend

#### Run configuration

1. From the main project layout, select Edit Configurations... dropdown
2. Click the + button at the top left of the window and select Flask Server from the dropdown list
3. Set Target Type to Module name
4. Set Target to `backend_db_connections`
5. Check the FLASK_DEBUG box if you want to debug the server
6. Click Ok

#### Style setup

  Pycharm uses the Python style guide by default, including listing the python style guide rule numbers for violations. If you changed Pycharm's style checking manually, here's how to reset it to the default:
1. Open the settings dialog (File->Setting or Ctrl+Alt+S on Windows)
2. Expand the Editor dropdown and select Code Style
3. Click the gear at the top of the window and select Restore Defaults

### Javascript/Webstorm

#### Open the project

1. Open Webstorm
2. Click Open
3. Navigate to your local copy of the repo
4. Select the frontend folder and click Ok (ensures your project root is correct)

#### Install dependencies

1. Right click the package.json file from the file explorer
2. Select Run 'npm install' from the dropdown

#### Run configuration

1. Select the Edit Configurations... dropdown at the top of the project window
2. Click the + at the top left corner of the window and select npm
3. Click Ok

#### Style setup

Webstorm makes it easy to use the JavaScript standard style rules for formatting. The process is similar to the steps for Pycharm as they are both Intellij-based IDEs.
1. Open the settings dialog (File->Setting or Ctrl+Alt+S on Windows)
2. Expand the Editor dropdown, expand the Code Style dropdown, and select JavaScript.
3. Click the Set from... link at the upper right side of the page and select JavaScript Standard Style.

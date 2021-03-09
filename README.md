# VotesToSkipMusic
Voting app that used to skip music on public demand

Homepage

![LCO Mascot](https://i.ibb.co/bQLd7kR/homepage.png "LCO")

Create Room

![LCO Mascot](https://i.ibb.co/C1fKHsG/createroom.png "LCO")

Join Room

![LCO Mascot](https://i.ibb.co/fS3H4Hq/joinroom.png "LCO")

Create Room with Spotify

![LCO Mascot](https://i.ibb.co/tpv9Fxc/Login-with-spotify.png "LCO")

### Features

* User create room with Spotify

* Room admin can change the song with Spotify

* Joining user can add votes to skip the song

* More the votes the song gets changed automatically

# Getting Started

To start the backend

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/Yogeshshirsath01/VotesToSkipMusic
    $ cd {{ VotesToSkipMusic }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


## To start the frontend


Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npx json-server --watch data/db.json --port 8000`

To connect with the database and runing it on localhost.\

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.


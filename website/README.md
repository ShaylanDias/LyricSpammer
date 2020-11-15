# TikTokBikBok Server
Serves the frontend and acts as an intermediary to forward API requests after adding the API keys, as well as control
requests sent per second by user. Additionally, could be used to serve ads and do other integration.

## Deployment
The key here is the git repo takes up the whole project including the app folder, while Heroku will only register it as an
app if it sees the `Procfile` file at the upper level. This means deployment is a little different than normal.
1. Navigate to the very upper level of the git repo. This is currently the `TikTokBikBok`
2. Run the command: `git subtree push --prefix website/ heroku master`
    1. This pushes only this subtree (folder/directory) inside `TikTokBikBok/website/` to the remote, thus the Heroku remote
    will only see the Flask project and not the app folder.
    
 ## Running Locally
 1. Set up a virtual environment: `python3 -m venv .venv`
 2. `source .venv/bin/activate && pip3 install -r requirements.txt`
 3. Add a .env file and input your API Key for http://ws.audioscrobbler.com/2.0/': `secret_key=<key>`
 4. `flask run`

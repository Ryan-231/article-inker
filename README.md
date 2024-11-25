# Article Inker
A local tool used for generating a short starting passage for inspiration while writing. 4 genres are available, being drama, horror, poetry, and dad jokes.

This project was built using omni, a scaffold for deploying dockerized flask applications: [https://github.com/organization-x/omni](https://github.com/organization-x/omni)

### Installation and setup
This tool requires Python 3.10.x to run, so make sure you have that installed. It also requires the `pip` package manager, which can be installed [here](https://pip.pypa.io/en/stable/installation/) if it didn't come with your Python installation. This project was built with Python 3.10.5 and pip 22.0.4, but any modern version of Python3 and pip should work fine.

Download the source code as a .zip archive and extract it.

cd into the `/app/model` folder and replace `model.txt` with the contents of the folder at the link.

Do the same for `/app/aitextgen/aitextgen.txt`.

cd back into `/app/` and run `python3 -m pip install -r requirements.txt` to install all dependencies. The important ones are aitextgen and flask, so you may want to make sure those are installed and up to date by running
`pip install -u Flask`
and
`pip3 install -u aitextgen`

Line 34 of `/app/main.py` contains the port that this project will run on, and line 157 contains its url. If you want to run multiple projects at once, or if you want to run this on a remote server, you might want to change the port number and url, respectively. The port is by default `12345`, and the url is by default `localhost`.

From `/app/`, run `python3 -m main` to start the server locally. Changes made will usually be picked up in realtime by the server. 

If you want to deploy it with docker, instructions and common issues can be found at [https://github.com/organization-x/omni]([https://github.com/organization-x/omni) under "Quickstart Guide for Local Deployment" and "Common Issues", respectively.

# Article Inker
A local tool used for generating a short starting passage for inspiration while writing. 4 genres are available, being drama, horror, poetry, and dad jokes.

This project was built using omni, a scaffold for deploying dockerized flask applications: [https://github.com/organization-x/omni](https://github.com/organization-x/omni)

### Prerequites
This tool requires Python 3.10.x to run and the `pip` package manager, which can be installed [here](https://pip.pypa.io/en/stable/installation/).

### Installation and setup
Download the source code as a .zip archive and extract it.

-Run `cd app/model`

-Open the link in the `model.txt` file.

-Copy the contents of the folder at that link into the `app/model/` folder and delete `model.txt.`

-Run `cd /app/aitextgen` 

-Open the link in the `aitextgen.txt` file.

-Copy the contents of the folder at that link into the `app/aitextgen/` folder and delete `aitextgen.txt.`

-Run           
`cd /app`<br>
`python3 -m pip install -r requirements.txt`   
`pip install -u Flask`      
`pip3 install -u aitextgen`            

### Launching the project
Run `python3 -m main` from the `app/` folder to start the server locally. Changes made will usually be picked up in realtime by the server. Input a genre and a couple starting words, click generate, and the tool will generate a short passage based on your genre and prompt.

### TODO:
Add functionality for deploying using Docker.
Store models and model artifacts in an S3 bucket to streamline user installation.
Deploy project online.

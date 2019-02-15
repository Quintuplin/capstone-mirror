# capstone-2019-nist

## The team: 
* Dylan Cowden
* Misae Evans
* Jack Fraser

## Explanation of Files in this Repository: 
### mysql directory 
* Dockerfile: the dockerfile for the image
* createdata.sql: creates a database
* createuser.sql: creates a user for the database 
### rshiny directory
* Dockerfile: the dockerfile for the image
* shiny-server.sh: ensures a directory for the web app
### buildContainer-playbook.yml
* ansible script that builds docker images, contaienrs and network to link containers. 
### clean-docker.sh
* script that cleans local system of all docker images and contaienrs for testing.

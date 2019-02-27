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
### buildContainer-playbook.yml
* ansible script that builds docker images, containers and network to link containers. 
### clean-docker.sh
* script that cleans local system of all docker images and contaienrs for testing.

## To Run Shiny Container
* navigate to browser of choice
>  localhost:80

## To add apps 
* go to ./srv/shiny-server/
* add the following dirs mountpoints/apps/name-of-app/ 
* in name-of-app add UI.R and server.R 

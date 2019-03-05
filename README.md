# capstone-2019-nist
<<<<<<< HEAD

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

## Drag and Drop Dependencies
* must have R version 3.5
### How To: 
1. Check ubuntu version 
> lsb_release -a
2. add pub key to your system if you don't already have one 
> sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
3. go to /etc/apt/sources.list

4. for 18.04 version add this line to the sources.list file  <br />
> deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/  <br />

4a. for 16.04 version add this line to the sources.list file  <br />
> deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/  <br />

4b. If your ubuntu distro is older than 16.04... dude upgrade  <br />

5. Update and intall  <br />
> sudo apt-get update  <br />
> sudo apt-get install r-base r-base-dev <br />
> sudo apt-get upgrade <br />
6. Clean your system up <br />
> sudo apt-get remove -y 'r-cran-*' <br />
7. open up R and type this in console 
>update.packages(ask = FALSE) <br />
8. Still in R Console <br />
> BiocManager::install() <br />
9. Make sure it worked by typing this in console.. a bunch of stuff should pop up <br />
> BiocManager::available()
10. one more check in the R console (should come back TRUE) <br />
> BiocManager::valid() <br />
11. Install this guy (MzR package) *This is a big package- will take time, try not to have to many things running while this is going. It froze my PC up 3 times*
> BiocManager::install("mzR", version = "3.8") <br />
12. Check that it worked by trying to access the documentation for MZR <br />
> browseVignettes("mzR") <br />
=======
# other files too large to upload on git
>>>>>>> 52583442b547abd8f7af40c175078c5dd6b3ddab

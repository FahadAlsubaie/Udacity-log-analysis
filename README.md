## **Log Analysis Project**

This project was made by Fahad Alsubaie 

## **About**
This is full stack developer project for udacity course provided by Misk Foundation, in this project we were supposed to build an internal report tool for newspaper articles to find data about the visitors of the site and others.

## prerequisites
you need to have those installed on your computer.

 - Python 3  
 - VirtualBox 
 - Vagrant

## setting up

 - Install all of the above 
 - Download this tool inside vagrant

## Launch
start up the vagrant VM by running  

> Vagrant up

it will take a while if it's your first time 
then run 

> Vagrant ssh 

to log in to your VM and to load your data run this command 

> psql -d news -f newsdata.sql

and last to execute the program run 

> python Log-Analysis-Project.py
> 
> python3 Log-Analysis-Project.py

depending on your python path.



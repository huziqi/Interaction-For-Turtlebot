Interaction-For-Turtlebot
========== 
How to complie  
----------  
Make sure you have already install ROS and Turtlebot. The tutorial for installing ROS and Turtlebot: [installation](http://wiki.ros.org/)  
Git clone to your workspace,and make. 

    cd ~/your_workspace/
    catkin_make
    
Test the Server and Client on ROS
----------
Server and Client are important components in ROS system. They connects each nodes with information published by Rostopic.
The code in this project make a demo of how to use server and client.  
Task: Through user's inputs controling turtlebot whether to follow the people.  
* follow_client.cpp  
* follow_client.py

Speech on Turtlebot
---------
In this part I use two methods to test the speech function on turtlebot  

###Soud_play

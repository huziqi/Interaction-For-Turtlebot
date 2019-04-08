Interaction-For-Turtlebot
========== 
How to complie  
----------  
Make sure you have already install ROS and Turtlebot. The tutorial for installing ROS and Turtlebot: [installation](http://wiki.ros.org/)  
Git clone to your workspace,and make. 

    cd ~/<your_workspace>/
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

### Soud_play
The sound_play node considers each sound (built-in, wave file or synthesized text) as an entity that can be playing, playing repeatedly or stopped. Nodes change the state of a sound by publishing to the robotsound topic. Multiple sounds can be played at once.  
Download the example code :

        cd ~/<your_workspace>/src
        git clone https://github.com/robocupathomeedu/rc-home-edu-learn-ros.git
        cd ..
        catkin_make
        
* installation

        sudo apt-get install ros-kinetic-audio-common
        sudo apt-get install libasound2
* Command line operation

        roscore
        rosrun sound_play soundplay_node.py
        rosrun sound_play say.py "Hello"
* Source code implementation:

        rosrun rchomeedu_speech sound_test.py
        roslaunch rchomeedu_speech sound_test.launch
        
### Pocketsphinx
CMUSphinx is an open source package which aimed at offline speech recognition.  
* Installation Pocketsphinx

        sudo apt-get install python-pip python-dev build-essential
        sudo pip install --upgrade pip
        sudo apt-get install libasound-dev
        sudo apt-get install python-pyaudio
        sudo pip install pyaudio
        sudo apt-get install swig
        sudo pip install pocketsphinx
* Install ROS package for Pocketsphinx

        cd ~/<your_workspace>/src
        git clone https://github.com/Pankaj-Baranwal/pocketsphinx
        cd ..
        catkin_make
* Add language model
    * Download and copy the hub4wsj_sc_8k language model to /usr/local/share/pocketsphinx/model/en-us/en-us/
    * http://sourceforge.net/projects/cumsphinx/files/Acoustic%20and%20Language%20Models/Archive/US%20English%20HUB4WSJ%20Acoustic%20Model/
* Demonstration of lm mode(language model mode):

        roslaunch rchomeedu_speech lm.launch dict:=/home/<username>/catkin_ws/src/rc-home-edu-learn-ros/rchomeedu_speech/robocup/robocup.dic lm:=/home/<username>/catkin_ws/src/rc-home-edu-learn-ros/rchomeedu_speech/robocup/robocup.lm
        rostopic echo /lm_data
* Creating a Vocabulary:

        roscd rchomeedu_speech/robocup
        less robocup.corpus
    * http://www.speechcs.cum.edu/tools/lmtool-new.html
    * Update dic and lm files in launch file(lm.launch)
    
### 科大讯飞
* Installation

        cd ~
        git clone https://github.com/ncnyn/xf-ros.git
        cp -R xf-ros/xfei_asr ~/<your_workspace>/src/
* in xfei_asr/Cmakelist.txt:
    
        /home/ubu/<your_workspace>/ >>> /home/<username>/<your_workspace>/  
        
        cd ~/<your_workspace>
        catkin_make
* TTS speech make up:

        roscore
        rosrun xfei_asr tts_subscribe_speak
        rostopic pub xfwords std_msgs/String "你好"
* Speech recognition:

        rosrun xfei_asr iat_record
        
* In this project I make a demo using 科大讯飞 achieving a task that computer can first recognition your speech and then repeat what you said by online speech making up.
    * iat_publish_speak.cpp
    * tts_subscribe_speak.cpp
       
            

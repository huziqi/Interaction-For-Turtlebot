#include <ros/ros.h>
#include <cstdlib>
#include<iostream>
#include "turtlebot_msgs/SetFollowState.h"



using namespace std;


int main(int argc, char **argv)
{
  ros::init(argc, argv, "follow_client");
  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<turtlebot_msgs::SetFollowState>("/turtlebot_follower/change_state");
  turtlebot_msgs::SetFollowState req;
  ros::Rate loop_rate(10);
  while(ros::ok())
  {
    cout<<"//if you want to start follower please enter f,"<<endl;
    cout<<"//if you want to stop follower please enter s"<<endl;

    char swi;
    cin>>swi;
    if(swi=='f')
    {
        req.request.state=1;
    }
    if(swi=='s')
    {
        req.request.state=0;
    }
    if (client.call(req))
    {
        ROS_INFO("called the server!!!!!!!!!!!!!!!");
    }
    // else
    // {
    //     ROS_ERROR("Failed to call service!!!!!!!!!");
    //     return 1;
    // }
    //ros::spinOnce();
    cout<<endl;
    //loop_rate.sleep();
  }


  return 0;
}
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="yolo_test_world">
    <include>
      <uri>model://sun</uri>
    </include>
    <include>
      <uri>model://ground_plane</uri>
    </include>
    <include>
      <name>person_standing</name>
      <uri>model://person_standing</uri>
      <static>true</static>
      <pose>3.2 5.7 0 0 0 -0.35</pose>
    </include>
    <include>
      <name>suv</name>
      <uri>model://suv</uri>
      <static>true</static>
      <pose>8 7 0 0 0 -1.57</pose>
    </include>    
    <include>
      <name>stop_sign</name>
      <uri>model://stop_sign</uri>
      <static>true</static>
      <pose>7.2 -2 0 0 0 -1.61</pose>
    </include>  
    <include>
      <name>prius_hybrid</name>
      <uri>model://prius_hybrid</uri>
      <static>true</static>
      <pose>11 -6 0 0 0 -1.1</pose>
    </include> 
    <include>
      <name>bus</name>
      <uri>model://bus</uri>
      <static>true</static>
      <pose>17 3 0 0 0 -1.1</pose>
    </include> 
    <include>
      <name>postbox</name>
      <uri>model://postbox</uri>
      <static>true</static>
      <pose>3.5 -7 0 0 0 -3.1</pose>
    </include> 
  </world>
</sdf>


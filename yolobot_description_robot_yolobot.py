<?xml version="1.0" ?>
<!-- =================================================================================== -->
<!-- |    This document was autogenerated by xacro from box_bot.xacro                  | -->
<!-- |    EDITING THIS FILE BY HAND IS NOT RECOMMENDED                                 | -->
<!-- =================================================================================== -->
<robot name="yolobot">
  <material name="black">
    <color rgba="0.0 0.0 0.0 1.0"/>
  </material>
  <material name="blue">
    <color rgba="0.203125 0.23828125 0.28515625 1.0"/>
  </material>
  <material name="green">
    <color rgba="0.0 0.8 0.0 1.0"/>
  </material>
  <material name="grey">
    <color rgba="0.2 0.2 0.2 1.0"/>
  </material>
  <material name="orange">
    <color rgba="1.0 0.423529411765 0.0392156862745 1.0"/>
  </material>
  <material name="brown">
    <color rgba="0.870588235294 0.811764705882 0.764705882353 1.0"/>
  </material>
  <material name="red">
    <color rgba="0.80078125 0.12890625 0.1328125 1.0"/>
  </material>
  <material name="white">
    <color rgba="1.0 1.0 1.0 1.0"/>
  </material>
  <gazebo reference="chassis">
    <material>Gazebo/Blue</material>
  </gazebo>
  <gazebo reference="left_wheel">
    <kp>1000.0</kp>
    <kd>1000.0</kd>
    <mu1>0.5</mu1>
    <mu2>0.5</mu2>
    <material>Gazebo/Blue</material>
  </gazebo>
  <gazebo reference="right_wheel">
    <kp>1000.0</kp>
    <kd>1000.0</kd>
    <mu1>0.5</mu1>
    <mu2>0.5</mu2>
    <material>Gazebo/Blue</material>
  </gazebo>
  <!-- ros_control plugin -->
  <gazebo>
    <plugin filename="libgazebo_ros_control.so" name="gazebo_ros_control">
      <robotNamespace>/yolobot</robotNamespace>
      <robotParam>/robot_description</robotParam>
      <robotSimType>gazebo_ros_control/DefaultRobotHWSim</robotSimType>
    </plugin>
  </gazebo>
  <gazebo>
    <plugin filename="libgazebo_ros_diff_drive.so" name="differential_drive_controller">

      <ros>
        <namespace>/yolobot</namespace>
      </ros>

      <!-- wheels -->
      <left_joint>joint_right_wheel</left_joint>
      <right_joint>joint_left_wheel</right_joint>

      <!-- kinematics -->
      <wheel_separation>0.1</wheel_separation>
      <wheel_diameter>0.025</wheel_diameter>

      <!-- limits -->
      <max_wheel_torque>0.1</max_wheel_torque>
      <max_wheel_acceleration>1.0</max_wheel_acceleration>

      <!-- output -->
      <publish_odom>true</publish_odom>
      <publish_odom_tf>true</publish_odom_tf>

      <odometry_frame>odom</odometry_frame>
      <robot_base_frame>chassis</robot_base_frame>


    </plugin>
  </gazebo>
  <!-- imu -->
  <gazebo>
    <plugin filename="libgazebo_ros_imu.so" name="gazebo_ros_imu_controller">
      <robotNamespace>/yolobot/</robotNamespace>
      <topicName>imu/data3</topicName>
      <serviceName>imu/service</serviceName>
      <bodyName>chassis</bodyName>
      <gaussianNoise>0</gaussianNoise>
      <rpyOffsets>0 0 0</rpyOffsets>
      <updateRate>50.0</updateRate>
      <alwaysOn>true</alwaysOn>
      <gaussianNoise>0</gaussianNoise>
    </plugin>
  </gazebo>

  <link name="base_link">
      </link>
  <link name="chassis">
    <!-- pose and inertial -->
    <pose>0 0 0 0 0 0</pose>
    <inertial>
      <mass value="1.0"/>
      <origin rpy="0 0 0" xyz="0 0 -0.025"/>
      <inertia ixx="0.00033333333333333343" ixy="0" ixz="0" iyy="0.00033333333333333343" iyz="0" izz="0.00033333333333333343"/>
      <inertia ixx="0.000241935" ixy="0" ixz="0" iyy="0.000241935" iyz="0" izz="0.000241935"/>
    </inertial>
    <!-- body -->
    <collision name="collision_chassis">
      <geometry>
        <box size="0.2 0.1 0.05"/>
      </geometry>
    </collision>
    <visual name="visual_chassis">
      <geometry>
        <box size="0.2 0.1 0.05"/>
      </geometry>
    </visual>
  </link>
  <gazebo reference="chassis">
    <material>Gazebo/Red</material>
  </gazebo>
  <joint name="base_link_joint" type="fixed">
    <origin rpy="0 0 0" xyz="0 0 0"/>
    <parent link="base_link"/>
    <child link="chassis"/>
  </joint>


  <!-- CAMERA-->
  <link name='rgb_cam_camera_link'>
		<visual>
			<origin xyz="0 0 0" rpy="0 0 0"/>
			<geometry>
				<box size="0.02 0.04 0.01"/>
			</geometry>
		</visual>
	</link>

  <joint name="rgb_cam_camera_link_joint" type="fixed">
		<origin rpy="0 0 0" xyz="0.04 0.0 0.5"/>
		<parent link="chassis"/>
		<child link="rgb_cam_camera_link"/>
	</joint>


    <link name="rgb_cam_camera_link_frame">
    </link>

    <joint name="rgb_cam_camera_frame_joint" type="fixed">
        <origin xyz="0.01 0 0" rpy="0 0 0" />
        <parent link="rgb_cam_camera_link" />
        <child link="rgb_cam_camera_link_frame" />
        <axis xyz="0 0 0"/>
    </joint>

    <gazebo reference="rgb_cam_camera_link_frame">
      <sensor type="camera" name="rgb_cam">
        <always_on>1</always_on>
        <update_rate>10.0</update_rate>
        <camera name="rgb_cam">
            <pose>0 0 0 0 0 0</pose>
            <horizontal_fov>1.3962634</horizontal_fov>
            <image>
             <width>640</width>
             <height>480</height>
             <format>R8G8B8</format>
            </image>
            <clip>
                <near>0.005</near>
                <far>20.0</far>
            </clip>
        </camera>
        <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
            <alwaysOn>true</alwaysOn>
            <updateRate>0.0</updateRate>
            <cameraName>rgb_cam</cameraName>
            <imageTopicName>image_raw</imageTopicName>
            <cameraInfoTopicName>camera_info</cameraInfoTopicName>
            <frameName>rgb_cam_camera_link_frame</frameName>
            <hackBaseline>0.07</hackBaseline>
            <distortionK1>0.0</distortionK1>
            <distortionK2>0.0</distortionK2>
            <distortionK3>0.0</distortionK3>
            <distortionT1>0.0</distortionT1>
            <distortionT2>0.0</distortionT2>
        </plugin>
      </sensor>
    </gazebo>



  <link name="right_wheel">
    <inertial>
      <mass value="0.2"/>
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <inertia ixx="3.126666666666667e-05" ixy="0" ixz="0" iyy="3.126666666666667e-05" iyz="0" izz="6.250000000000001e-05"/>
    </inertial>
    <collision name="link_right_wheel_collision">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.01" radius="0.035"/>
      </geometry>
    </collision>
    <visual name="link_right_wheel_visual">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.01" radius="0.035"/>
      </geometry>
    </visual>
  </link>
  <joint name="joint_right_wheel" type="continuous">
    <origin rpy="0 0 0" xyz="-0.05 0.05 -0.025"/>
    <child link="right_wheel"/>
    <parent link="chassis"/>
    <axis rpy="0 0 0" xyz="0 1 0"/>
    <limit effort="10000" velocity="1000"/>
    <joint_properties damping="1.0" friction="1.0"/>
  </joint>
  <link name="left_wheel">
    <inertial>
      <mass value="0.2"/>
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <inertia ixx="3.126666666666667e-05" ixy="0" ixz="0" iyy="3.126666666666667e-05" iyz="0" izz="6.250000000000001e-05"/>
    </inertial>
    <collision name="link_right_wheel_collision">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.01" radius="0.035"/>
      </geometry>
    </collision>
    <visual name="link_right_wheel_visual">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.01" radius="0.035"/>
      </geometry>
    </visual>
  </link>
  <joint name="joint_left_wheel" type="continuous">
    <origin rpy="0 0 0" xyz="-0.05 -0.05 -0.025"/>
    <child link="left_wheel"/>
    <parent link="chassis"/>
    <axis rpy="0 0 0" xyz="0 1 0"/>
    <limit effort="10000" velocity="1000"/>
    <joint_properties damping="1.0" friction="1.0"/>
  </joint>
  <!-- CASTER FRONT-->
  <link name="front_yaw_link">
    <inertial>
      <mass value="0.001"/>
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <inertia ixx="5.145833333333334e-09" ixy="0" ixz="0" iyy="5.145833333333334e-09" iyz="0" izz="1.0125000000000003e-08"/>
    </inertial>
    <collision name="link_right_wheel_collision">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.001" radius="0.0045000000000000005"/>
      </geometry>
    </collision>
  </link>
  <joint name="front_yaw_joint" type="continuous">
    <origin rpy="0 0 0" xyz="0.08 0 -0.05"/>
    <parent link="chassis"/>
    <child link="front_yaw_link"/>
    <axis xyz="0 0 1"/>
    <limit effort="1000.0" velocity="100.0"/>
    <dynamics damping="0.0" friction="0.1"/>
  </joint>
  <transmission name="front_yaw_joint_trans">
    <type>transmission_interface/SimpleTransmission</type>
    <joint name="front_yaw_joint">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
    </joint>
    <actuator name="front_yaw_jointMotor">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
      <mechanicalReduction>1</mechanicalReduction>
    </actuator>
  </transmission>
  <link name="front_roll_link">
    <inertial>
      <mass value="0.001"/>
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <inertia ixx="5.145833333333334e-09" ixy="0" ixz="0" iyy="5.145833333333334e-09" iyz="0" izz="1.0125000000000003e-08"/>
    </inertial>
    <collision name="link_right_wheel_collision">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.001" radius="0.0045000000000000005"/>
      </geometry>
    </collision>
  </link>
  <joint name="front_roll_joint" type="continuous">
    <origin rpy="0 0 0" xyz="0 0 0"/>
    <parent link="front_yaw_link"/>
    <child link="front_roll_link"/>
    <axis xyz="1 0 0"/>
    <limit effort="1000.0" velocity="100.0"/>
    <dynamics damping="0.0" friction="0.1"/>
  </joint>
  <transmission name="front_roll_joint_trans">
    <type>transmission_interface/SimpleTransmission</type>
    <joint name="front_roll_joint">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
    </joint>
    <actuator name="front_roll_jointMotor">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
      <mechanicalReduction>1</mechanicalReduction>
    </actuator>
  </transmission>
  <link name="front_pitch_link">
    <inertial>
      <mass value="0.001"/>
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <inertia ixx="4e-08" ixy="0" ixz="0" iyy="4e-08" iyz="0" izz="4e-08"/>
    </inertial>
    <collision name="front_collision">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.01"/>
      </geometry>
    </collision>
    <visual name="front_visual">
      <origin rpy="0 1.5707 1.5707" xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.01"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_pitch_joint" type="continuous">
    <origin rpy="0 0 0" xyz="0 0 0"/>
    <parent link="front_roll_link"/>
    <child link="front_pitch_link"/>
    <axis xyz="0 1 0"/>
    <limit effort="1000.0" velocity="100.0"/>
    <dynamics damping="0.0" friction="0.1"/>
  </joint>
  <transmission name="front_pitch_joint_trans">
    <type>transmission_interface/SimpleTransmission</type>
    <joint name="front_pitch_joint">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
    </joint>
    <actuator name="front_pitch_jointMotor">
      <hardwareInterface>EffortJointInterface</hardwareInterface>
      <mechanicalReduction>1</mechanicalReduction>
    </actuator>
  </transmission>
  <gazebo reference="front_pitch_link">
    <kp>1000000000000000000000000000.0</kp>
    <kd>1000000000000000000000000000.0</kd>
    <mu1>0.5</mu1>
    <mu2>0.5</mu2>
    <material>Gazebo/Green</material>
  </gazebo>
  
</robot>


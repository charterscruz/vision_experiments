import rosbag
import matplotlib.pyplot as plt
import numpy as np

filename = '/media/cruz/data/datasets/bag_files/log_test2/2022-08-25-15-02-05.bag'
# Open the bag file
bag = rosbag.Bag(filename)

# Create a dictionary to store the data for each topic
topic_data = {}

# Iterate over each topic in the bag
for topic, msg, t in bag.read_messages():
    # Check if the topic is already in the dictionary
    if topic not in topic_data:
        # If not, initialize the data list for the topic
        topic_data[topic] = []
    # Add the data for the message to the topic's data list
    topic_data[topic].append(msg)
    #print('topic')
    #print(topic)
    #print('msg')
    #print(msg)
    #print(t)

# Close the bag file
bag.close()

# Create a figure for each topic
for topic, data in topic_data.items():
    fig, ax = plt.subplots()


    # Filter out non-numerical entries
    # data = [d for d in data if isinstance(d, (int, float))]

    print(topic)
    #print(data)

    if topic=='/dji_sdk/attitude':
        q_w=[]
        q_x=[]
        q_y=[]
        q_z=[]
        for d in data:
            q_w.append(d.quaternion.w)
            q_x.append(d.quaternion.x)
            q_y.append(d.quaternion.y)
            q_z.append(d.quaternion.z)


        ax.plot(q_w)
        ax.plot(q_x)
        ax.plot(q_y)
        ax.plot(q_z)
        ax.set_title(topic)
        ax.legend(['quarternion w', 'quarternion x', 'quarternion y', 'quarternion z'])

    elif topic=='/dji_sdk/imu':
        
        ang_vel_x=[]
        ang_vel_y=[]
        ang_vel_z=[]
        lin_ace_x=[]
        lin_ace_y=[]
        lin_ace_z=[]
        orient_x=[]
        orient_y=[]
        orient_z=[]
        
        for d in data:
            ang_vel_x.append(d.angular_velocity.x)
            ang_vel_y.append(d.angular_velocity.y)
            ang_vel_z.append(d.angular_velocity.z)
            
            lin_ace_x.append(d.linear_acceleration.x)
            lin_ace_y.append(d.linear_acceleration.y)
            lin_ace_z.append(d.linear_acceleration.z)

            orient_x.append(d.orientation.x)
            orient_y.append(d.orientation.y)
            orient_z.append(d.orientation.z)


        ax.plot(ang_vel_x)
        ax.plot(ang_vel_y)
        ax.plot(ang_vel_z)
        ax.plot(lin_ace_x)
        ax.plot(lin_ace_y)
        ax.plot(lin_ace_z)
        ax.plot(orient_x) 
        ax.plot(orient_y) 
        ax.plot(orient_z)
        # ax.plot(lin_ace_x, lin_ace_y, lin_ace_z)
        # ax.plot(orient_x, orient_y, orient_z)
        ax.set_title(topic)
        ax.legend(['angular_velocity x' , 'angular_velocity y', 'angular_velocity z', 
        'linear acceleration x', 'linear acceleration y', 'linear acceleration z', 
        'orientation x', 'orientation y', 'orientation z'])
    
    elif topic == '/dji_sdk/gps_position':
        latitude =[]
        longitude = []
        altitude = []
       
        for d in data:
            latitude.append(d.latitude)
            longitude.append(d.longitude)
            altitude.append(d.altitude)
       
        ax.plot(latitude)
        ax.plot(longitude)
        ax.plot(altitude)

        ax.set_title(topic)
        ax.legend(['latitude', 'longitude', 'altitude'])
            

    elif topic == '/dji_sdk/height_above_takeoff': # TODO 
        height_above_to =[]
       
        for d in data:
            height_above_to.append(d.data)
       
        ax.plot(height_above_to)

        ax.set_title(topic)
        ax.legend(['height above take-off area'])

    elif topic == '/dji_sdk/velocity': # TODO 
        
        velocity_x = []
        velocity_y = []
        velocity_z = []
        for d in data:
            velocity_x.append(d.vector.x)
            velocity_y.append(d.vector.y)
            velocity_z.append(d.vector.z)
        
        ax.plot(velocity_x)
        ax.plot(velocity_y)
        ax.plot(velocity_z)

        ax.set_title(topic)
        ax.legend(['velocity_x', 'velocity_y', 'velocity_z'])

    #ax.plot(data)
    #ax.set_title(topic)

# Show the plots
plt.show()




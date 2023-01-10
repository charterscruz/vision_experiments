import numpy as np
import rosbag
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

filename = '/media/cruz/data/datasets/bag_files/flight_test_06012023/flight_2_3/2022-08-25-15-06-44.bag'
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

# Close the bag file
bag.close()

for topic, data in topic_data.items():

    if topic == '/dji_sdk/attitude':
        pass
    elif topic == '/dji_sdk/imu':  # high_rate
        pass
    elif topic == '/dji_sdk/gps_position':
        latitude = []
        for d in data:
            latitude.append(d.latitude)
        gps_sample_number = len(latitude)
    elif topic == '/dji_sdk/height_above_takeoff':
        pass
    elif topic == '/dji_sdk/velocity':
        pass

start_time = 1
stop_time = gps_sample_number
step = 15

# Create a figure for each topic
for topic, data in topic_data.items():

    if topic == '/dji_sdk/attitude':
        fig, ax = plt.subplots()
        q_w = []
        q_x = []
        q_y = []
        q_z = []
        for d in data:
            q_w.append(d.quaternion.w)
            q_x.append(d.quaternion.x)
            q_y.append(d.quaternion.y)
            q_z.append(d.quaternion.z)

        scl_start_time_LR = int(start_time * len(q_w) / gps_sample_number)
        scl_stop_time_LR = int(stop_time * len(q_w) / gps_sample_number)

        q_w_np = np.array(q_w)[scl_start_time_LR:scl_stop_time_LR]
        q_x_np = np.array(q_x)[scl_start_time_LR:scl_stop_time_LR]
        q_y_np = np.array(q_y)[scl_start_time_LR:scl_stop_time_LR]
        q_z_np = np.array(q_z)[scl_start_time_LR:scl_stop_time_LR]

        ax.plot(q_w_np)
        ax.plot(q_x_np)
        ax.plot(q_y_np)
        ax.plot(q_z_np)
        print('len(q_x)', len(q_x))
        print('size of q_x_np: ', np.shape(q_x_np))

        ax.set_title(topic)
        ax.legend(['quarternion w', 'quarternion x', 'quarternion y', 'quarternion z'])
        quaternion_DF = pd.DataFrame(np.transpose(np.vstack([q_w_np, q_x_np, q_y_np, q_z_np])),
                                     columns=['quaternion w', 'quaternion x', 'quaternion y', 'quaternion z'])
        quaternion_DF.to_csv(filename[:-4] + '_' + topic[9:] + '.csv')

    elif topic == '/dji_sdk/imu':  # high_rate

        ang_vel_x = []
        ang_vel_y = []
        ang_vel_z = []
        lin_ace_x = []
        lin_ace_y = []
        lin_ace_z = []
        orient_x = []
        orient_y = []
        orient_z = []
        
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

        ang_vel_x_np = np.array(ang_vel_x)
        ang_vel_y_np = np.array(ang_vel_y)
        ang_vel_z_np = np.array(ang_vel_z)
        lin_ace_x_np = np.array(lin_ace_x)
        lin_ace_y_np = np.array(lin_ace_y)
        lin_ace_z_np = np.array(lin_ace_z)
        orient_x_np = np.array(orient_x)
        orient_y_np = np.array(orient_y)
        orient_z_np = np.array(orient_z)

        scl_start_time_HR = int(start_time * len(ang_vel_x) / gps_sample_number)  # TODO change this
        scl_stop_time_HR = int(stop_time * len(ang_vel_x) / gps_sample_number)

        ang_vel_x_np = ang_vel_x_np[scl_start_time_HR:scl_stop_time_HR]
        ang_vel_y_np = ang_vel_y_np[scl_start_time_HR:scl_stop_time_HR]
        ang_vel_z_np = ang_vel_z_np[scl_start_time_HR:scl_stop_time_HR]
        lin_ace_x_np = lin_ace_x_np[scl_start_time_HR:scl_stop_time_HR]
        lin_ace_y_np = lin_ace_y_np[scl_start_time_HR:scl_stop_time_HR]
        lin_ace_z_np = lin_ace_z_np[scl_start_time_HR:scl_stop_time_HR]
        orient_x_np = orient_x_np[scl_start_time_HR:scl_stop_time_HR]
        orient_y_np = orient_y_np[scl_start_time_HR:scl_stop_time_HR]
        orient_z_np = orient_z_np[scl_start_time_HR:scl_stop_time_HR]

        fig, ax = plt.subplots()
        ax.plot(ang_vel_x_np)
        ax.plot(ang_vel_y_np)
        ax.plot(ang_vel_z_np)
        ax.set_title(topic)
        ax.legend(['angular_velocity x', 'angular_velocity y', 'angular_velocity z'])

        imu_DF = pd.DataFrame(np.transpose(np.vstack([ang_vel_x_np, ang_vel_y_np, ang_vel_z_np,
                                                      lin_ace_x_np, lin_ace_y_np, lin_ace_z_np,
                                                      orient_x_np, orient_y_np, orient_z_np])),
                              columns=['angular velocity x', 'angular velocity y', 'angular velocity z',
                                       'linear acceleration x', 'linear acceleration y', 'linear acceleration z',
                                       'orientation x', 'orientation y', 'orientation z'])
        imu_DF.to_csv(filename[:-4] + '_' + topic[9:] + '.csv')

        fig, ax = plt.subplots()
        ax.plot(lin_ace_x_np)
        ax.plot(lin_ace_y_np)
        ax.plot(lin_ace_z_np)
        ax.set_title(topic)
        ax.legend(['linear acceleration x', 'linear acceleration y', 'linear acceleration z',])

        fig, ax = plt.subplots()
        ax.plot(orient_x_np)
        ax.plot(orient_y_np)
        ax.plot(orient_z_np)
        ax.set_title(topic)
        ax.legend(['orientation x', 'orientation y', 'orientation z'])

        # print('len ang_vel_x: ', len(ang_vel_x_np))
        # print('len ang_vel_y: ', len(ang_vel_y_np))
        # print('len ang_vel_z: ', len(ang_vel_z_np))
        # print('len lin_ace_x: ', len(lin_ace_x_np))
        # print('len lin_ace_y: ', len(lin_ace_y_np))
        # print('len lin_ace_z: ', len(lin_ace_z_np))
        # print('len orient_x: ', len(orient_x_np))
        # print('len orient_y: ', len(orient_y_np))
        print('len orient_z np : ', len(orient_z_np))
        print('len orient_z: ', len(orient_z))

        # ax.plot(lin_ace_x_np, lin_ace_y_np, lin_ace_z_np)
        # ax.plot(orient_x_np, orient_y_np, orient_z_np)

    elif topic == '/dji_sdk/gps_position':  # medium rate
        fig, ax = plt.subplots()
        latitude = []
        longitude = []
        altitude = []

        for d in data:
            latitude.append(d.latitude)
            longitude.append(d.longitude)
            altitude.append(d.altitude)

        fig = plt.figure()

        graph, = plt.plot([], [], ',')

        lat_np = np.array(latitude)
        long_np = np.array(longitude)
        alt_np = np.array(altitude)

        lat_np = lat_np[start_time:stop_time]
        long_np = long_np[start_time:stop_time]
        alt_np = alt_np[start_time:stop_time]

        plt.xlim(np.min(long_np), np.max(long_np))
        plt.ylim(np.min(lat_np), np.max(lat_np))

        def animate(i):
            graph.set_data(long_np[:i*step + 1], lat_np[:i*step + 1])
            print('i: ', i*step)
            return graph

        # ani = FuncAnimation(fig, animate)
        # plt.show()

        # ax.plot(latitude)
        # ax.plot(longitude)
        # ax.plot(altitude)
        ax.plot(latitude, longitude)

        ax.set_title(topic)
        ax.legend(['latitude vs longitude', 'longitude'])

        gps_position_DF = pd.DataFrame(np.transpose(np.vstack([lat_np, long_np, alt_np])),
                                       columns=['latitude', 'longitude', 'altitude'])
        gps_position_DF.to_csv(filename[:-4] + '_' + topic[9:] + '.csv')

        fig, ax = plt.subplots()
        ax.plot(altitude)
        ax.set_title(topic)
        ax.legend(['altitude'])

    elif topic == '/dji_sdk/height_above_takeoff':
        fig, ax = plt.subplots()
        height_above_to = []
       
        for d in data:
            height_above_to.append(d.data)

        print('len height_above_to', len(height_above_to))
        height_above_to_np = np.array(height_above_to)[start_time:stop_time]
        print('len height_above_to np', np.shape(height_above_to_np))
        ax.plot(height_above_to_np)

        ax.set_title(topic)
        ax.legend(['height above take-off area'])

    elif topic == '/dji_sdk/velocity':
        fig, ax = plt.subplots()
        
        velocity_x = []
        velocity_y = []
        velocity_z = []
        for d in data:
            velocity_x.append(d.vector.x)
            velocity_y.append(d.vector.y)
            velocity_z.append(d.vector.z)

        velocity_x_np = np.array(velocity_x)[start_time: stop_time]
        velocity_y_np = np.array(velocity_y)[start_time: stop_time]
        velocity_z_np = np.array(velocity_z)[start_time: stop_time]

        ax.plot(velocity_x_np)
        ax.plot(velocity_y_np)
        ax.plot(velocity_z_np)

        ax.set_title(topic)
        ax.legend(['velocity_x', 'velocity_y', 'velocity_z'])
        print('size : velocity_x  ', np.shape(velocity_x_np))

        velocity_DF = pd.DataFrame(np.transpose(np.vstack([velocity_x_np, velocity_y_np, velocity_z_np])),
                                   columns=['velocity x', 'velocity y', 'velocity z'])
        velocity_DF.to_csv(filename[:-4] + '_' + topic[9:] + '.csv')
    #ax.plot(data)
    #ax.set_title(topic)

# Show the plots
plt.show()




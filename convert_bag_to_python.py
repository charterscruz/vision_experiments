import rosbag
import pandas as pd

filename = '/media/cruz/data/datasets/bag_files/log_test1/2022-08-25-17-00-11.bag'

# Read the ROS bag
bag = rosbag.Bag(filename)

# Initialize an empty list to store the data
data = []

# Iterate over the messages in the bag
for topic, msg, t in bag.read_messages():
    # Extract all the fields from the message
    msg_data = {}
    for field in dir(msg):
        # Ignore private fields (those that start with an underscore)
        if not field.startswith('_'):
            msg_data[field] = getattr(msg, field)
    # Add the topic, time stamp, and message data to the dictionary
    msg_dict = {**msg_data, 'topic': topic, 'time': t}
    # Append the dictionary to the list
    data.append(msg_dict)

# Convert the list to a Pandas dataframe
df = pd.DataFrame(data)

print(df)
print(filename[:-3])
df.to_csv(filename[:-3]+'csv', na_rep='NULL')

# df.to_excel(filename[:-3]+'xlsx', na_rep='NULL')
# df.to_xml(filename[:-3]+'xml', na_rep='NULL')

# Close the bag
bag.close()
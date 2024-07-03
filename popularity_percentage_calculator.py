# Popularity Percentage

#Find the popularity percentage for each user on Meta/Facebook. 
#The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, 
#then converted into a percentage by multiplying by 100.
#Output each user along with their popularity percentage. Order records in ascending order by user id.
#The 'user1' and 'user2' column are pairs of friends.

import pandas as pd

# Sample data
data = {
    'user1': [2, 1, 4, 1, 1, 2, 7, 8, 3],
    'user2': [1, 3, 1, 5, 6, 6, 2, 3, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 1: Calculate total number of users
all_users = pd.concat([df['user1'], df['user2']]).unique()
total_users = len(all_users)

# Step 2: Determine the number of friends each user has
friend_pairs = pd.concat([df, df.rename(columns={'user1': 'user2', 'user2': 'user1'})])
friend_counts = friend_pairs.groupby('user1').size().reset_index(name='num_friends')

# Step 3: Calculate the popularity percentage for each user
friend_counts['popularity_percentage'] = (friend_counts['num_friends'] / total_users) * 100

# Step 4: Output the result ordered by user_id
result = friend_counts.rename(columns={'user1': 'user_id'}).sort_values(by='user_id').reset_index(drop=True)

print(result)


#or 
import pandas as pd
import numpy as np

concatvalues =len(np.unique(np.concatenate([df.user1.values,df.user2.values])))
revert = df.rename(columns= {'user1':'user2','user2':'user1'})
final = pd.concat([df, revert],sort = False).drop_duplicates()
result = final.groupby('user1').size().to_frame('count').reset_index()
result['popularity_percent'] = 100*(result['count'] /concatvalues)
result = result[['user1', 'popularity_percent']]






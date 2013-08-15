import twitter #import the twitter module

api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='') # obtain your keys from Twitter API and enter them here

f = open('last_used.conf', 'r')			# set var f to open last_used.conf and (r)ead
id = f.readline()						# reads a line, adds \n and returns identity of an object, sets it to id
m = open('new_favs.txt', 'w')			# sets var m to open new_favs.txt and (w)rite 
f.close()								# closes f (file)

for page in xrange(1, 10):                         # a for loop to run through Twitter pages
    statuses = api.GetSearch("#Dali", count=500)   # sets var statuses, result of api.Getsearch and custom words and counts to favorite

count = 0     # sets var count to 0 

for s in statuses:
    friend = api.GetUser(twitter#)   # this is the userID number from Twitter, must enter your own
    
    if friend.followers_count == 0:  
        follow_ratio = 1
    else:
        follow_ratio = friend.friends_count / friend.followers_count
    if follow_ratio > 0:
        #api.CreateFriendship(s.user.screen_name)            
        status = api.GetStatus(s.id)
        if friend.id not in api.GetFriendIDs('customTwittername'):     
            if status.favorited == False:
                print str(follow_ratio) + " Ratio"
                print str(status.user.screen_name) + " favorited"
                api.CreateFavorite(status)               # use api to CreateFavorite
                count += 1
            m.write(str(status.id) + "\n")
            id = s.id

print "Favorited: " + str(count) + " tweets"
f = open('last_used.conf', 'w')
print id
f.write(str(id))
f.close()
m.close()

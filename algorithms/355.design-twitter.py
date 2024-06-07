import itertools, collections, heapq
class Twitter(object):
    
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
        


twitter = Twitter();

# User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

# User 1's news feed should return a list with 1 tweet id -> [5].
print twitter.getNewsFeed(1);

# User 1 follows user 2.
twitter.follow(1, 2);

# User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

# User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
print twitter.getNewsFeed(1);

# User 1 unfollows user 2.
twitter.unfollow(1, 2);

# User 1's news feed should return a list with 1 tweet id -> [5],
# since user 1 is no longer following user 2.
print twitter.getNewsFeed(1);

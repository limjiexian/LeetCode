from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.followee_map = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followee_map[userId].add(userId)

        min_heap = []

        for followee in self.followee_map[userId]:
            if followee not in self.tweet_map:
                continue

            index = len(self.tweet_map[followee]) - 1
            # most recent tweet
            count, tweet_id = self.tweet_map[followee][index]
            min_heap.append([count, tweet_id, followee, index])
        
        heapq.heapify(min_heap)
        
        res = []

        while min_heap and len(res) < 10:
            count, tweet_id, followee, index = heapq.heappop(min_heap)
            res.append(tweet_id)

            if index <= 0:
                continue

            # retrieve next most recent tweet
            count, tweet_id = self.tweet_map[followee][index-1]
            heapq.heappush(min_heap, [count, tweet_id, followee, index-1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followee_map[followerId]:
            self.followee_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee_map[followerId]:
            self.followee_map[followerId].remove(followeeId)
        
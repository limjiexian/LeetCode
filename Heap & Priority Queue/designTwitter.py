from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # list of list -> [count, tweetId]
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get latest tweet from each of the person that we are following
        # First we will need to get our list of followers
        # 2nd get the last index of each followers tweetMap
        maxHeap = []    # each element will store count, index,
        
        # need include ownself also
        self.followMap[userId].add(userId)

        # Get follower list
        # For each followee:
        # - Get last index aka latest tweet from our followee tweetMap
        for followeeId in self.followMap[userId]:
            index = len(self.tweetMap[followeeId]) - 1
            if index < 0:
                continue
            count, tweetId = self.tweetMap[followeeId][index]
            heapq.heappush(maxHeap, [count, tweetId, followeeId, index-1])

        res = []
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index < 0:
                continue
            count, tweetId = self.tweetMap[followeeId][index]
            heapq.heappush(maxHeap, [count, tweetId, followeeId, index-1])
    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

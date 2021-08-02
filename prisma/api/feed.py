import feedparser


feedurl = "https://www.upwork.com/ab/feed/topics/rss?securityToken=603faf8be88812e05894fef665cc72f59122b4e500a178302e158b7e3f714517a29290fe9c5bd49e217007ccd2d19fc0094e9c6129e1efe48170d900004e6c57&userUid=1012859292809781248&orgUid=1012859292818169857"
recentfeedurl = "https://www.upwork.com/ab/feed/topics/rss?securityToken=603faf8be88812e05894fef665cc72f59122b4e500a178302e158b7e3f714517a29290fe9c5bd49e217007ccd2d19fc0094e9c6129e1efe48170d900004e6c57&userUid=1012859292809781248&orgUid=1012859292818169857&topic=recommended"


def upworkfeedv1():

    UpworkFeeds = []

    NewsFeed = feedparser.parse(feedurl)
    RecentFeed = feedparser.parse(recentfeedurl)

    UpworkFeeds.append(NewsFeed)
    UpworkFeeds.append(RecentFeed)

    return NewsFeed

def upworkfeed():

    UpworkFeeds = []

    NewsFeed = feedparser.parse(feedurl)
    RecentFeed = feedparser.parse(recentfeedurl)

    UpworkFeeds.append(NewsFeed)
    UpworkFeeds.append(RecentFeed)

    return UpworkFeeds
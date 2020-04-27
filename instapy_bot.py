from instapy import InstaPy

session = InstaPy(username="<username>", password="<password>", headless_browser=True)

session.login()
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.set_relationship_bounds(enabled=True, max_followers=8500)
session.like_by_tags(["programming", "python"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.end()

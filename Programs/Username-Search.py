try:
    import re
    import time
    import requests
    import os
except Exception as e:
    input(e)

username = input("Enter the username to search for: ")

sites = {
        "Roblox": {
            "url": f"https://roblox.com/users/{username}/profile",
            "method": "get",
            "verification": "status",
            "except": ["We couldn't find that user"]
        },
        "Steam": {
            "url": f"https://steamcommunity.com/id/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Telegram": {
            "url": f"https://t.me/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"if you have telegram, you can contact @{username} right away.", f"resolve?domain={username}", f"telegram: contact @{username}"]
        },
        "TikTok": {
            "url": f"https://www.tiktok.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": [f"\\u002f@{username}\""]
        },
        "Instagram": {
            "url": f"https://www.instagram.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Paypal": {
            "url": f"https://www.paypal.com/paypalme/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"slug_name={username}", f"\"slug\":\"{username}\"", f"2F{username}&amp"]
        },
        "GitHub": {
            "url": f"https://github.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Pinterest": {
            "url": f"https://www.pinterest.com/{username}",
            "method": "get",
            "verification": "username",
            "except": [f"[\\\"username\\\",\\\"{username}\\\"]"]
        },
        "Snapchat": {
            "url": f"https://www.snapchat.com/add/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Blogger": {
            "url": f"https://{username}.blogspot.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Tumblr": {
            "url": f"https://{username}.tumblr.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "SoundCloud": {
            "url": f"https://soundcloud.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "DeviantArt": {
            "url": f"https://www.deviantart.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "About.me": {
            "url": f"https://about.me/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Flickr": {
            "url": f"https://www.flickr.com/people/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Keybase": {
            "url": f"https://keybase.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Last.fm": {
            "url": f"https://www.last.fm/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Behance": {
            "url": f"https://www.behance.net/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
               "Quora": {
            "url": f"https://www.quora.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Patreon": {
            "url": f"https://www.patreon.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Myspace": {
            "url": f"https://myspace.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Kaggle": {
            "url": f"https://www.kaggle.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Periscope": {
            "url": f"https://www.pscp.tv/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Disqus": {
            "url": f"https://disqus.com/by/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Mastodon": {
            "url": f"https://mastodon.social/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "GitLab": {
            "url": f"https://gitlab.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "LiveJournal": {
            "url": f"https://{username}.livejournal.com",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "CodeWars": {
            "url": f"https://www.codewars.com/users/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Gumroad": {
            "url": f"https://gumroad.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Spotify": {
            "url": f"https://open.spotify.com/user/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Weebly": {
            "url": f"https://{username}.weebly.com",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "YouTube": {
            "url": f"https://www.youtube.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "ProductHunt": {
            "url": f"https://www.producthunt.com/@{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Mix": {
            "url": f"https://mix.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Facebook": {
            "url": f"https://www.facebook.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Strava": {
            "url": f"https://www.strava.com/athletes/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Linktree": {
            "url": f"https://linktr.ee/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Xbox": {
            "url": f"https://www.xboxgamertag.com/search/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vimeo": {
            "url": f"https://vimeo.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Twitch": {
            "url": f"https://www.twitch.tv/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Goodreads": {
            "url": f"https://www.goodreads.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "VK": {
            "url": f"https://vk.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "TripAdvisor": {
            "url": f"https://www.tripadvisor.com/members/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Dribbble": {
            "url": f"https://dribbble.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "AngelList": {
            "url": f"https://angel.co/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "LinkedIn": {
            "url": f"https://www.linkedin.com/in/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Weibo": {
            "url": f"https://weibo.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "OKCupid": {
            "url": f"https://www.okcupid.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "CodePen": {
            "url": f"https://codepen.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "StackOverflow": {
            "url": f"https://stackoverflow.com/users/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "HackerRank": {
            "url": f"https://www.hackerrank.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Xing": {
            "url": f"https://www.xing.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Deezer": {
            "url": f"https://www.deezer.com/en/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "ReverbNation": {
            "url": f"https://www.reverbnation.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vine": {
            "url": f"https://vine.co/u/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Foursquare": {
            "url": f"https://foursquare.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Ello": {
            "url": f"https://ello.co/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Hootsuite": {
            "url": f"https://hootsuite.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None  
        },
        "Prezi": {
            "url": f"https://prezi.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Groupon": {
            "url": f"https://www.groupon.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Liveleak": {
            "url": f"https://www.liveleak.com/c/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Joomla": {
            "url": f"https://www.joomla.org/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "StackExchange": {
            "url": f"https://stackexchange.com/users/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Taringa": {
            "url": f"https://www.taringa.net/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Shopify": {
            "url": f"https://{username}.myshopify.com",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "8tracks": {
            "url": f"https://8tracks.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Couchsurfing": {
            "url": f"https://www.couchsurfing.com/people/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "OpenSea": {
            "url": f"https://opensea.io/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Trello": {
            "url": f"https://trello.com/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Fiverr": {
            "url": f"https://www.fiverr.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Badoo": {
            "url": f"https://badoo.com/profile/{username}",
            "method": "get",
            "verification": "username",
            "except": None
        },
        "Rumble": {
            "url": f"https://rumble.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Wix": {
            "url": f"https://www.wix.com/website/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "ReverbNation": {
            "url": f"https://www.reverbnation.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Gumroad": {
            "url": f"https://gumroad.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "Vimeo": {
            "url": f"https://vimeo.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "TripAdvisor": {
            "url": f"https://www.tripadvisor.com/members/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "DeviantArt": {
            "url": f"https://www.deviantart.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "VK": {
            "url": f"https://vk.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None
        },
        "allmylinks": {
            "url": f"https://allmylinks.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This page is missing"]
        },
        "Medium": {
            "url": f"https://medium.com/@{username}",
            "method": "get",
            "verification": "status",
            "except": ["Out of nothing, something."]
        },
        "Reddit": {
            "url": f"https://reddit.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Sorry, nobody on Reddit goes by that name."]
        },
        "Twitter": {
            "url": f"https://x.com/{username}",
            "method": "get",
            "verification": "status",
            "except": None  
        },
        "Fosstodon": {
            "url": f"https://fosstodon.org/@{username}",
            "method": "get",
            "verification": "status",
            "except": ["The user could not be found"]
        },
        "Bugcrowd": {
            "url": f"https://bugcrowd.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The requested page was not found"]
        },
        "HackerOne": {
            "url": f"https://hackerone.com/{username}",
            "method": "post",
            "verification": "status",
            "except": ["User does not exist"]
        },
        "HackTheBox": {
            "url": f"https://app.hackthebox.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["User not found"]
        },
        "Apple Developer": {
            "url": f"https://developer.apple.com/forums/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The page you’re looking for can’t be found"]
        },
        "Apple Discussions": {
            "url": f"https://discussions.apple.com/profile/{username}",
            "method": "get",
            "verification": "status",
            "except": ["The page you tried was not found. You may have used an outdated link or may have typed the address (URL) incorrectly."]
        },
        "Hacker News": {
            "url": f"https://news.ycombinator.com/user?id={username}",
            "method": "get",
            "verification": "status",
            "except": ["No such user."]
        },
        "Bitbucket": {
            "url": f"https://bitbucket.org/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Repository not found"]
        },
        "Slack": {
            "url": f"https://{username}.slack.com",
            "method": "get",
            "verification": "status",
            "except": ["This workspace doesn’t exist"]
        },
        "Slide Share": {
            "url": f"https://www.slideshare.net/{username}",
            "method": "get",
            "verification": "status",
            "except": ["This username"]
        },
        "Wattpad": {
            "url": f"https://www.wattpad.com/user/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Oops! That page can’t be found."]
        },
        "Crunchbase": {
            "url": f"https://www.crunchbase.com/person/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Page Not Found"]
        },
        "Pinterest": {
            "url": f"https://Pinterest.com/{username}",
            "method": "get",
            "verification": "status",
            "except": ["Page Not Found"]
        },
    }

print("Started search")

last_key = list(sites.keys())[-1]

for site, data in sites.items():
    try:
        if data == "Roblox":
            url = f"https://api.roblox.com/users/get-by-username?username={username}"
            response = requests.get(url)
            if response.status_code == 200 and "Id" in response.text:
                print(f"\033[92m[+] Found {username} on {site}: https://roblox.com/users/{response.json()['Id']}/profile\033[0m")
            else:
                print(f"\033[91m[-] {username} not found on {site}\033[0m")

        if data["method"] == "get":
            response = requests.get(data["url"])
        elif data["method"] == "post":
            response = requests.post(data["url"])

        if data["verification"] == "username":
            if data["except"]:
                if response.status_code == 200 and all(exc not in response.text for exc in data["except"]):
                    print(f"\033[92m[+] Found {username} on {site}: {data['url']}\033[0m")
            else:
                if response.status_code == 200:
                    print(f"\033[92m[+] Found {username} on {site}: {data['url']}\033[0m")

        elif data["verification"] == "status":
            if data["except"]:
                if response.status_code == 200 and all(exc not in response.text for exc in data["except"]):
                    print(f"\033[92m[+] Found {username} on {site}: {data['url']}\033[0m")
            else:
                if response.status_code == 200:
                    print(f"\033[92m[+] Found {username} on {site}: {data['url']}\033[0m")

    except Exception as e:
        print(f"\033[91m[-] Error checking {site}: {e}\033[0m")

    time.sleep(0.01)

print("Finished search")
os.system("python Main.py")
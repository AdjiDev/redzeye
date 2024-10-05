import requests
import json

def TrackSocial(username):
    # Daftar platform media sosial dan pola URL-nya
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://www.medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
        {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
        {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
        {"url": "https://www.ello.co/{}", "name": "Ello"},
        {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
        {"url": "https://www.telegram.me/{}", "name": "Telegram"},
        {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
    ]
    
    results = []

    for platform in social_media:
        url = platform["url"].format(username)
        try:
            aji = requests.get(url)
            
            if aji.status_code == 200:
                results.append({
                    "username": username,
                    "url": url,
                    "status": "Found"
                })
            else:
                results.append({
                    "username": username,
                    "url": url,
                    "status": "Not Found"
                })
        except requests.exceptions.RequestException as e:
            results.append({
                "username": username,
                "url": url,
                "status": f"Error: {str(e)}"
            })
    
    return json.dumps(results, indent=4)

#username = "exampleuser"
#social_profiles_json = TrackSocial(username)
#print(social_profiles_json)

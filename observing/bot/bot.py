# bot.py
# This script sends embed messages to a Discord channel using a webhook.
# It defines a function to format the embed data and make a POST request.
import requests
import json

def post_to_discord(embed, webhook_url):
    print(embed)
    print(webhook_url)
    if embed == None:
        return
    data = {
        "embeds": [embed]
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    return response.status_code, response.text


# fields = []
# reopen_field = {
#     "name": "\n\n🟡 **Reopened Pull Requests** 🟡\n\n",
#     "value": "",
#     "inline": False
# }
# pr = [{
#     "title": "Fix issue with user authentication",
#     "url": "https://github.com/example/repo/pull/123",
#     "author": "johndoe",
#     "commits": [
#         {"name": "Initial commit", "link": "https://github.com/example/repo/commit/abc123"},
#         {"name": "Add unit tests", "link": "https://github.com/example/repo/commit/def456"},
#         {"name": "Fix edge case", "link": "https://github.com/example/repo/commit/ghi789"},
#         {"name": "Refactor code", "link": "https://github.com/example/repo/commit/jkl012"}
#     ]
# },
# {
#     "title": "Fix issue with user authentication",
#     "url": "https://github.com/example/repo/pull/123",
#     "author": "johndoe",
#     "commits": [
#         {"name": "Initial commit", "link": "https://github.com/example/repo/commit/abc123"},
#         {"name": "Add unit tests", "link": "https://github.com/example/repo/commit/def456"},
#         {"name": "Fix edge case", "link": "https://github.com/example/repo/commit/ghi789"},
#         {"name": "Refactor code", "link": "https://github.com/example/repo/commit/jkl012"}
#     ]
# },      
# ]
# for pr_details in pr:
#     if pr_details:
#         reopen_field["value"] += f"\nΔ [{pr_details['title']}]({pr_details['url']}) by [{pr_details['author']}](https://github.com/{pr_details['author']})\n"
#         reopen_field["value"] += "  Commits:\n"
#         for i, commit in enumerate(pr_details["commits"]):
#             if i:
#                 reopen_field["value"] += f"\n * [{commit['name']}]({commit['link']})"
#             else: 
#                 reopen_field["value"] += f" * [{commit['name']}]({commit['link']})"
#         reopen_field["value"] += "\n"
#     fields.append(reopen_field)


# embed = {
#     "title": "🚀 __ PULL REQUEST REPORT __ 🚀",
#     "description": "This is a report of pull request activities.",
#     "color": 32255,
#     "fields": fields,
# }

# post_to_discord(embed, "https://discord.com/api/webhooks/1293670846178787398/_WHJjgu2cPZcQtfImceHIjhkjlyc8CtLsWBVtomxw3dhwBUaw9DOdBV7q8fCvPAh0LS2")
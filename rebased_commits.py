import requests

def get_commits_from_github(owner, repo, branch, token, last_known_sha):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"}
    params = {"sha": branch}

    response = requests.get(url, headers=headers, params=params)
    commits = response.json()

    new_commits = []
    found_last_known = False

    for commit in commits:
        if commit['sha'] == last_known_sha:
            found_last_known = True
            break
        new_commits.append(commit)

    if not found_last_known:
        print("Warning: Last known commit SHA not found in the current branch history.")

    return new_commits

def check_commit_in_other_branches(owner, repo, commit_sha, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    branches = response.json()

    return branches


def identify_commits(owner, repo, branch, token, last_known_sha):
    new_commits = get_commits_from_github(owner, repo, branch, token, last_known_sha)

    rebased_commits = []
    new_direct_commits = []

    for commit in new_commits:
        branches = check_commit_in_other_branches(owner, repo, commit['sha'], token)
        if len(branches) > 1:
            rebased_commits.append(commit)
        else:
            new_direct_commits.append(commit)

    return rebased_commits, new_direct_commits

# Usage
owner = 'your-github-username'
repo = 'your-repo-name'
branch = 'your-branch-name'
token = 'your-github-token'
last_known_sha = 'your-last-known-sha'

rebased, new_direct = identify_commits(owner, repo, branch, token, last_known_sha)
print("Rebased Commits:", [commit['sha'] for commit in rebased])
print("New Direct Commits:", [commit['sha'] for commit in new_direct])

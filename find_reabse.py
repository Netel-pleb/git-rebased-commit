import subprocess

def find_rebased_commits(branch_name):
    """Finds commits that were rebased onto the specified branch."""

    try:
        # Get the original base of the branch
        original_base = subprocess.check_output(
            ["git", "merge-base", "origin/feat/update-bot", f"origin/{branch_name}"]
        ).decode().strip()
        print(f"Original base: {original_base}")  # Debug print

        # Verify the branch and original base
        branch_exists = subprocess.check_output(
            ["git", "rev-parse", "--verify", branch_name]
        ).decode().strip()
        print(f"Branch exists: {branch_exists}")  # Debug print

        # Get all commits on the branch since the original base
        log_command = ["git", "log", f"{original_base}..{branch_name}", "--format=%H"]
        print(f"Running command: {' '.join(log_command)}")  # Debug print
        commits = subprocess.check_output(log_command).decode().splitlines()
        print(f"Commits: {commits}")  # Debug print

        if not commits:
            print("No commits found.")
            return []

        rebased_commits = []
        for commit in commits:
            # Check if the commit's parent is different from the original parent
            original_parent = subprocess.check_output(
                ["git", "rev-parse", f"{commit}^"]
            ).decode().strip()
            current_parent = subprocess.check_output(
                ["git", "rev-parse", f"{commit}~1"]
            ).decode().strip()

            if original_parent != current_parent:
                rebased_commits.append(commit)

        return rebased_commits

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    branch_name = "main"  # Replace with your actual branch name
    rebased_commits = find_rebased_commits(branch_name)

    if rebased_commits:
        print("Rebased commits:")
        for commit in rebased_commits:
            print(commit)
    else:
        print("No rebased commits found.")
        
        
# Explanation:
# 1. Get the original base:
# The script finds the common ancestor of the local branch and its remote counterpart using git merge-base.
# 2. Get commits since the original base:
# It uses git log to get all commits on the branch that are not present in the original base.
# 3. Check for rebased commits:
# For each commit, it compares the commit's original parent (before rebasing) with its current parent. If they are different, the commit was likely rebased.
# How to use:
# Replace "your_branch_name" with the actual name of the branch you want to analyze.
# Run the script. It will output a list of rebased commit hashes.
import os
import subprocess

# Get the GitHub PAT from environment variables
github_pat = os.getenv("GITHUB_PAT")

if not github_pat:
    print("Error: GitHub PAT is not set. Exiting.")
    exit(1)

# GitHub repo URL (use token for authentication)
github_repo_url = f"https://{github_pat}@github.com/mahatnino/NYC_TLC_Trip.git"
# Configure Git user
subprocess.run(["git", "config", "--global", "user.email", "subashmahat35@gmail.com"], check=True)
subprocess.run(["git", "config", "--global", "user.name", "mahatnino"], check=True)

# Add GitHub as a remote
subprocess.run(["git", "remote", "add", "github", github_repo_url], check=True)

# Fetch the latest changes
subprocess.run(["git", "fetch", "origin"], check=True)

# Push changes to GitHub
subprocess.run(["git", "push", "github", "main"], check=True)  # Change branch if needed

print("✅ Sync completed successfully!")

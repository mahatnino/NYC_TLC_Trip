import os
import subprocess

# Get the GitHub PAT from environment variables
github_pat = os.getenv("GITHUB_PAT")
print("done line6")
if not github_pat:
    print("Error: GitHub PAT is not set. Exiting.")
    exit(1)
print("done line10")
# GitHub repo URL (use token for authentication)
github_repo_url = f"https://{github_pat}@github.com/mahatnino/NYC_TLC_Trip.git"
print("done line13")
# Configure Git user
subprocess.run(["git", "config", "--global", "user.email", "subashmahat35@gmail.com"], check=True)
print("done line16")
subprocess.run(["git", "config", "--global", "user.name", "mahatnino"], check=True)
print("done line18")
# Add GitHub as a remote
subprocess.run(["git", "remote", "add", "github", github_repo_url], check=True)
print("done line20")
# Fetch the latest changes
subprocess.run(["git", "fetch", "origin"], check=True)
print("done line24")
# Push changes to GitHub
subprocess.run(["git", "push", "github", "main"], check=True)  # Change branch if needed

print("✅ Sync completed successfully!")

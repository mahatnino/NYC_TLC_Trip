import os
import subprocess

# Get Azure DevOps and GitHub PATs securely from environment variables
azure_pat = os.getenv("AZURE_DEVOPS_PAT")
github_pat = os.getenv("GITHUB_PAT")

# 🔍 Debugging: Check if the environment variable is being set
print(f"🔍 AZURE_DEVOPS_PAT: {repr(azure_pat)}")  # Shows raw value (should not be None)
print(f"🔍 AZURE_DEVOPS_PAT length: {len(azure_pat) if azure_pat else 'None'}")

# Debugging: Check if PATs are set
if not azure_pat or not github_pat:
    print("❌ Error: One or both PATs are not set. Exiting.")
    print(f"AZURE_DEVOPS_PAT length: {len(azure_pat) if azure_pat else 'None'}")
    print(f"GITHUB_PAT length: {len(github_pat) if github_pat else 'None'}")
    exit(1)

# ✅ Corrected Azure DevOps repo URL format
AZURE_DEVOPS_REPO = f"https://:{azure_pat}@dev.azure.com/SubashMahat/NYC%20TLC%20Trip/_git/NYC%20TLC%20Trip"

# ✅ Corrected GitHub repo URL
GITHUB_USERNAME = "mahatnino"
GITHUB_REPO_URL = f"https://{github_pat}@github.com/{GITHUB_USERNAME}/NYC_TLC_Trip.git"

# Clone Azure DevOps repository if not already cloned
if not os.path.exists("repo"):
    subprocess.run(["git", "clone", "--mirror", AZURE_DEVOPS_REPO, "repo"], check=True)

# Move into repo directory
os.chdir("repo")

# Configure Git user
subprocess.run(["git", "config", "--global", "user.email", "subashmahat35@gmail.com"], check=True)
subprocess.run(["git", "config", "--global", "user.name", GITHUB_USERNAME], check=True)

# Ensure GitHub remote is correctly set up
existing_remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout
if "github" in existing_remotes:
    subprocess.run(["git", "remote", "remove", "github"], check=True)

subprocess.run(["git", "remote", "add", "github", GITHUB_REPO_URL], check=True)

# Fetch latest changes and push to GitHub
subprocess.run(["git", "fetch", "--prune"], check=True)
subprocess.run(["git", "push", "--mirror", "github"], check=True)

print("✅ Sync completed successfully!")

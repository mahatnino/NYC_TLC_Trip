import os
import subprocess

# Retrieve environment variables
azure_pat = os.getenv("AZURE_DEVOPS_PAT")
github_pat = os.getenv("GITHUB_PAT")

# Debugging
print(f"🔍 AZURE_DEVOPS_PAT in Python: {repr(azure_pat)}")  # Should NOT be "$(AZURE_DEVOPS_PAT)"
print(f"🔍 AZURE_DEVOPS_PAT length: {len(azure_pat) if azure_pat else 'None'}")
print(f"🔍 GITHUB_PAT length: {len(github_pat) if github_pat else 'None'}")

# 🚨 Exit if the PAT is incorrect
if not azure_pat or "$(AZURE_DEVOPS_PAT)" in azure_pat:
    print("❌ Error: AZURE_DEVOPS_PAT is not set correctly. Exiting.")
    exit(1)

# ✅ Correct repository URL format
AZURE_DEVOPS_REPO = f"https://{azure_pat}@dev.azure.com/SubashMahat/NYC%20TLC%20Trip/_git/NYC%20TLC%20Trip"
GITHUB_REPO = f"https://{github_pat}@github.com/mahatnino/NYC_TLC_Trip.git"

print(f"🔍 Using repository URL: {AZURE_DEVOPS_REPO}")

# ✅ Clone repository
try:
    subprocess.run(["git", "clone", "--mirror", AZURE_DEVOPS_REPO, "repo"], check=True)
except subprocess.CalledProcessError:
    print("❌ Failed to clone Azure DevOps repo. Check PAT permissions and repository URL.")
    exit(1)

# ✅ Move into repo directory
os.chdir("repo")

# ✅ Configure Git user
subprocess.run(["git", "config", "--global", "user.email", "subashmahat35@gmail.com"], check=True)
subprocess.run(["git", "config", "--global", "user.name", "mahatnino"], check=True)

# ✅ Ensure GitHub remote is set up
existing_remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout
if "github" in existing_remotes:
    subprocess.run(["git", "remote", "remove", "github"], check=True)

subprocess.run(["git", "remote", "add", "github", GITHUB_REPO], check=True)

# ✅ Push changes to GitHub
try:
    subprocess.run(["git", "fetch", "--prune"], check=True)
    subprocess.run(["git", "push", "--mirror", "github"], check=True)
    print("✅ Sync completed successfully!")
except subprocess.CalledProcessError:
    print("❌ Failed to push to GitHub. Check GitHub PAT permissions.")
    exit(1)

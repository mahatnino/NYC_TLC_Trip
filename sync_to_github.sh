#!/bin/bash

# Debugging: Print if variables are set
echo "🔍 Checking if PATs are set..."
echo "🔍 AZURE_DEVOPS_PAT length: ${#AZURE_DEVOPS_PAT}"  # Should print a real number
echo "🔍 GITHUB_PAT length: ${#GITHUB_PAT}"

# Validate PATs
if [[ -z "$AZURE_DEVOPS_PAT" || -z "$GITHUB_PAT" ]]; then
    echo "❌ Error: One or both PATs are not set. Exiting."
    exit 1
fi

# Define repository URLs
AZURE_DEVOPS_REPO="https://$AZURE_DEVOPS_PAT@dev.azure.com/SubashMahat/NYC%20TLC%20Trip/_git/NYC%20TLC%20Trip"
GITHUB_REPO="https://$GITHUB_PAT@github.com/mahatnino/NYC_TLC_Trip.git"

# Clone Azure DevOps repository
echo "🔄 Cloning Azure DevOps repo..."
rm -rf repo  # Ensure a clean clone
git clone --mirror "$AZURE_DEVOPS_REPO" repo || { echo "❌ Failed to clone Azure DevOps repo"; exit 1; }

# Move into the repo directory
cd repo || exit 1

# Configure Git user
git config --global user.email "subashmahat35@gmail.com"
git config --global user.name "mahatnino"

# Ensure GitHub remote is correctly set up
if git remote | grep -q github; then
    git remote remove github
fi
git remote add github "$GITHUB_REPO"

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git fetch --prune
git push --mirror github || { echo "❌ Failed to push to GitHub"; exit 1; }

echo "✅ Sync completed successfully!"

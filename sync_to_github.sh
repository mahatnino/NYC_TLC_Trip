trigger:
- main  # Change to your branch

pool:
  vmImage: 'ubuntu-latest'

variables:
- group: PAT_TOKENS  # ✅ This pulls the variables from the Library

steps:
- script: |
    echo "🔍 Checking environment variables..."
    echo "🔍 AZURE_DEVOPS_PAT length: ${#AZURE_DEVOPS_PAT}"  # Should print a real number
    echo "🔍 GITHUB_PAT length: ${#GITHUB_PAT}"

    sudo apt-get install dos2unix -y  # Convert script if necessary
    dos2unix sync_to_github.sh  

    chmod +x sync_to_github.sh

    # ✅ Export the variable to ensure it's expanded properly in the script
    export AZURE_DEVOPS_PAT="${AZURE_DEVOPS_PAT}"
    export GITHUB_PAT="${GITHUB_PAT}"

    ./sync_to_github.sh
  env:
    AZURE_DEVOPS_PAT: $(AZURE_DEVOPS_PAT)  # ✅ Ensure secrets are correctly pulled
    GITHUB_PAT: $(GITHUB_PAT)
  displayName: "Run Sync Script"

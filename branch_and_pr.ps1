param(
    [Parameter(Mandatory = $true)]
    [string]$BranchName,
    [string]$Message = "Update practice files"
)

# Simple helper: write a header
function Write-Section($text) {
    Write-Host ""
    Write-Host "=== $text ==="
}

Write-Section "Current status"
git status

Write-Section "Creating / switching to branch '$BranchName'"

# Check if the branch already exists locally
$branchExists = git branch --list $BranchName

if ($branchExists) {
    Write-Host "Branch '$BranchName' already exists locally. Switching to it..."
    git checkout $BranchName
} else {
    Write-Host "Branch '$BranchName' does not exist. Creating it from current branch..."
    git checkout -b $BranchName
}

Write-Section "Staging changes"
git add .

Write-Section "Committing changes"
git commit -m $Message

Write-Section "Pushing branch to origin"
git push -u origin $BranchName

Write-Section "Next step: open a Pull Request"

# Change this to your actual GitHub username/repo if needed
$repoUrl = "https://github.com/MikeTheCyberGuy/d335-python-practice-bank"
$prUrl = "$repoUrl/compare/$BranchName?expand=1"

Write-Host "Open this URL in your browser to create a PR:"
Write-Host $prUrl

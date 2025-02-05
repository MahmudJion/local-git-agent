import os
from git import Repo

def list_repos(base_path):
    """List all git repositories in the given directory."""
    return [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f, ".git"))]

def select_repo(base_path):
    """Allow user to select a repository from available options."""
    repos = list_repos(base_path)
    if not repos:
        print("No repositories found in the directory.")
        return None
    print("Available Repositories:")
    for i, repo in enumerate(repos):
        print(f"{i + 1}. {repo}")
    choice = int(input("Select a repository by number: ")) - 1
    return os.path.join(base_path, repos[choice]) if 0 <= choice < len(repos) else None

def commit_changes(repo_path, commit_message):
    """Stage and commit changes to the repository."""
    repo = Repo(repo_path)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    print(f"Changes committed locally with message: {commit_message}")

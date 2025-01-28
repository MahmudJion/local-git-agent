import os
import subprocess
import openai
from git import Repo

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def select_repo(base_path):
    """List all repos in the base directory and select one."""
    repos = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f, ".git"))]
    print("Available Repositories:")
    for i, repo in enumerate(repos):
        print(f"{i + 1}. {repo}")
    choice = int(input("Select a repository by number: ")) - 1
    return os.path.join(base_path, repos[choice])

def generate_code(task_description):
    """Generate code using OpenAI API based on a task description."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who writes code."},
            {"role": "user", "content": f"Task: {task_description}"}
        ]
    )
    return response.choices[0].message.content.strip()

def apply_code(repo_path, file_path, code_snippet):
    """Apply the generated code to a file in the repo."""
    full_path = os.path.join(repo_path, file_path)
    with open(full_path, "a") as file:  # Append to the file
        file.write(f"\n\n# Auto-generated code\n{code_snippet}\n")
    print(f"Code applied to {file_path}")

def commit_changes(repo_path, commit_message):
    """Stage and commit changes locally."""
    repo = Repo(repo_path)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    print(f"Changes committed locally with message: {commit_message}")

def main():
    base_path = input("Enter the base path for your repositories: ")
    repo_path = select_repo(base_path)
    print(f"Selected Repository: {repo_path}")

    future_work = input("Describe the future work for this repo: ")
    num_tasks = int(input("How many tasks do you want to define? "))
    task_list = [input(f"Task {i + 1}: ") for i in range(num_tasks)]

    for task in task_list:
        print(f"Processing Task: {task}")
        code_snippet = generate_code(task)
        print(f"Generated Code:\n{code_snippet}")
        file_path = input(f"Enter the file path to apply the code (relative to {repo_path}): ")
        apply_code(repo_path, file_path, code_snippet)

    commit_message = f"Future work: {future_work}\nTasks:\n" + "\n".join([f"- {task}" for task in task_list])
    commit_changes(repo_path, commit_message)

    print("All changes committed locally. Push manually when ready.")

if __name__ == "__main__":
    main()

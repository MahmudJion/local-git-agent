from config import BASE_REPO_PATH
from utils import select_repo, commit_changes
from main import generate_code, apply_code

def main():
    repo_path = select_repo(BASE_REPO_PATH)
    if not repo_path:
        print("No repository selected. Exiting...")
        return

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

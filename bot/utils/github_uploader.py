# ---------------------------------------------------------
# GitHub Manager Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the GitHub Manager Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import os
from github import Github

def upload_to_github(user_token, repo_name, branch, folder_path):
    try:
        g = Github(user_token)
        repo = g.get_repo(repo_name)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)

                with open(full_path, 'rb') as f:
                    content = f.read()

                try:
                    existing_file = repo.get_contents(rel_path, ref=branch)
                    repo.update_file(existing_file.path, f"Update {rel_path}", content, existing_file.sha, branch=branch)
                except:
                    repo.create_file(rel_path, f"Add {rel_path}", content, branch=branch)
        return True
    except Exception as e:
        print(f"GitHub Upload Error: {e}")
        return False

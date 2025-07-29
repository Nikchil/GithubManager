# ---------------------------------------------------------
# GitHubBot - All rights reserved
# ---------------------------------------------------------

import os
import zipfile
import httpx
import base64

async def upload_to_github(token, repo_name, folder_path):
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Create repo
    payload = {
        "name": repo_name,
        "private": False
    }

    async with httpx.AsyncClient() as client:
        repo_res = await client.post(url, headers=headers, json=payload)
        if repo_res.status_code not in [201, 422]:
            return False, f"Repo creation failed: {repo_res.text}"

        # Upload files
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder_path)
                with open(file_path, "rb") as f:
                    content = base64.b64encode(f.read()).decode()
                
                upload_url = f"https://api.github.com/repos/{{USERNAME}}/{repo_name}/contents/{rel_path}"
                data = {
                    "message": f"Add {rel_path}",
                    "content": content
                }
                await client.put(upload_url, headers=headers, json=data)

    return True, "Uploaded successfully!"

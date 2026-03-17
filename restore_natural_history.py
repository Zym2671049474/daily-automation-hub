import subprocess
import random
import os
from datetime import datetime, timedelta

START_DATE = datetime(2023, 10, 7)
END_DATE = datetime(2026, 3, 17)
MESSAGES = [
    "Update project structure", "Optimize logic", "Add new features",
    "Fix bug", "Update README", "Code cleanup", "Initial project files"
]

current_date = START_DATE
total_commits = 0

subprocess.run(["git", "config", "user.email", "Zym2671049474@users.noreply.github.com"])
subprocess.run(["git", "config", "user.name", "Zym2671049474"])

while current_date <= END_DATE:
    # 恢复 13:24 版本的随机 1-5 个 commit，产生自然的深浅绿色
    num_commits = random.randint(1, 5)
    for i in range(num_commits):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_time = current_date.replace(hour=hour, minute=minute, second=second)
        date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        with open("daily_log.txt", "a") as f:
            f.write(f"Commit {total_commits}: {date_str}\n")
            
        subprocess.run(["git", "add", "daily_log.txt"], check=True)
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(["git", "commit", "-m", random.choice(MESSAGES)], env=env, check=True, capture_output=True)
        total_commits += 1
    current_date += timedelta(days=1)
print(f"Restored {total_commits} natural commits.")

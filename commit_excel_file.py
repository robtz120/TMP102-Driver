from git import Repo # Open my repository
import pandas as pd
import os
from datetime import datetime
import pytz

url_repo = "https://github.com/Mechatrobot/TMP102-Driver"
local_file = "C:/Users/se93297/Desktop/test"
repo = Repo(local_file)

if not os.path.exists(local_file) :
  Repo.clone_from(url_repo,local_file);       #clone the repo into the local if it doesn't exist.
else :
  origin = repo.remotes.origin #remote the repo to local directory
  origin.pull()   # pull the changes into the local repository
commits =  list(repo.iter_commits('main'))
commit_data = []
for commit in commits :
   commit_date = commit.committed_datetime.astimezone(pytz.UTC) #convert the timezone to UTC.
   commit_data.append({'SHA' : commit.hexsha,
                       'Commiter' : commit.committer.name,
                       'Date' : commit_date.strftime('%Y-%m-%d %H:%M:%S %Z%z'), #string format
                       'Email': commit.committer.email
                      })

data_frame = pd.DataFrame(commit_data) #convert commit data to DataFrame to put it on excel
excel_file = os.path.join(local_file,'commits_history.xlsx')  # create the excel file
data_frame.to_excel(excel_file, index=False, sheet_name= 'Commits') #assign DataFrame to excel

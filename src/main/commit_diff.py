import git

# Initialize a new repo in the current folder
repo = git.Repo()

repo.remotes.origin
repo.head.

# Creates an empty file called README.md
open('README.md', 'w').close()

# Add the README file
repo.index.add(['README.md'])

with open('README.md', 'a') as f:
    f.write("# My Project\n\nQuite brilliant, if I do say so myself!")

# Commit the README file to version control
repo.index.commit("Add README")

# List the files changed since the last commit
[diff.a_path for diff in repo.index.diff(repo.head.commit)]
type(repo.head.commit.stats.files)
repo.head.commit.stats.total

[diff.a_blob.data_stream.read().decode('utf-8') for diff in
 # Obtain the "diff" between latest commit with its parent
 repo.head.commit.diff(repo.head.commit.parents[0])]


import tempfile
import git

# Initialize a new repo in the current folder
temp_dir = tempfile.mkdtemp()
repo = git.Repo.init(temp_dir)

# Creates an empty file called README.md
open(temp_dir + 'README.md', 'w').close()

# Add and commit the README file
repo.index.add([temp_dir + 'README.md'])

# Commit the README file to version control
repo.index.commit("Add README")

# Add content to your README.md
with open(temp_dir + 'README.md', 'a') as f:
    f.write("# My Package\n\nQuite brilliant, if I do say so myself!")

# Add and commit the README file
repo.index.add([temp_dir + 'README.md'])

# Commit changes and get commit stats
repo.index.commit("Add project title to README")

new_repo = git.Repo.init('.')


# Connect the local and remote repos
origin = new_repo.create_remote('origin', url=repo.working_tree_dir)
origin.fetch()
# Create and checkout local branch "master" from remote "master"
(new_repo.create_head('master', origin.refs.master)
         .set_tracking_branch(origin.refs.master)
         .checkout())
new_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
# Pull the remote commits to the local repo
origin.pull()

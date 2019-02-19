import git

repo = git.Repo.init('.')
[commit.message for commit in repo.iter_commits()]

open('README.md', 'w').close()
repo.untracked_files

# Add and commit the README file
repo.index.add(['README.md'])
repo.index.entries

repo.index.diff()
repo.head.commit.parents
repo.index.commit("Initial commit")
[diff.a_blob.data_stream.read().decode('utf-8') for diff in repo.index.diff(repo.head.commit)]
[diff.a_blob.data_stream.read().decode('utf-8')
 for diff in repo.head.commit.diff(repo.head.commit.parents[0])]

# Add content to your README.md
with open('README.md', 'a') as f:
  f.write("# My Package\n\nQuite brilliant, if I do say so myself!")
repo.head.commit.stats.total
repo.index.add(['README.md'])
repo.index.diff(None)
repo.index.diff(repo.head.commit)[0].a_blob.data_stream.read().decode('utf-8')
repo.index.diff(repo.head.commit)[0].change_type
repo.index.diff(repo.head.commit)[0].diff
repo.index.diff(repo.head.commit)[0].
repo.index.diff('HEAD')[0].a_blob.data_stream.read().decode('utf-8')
repo.head.commit.diff()[0].a_blob.data_stream.read().decode('utf-8')

for diff_added in repo.head.commit.diff('HEAD~1').iter_change_type('A'):
    print(diff_added)

[blob.name for blob in repo.head.commit.tree]

open('analysis.py', 'w').close()
open('notes.md', 'w').close()
open('plot.py', 'w').close()

# Add content to your README.md
with open('README.md', 'a') as f:
    f.write("# My Package\n\nQuite brilliant, if I do say so myself!")

# Add and commit changes to the README file
repo.index.add(['README.md'])
repo.index.commit("Initial commit")

repo.index.add(['README.md'])
repo.index.commit("Add project title to README")
# Add and commit the README file
repo.git.add(['analysis.py', 'notes.md', 'plot.py'])
repo.index.commit("Add files")
repo.git.diff(repo.head.commit)
[i.data_stream.read() for i in repo.head.commit.tree]
[blob.name for blob in repo.head.commit.tree]
changed_files = [item.a_path for item in repo.index.diff(None)]
changed_files
[d.a_blob.data_stream.read().decode('utf-8') for d in repo.head.commit.diff('HEAD^')]

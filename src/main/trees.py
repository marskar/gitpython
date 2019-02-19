import os
import git

# Initialize a new repo in the current folder
repo = git.Repo.init()
repo = git.Repo()

# Creates an empty file called README.md
open("README.md", "w").close()
repo.untracked_files

# Add and commit the README file
repo.index.entries
repo.index.add(["README.md"])
repo.index.add(["README.md"])
repo.git.add(update=True)
repo.index.commit("Initial commit")

open("analysis.py", "w").close()
open("notes.md", "w").close()
open("plot.py", "w").close()

# Add and commit the new file
repo.git.add(["analysis.py", "notes.md", "plot.py"])
repo.git.add(["mynotes.md", "plot.py"])
repo.git.add(["src/main/trees.py"])
repo.index.add([".gitignore"])
repo.index.commit("Add files")
[item.a_path for item in repo.index.diff("HEAD")]
head = repo.head.commit.message
added = [i.a_blob.name for i in repo.index.diff(head).iter_change_type("M")]
added, deleted, modified, renamed = [
    [item.b_path for item in repo.head.commit.diff().iter_change_type(ct)]
    for ct in ("A", "D", "M", "R")
]

change_dict = {
    name: ', '.join(eval(name)) for name
    in "added deleted modified renamed".split()
}

repo.index.commit("Added: {added} Deleted: {deleted} Modified: {modified} "
                  "Renamed: {renamed}".format_map(change_dict))

repo.head.commit.message

# Untracked changes to be committed
repo.untracked_files
untracked_changes = [item.a_path for item in repo.index.diff(None)]
[item.a_path for item in repo.index.diff(None)]
[item.b_path for item in repo.index.diff(None)]

[item.a_blob.name for item in repo.index.diff(None)]
# [item.b_blob.name for item in repo.index.diff(None)]
[item.a_path for item in repo.index.diff(None)]
[item.b_path for item in repo.index.diff(None)]
# Tracked changes to be committed
tracked_changes = [item.a_path for item in repo.head.commit.diff()]
[item.a_blob.name for item in repo.head.commit.diff()]
[item.b_blob.name for item in repo.head.commit.diff()]
[item.a_path for item in repo.head.commit.diff()]
[item.b_path for item in repo.head.commit.diff()]
[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("R")]

[item.a_blob.name for item in repo.head.commit.diff().iter_change_type("M")]
[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("M")]
[item.a_path for item in repo.head.commit.diff().iter_change_type("M")]
[item.b_path for item in repo.head.commit.diff().iter_change_type("M")]

[item.a_blob.name for item in repo.head.commit.diff().iter_change_type("D")]
# [item.b_blob.name for item in repo.head.commit.diff().iter_change_type('D')]
[item.a_path for item in repo.head.commit.diff().iter_change_type("D")]
[item.b_path for item in repo.head.commit.diff().iter_change_type("D")]

[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("R")]
[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("M")]
[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("D")]

[item.a_path for item in repo.head.commit.diff().iter_change_type("A")]
[item.b_path for item in repo.head.commit.diff().iter_change_type("A")]
[item.a_blob for item in repo.head.commit.diff().iter_change_type("A")]
[item.b_blob.name for item in repo.head.commit.diff().iter_change_type("A")]

[item.a_blob.name for item in repo.index.diff("HEAD")]
[item.a_blob.name for item in repo.index.diff(repo.head.commit)]
[item.a_path for item in repo.index.diff(None).iter_change_type("A")]
[item.a_path for item in repo.index.diff("HEAD").iter_change_type("D")]
[item.a_blob for item in repo.index.diff("HEAD").iter_change_type("D")]
[item.a_path for item in repo.index.diff("HEAD").iter_change_type("M")]
[blob.name for stage, blob in list(repo.index.iter_blobs())]
[o.name for o in repo.head.commit.tree.traverse()]
[blob.name for blob in repo.head.commit.tree.blobs]
[blob.name for blob in repo.head.commit.tree]
repo.head.commit.tree.blobs
for (path, stage), entry in repo.index.entries.items():  # @UnusedVariable
    print(entry)
# Delete all but the first file in the tree
# list(map(os.remove, [file.name for file in repo.head.commit.tree][1:]))
[blob.name for blob in repo.head.commit.tree]


def add_to_files(filenames, contents):
    for filename in filenames:
        with open(filename, "a") as f:
            f.write(contents)


add_to_files([blob.name for blob in repo.head.commit.tree], "A change!")

# Get a list of files changed since the last commit
changed_files = [item.a_path for item in repo.index.diff(None)]
changed_files
# Add and commit the changes, then get the commit message
repo.index.add(changed_files)
repo.index.commit("Modified {}".format(changed_files))
repo.head.commit.message
[
    diff.a_blob.data_stream.read().decode("utf-8")
    for diff in repo.index.diff(repo.head.commit)
]

# Diff HEAD with its parent (HEAD^)
[
    diff.a_blob.data_stream.read().decode("utf-8")
    for diff in repo.head.commit.diff(repo.head.commit.parents[0])
]

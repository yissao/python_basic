## erro
Please commit your changes or stash them before you merge.

## cause
PS C:\Users\raziel\Documents\Projetos\Python\python_basic> git pull
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Total 19 (delta 7), reused 19 (delta 7), pack-reused 0 (from 0)
From https://github.com/yissao/python_basic
   d557e87..d24af60  main       -> origin/main
Updating d557e87..d24af60
error: Your local changes to the following files would be overwritten by merge:
        gemini/python_ai_02.ipynb
Please commit your changes or stash them before you merge.
Aborting
## workaround
You can't merge with local modifications. Git protects you from losing potentially important changes.

You have three options:

Commit the change using
git commit -m "My message"
Stash it.
Stashing acts as a stack, where you can push changes, and you pop them in reverse order.

To stash, type

git stash
Do the merge, and then pull the stash:

git stash pop
Discard the local changes
using git reset --hard
or git checkout -t -f remote/branch

Or: Discard local changes for a specific file
using git checkout filename

## solution
PS C:\Users\raziel\Documents\Projetos\Python\python_basic> git reset --hard
HEAD is now at d557e87 atualizado gemini
PS C:\Users\raziel\Documents\Projetos\Python\python_basic> git pull
Updating d557e87..d24af60
Fast-forward
 .github.bat                                 |   15 +-
 gemini/python_ai_02.ipynb                   |    2 +-
 legendayoutube/legenda_01.py                |   37 +
 legendayoutube/legendas.txt                 |  744 +++++++++++
 legendayoutube/legendas_com_links.txt       |  744 +++++++++++
 notebooklm_download/export_note.py          |   60 +
 notebooklm_download/notes.txt               |   88 ++
 notebooklm_download/readme.md               |    5 +
 regular_expression/seuarquivo.txt           | 1853 +++++++++++++++++++++++++++
 regular_expression/seuarquivo_formatado.txt | 1119 ++++++++++++++++
 regular_expression/troca_strings_01.ipynb   |   62 +
 11 files changed, 4725 insertions(+), 4 deletions(-)
 create mode 100644 legendayoutube/legenda_01.py
 create mode 100644 legendayoutube/legendas.txt
 create mode 100644 legendayoutube/legendas_com_links.txt
 create mode 100644 notebooklm_download/export_note.py
 create mode 100644 notebooklm_download/notes.txt
 create mode 100644 notebooklm_download/readme.md
 create mode 100644 regular_expression/seuarquivo.txt
 create mode 100644 regular_expression/seuarquivo_formatado.txt
 create mode 100644 regular_expression/troca_strings_01.ipynb
PS C:\Users\raziel\Documents\Projetos\Python\python_basic> 
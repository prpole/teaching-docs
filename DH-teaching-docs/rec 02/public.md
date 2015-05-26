chmod cheat sheet:

     chmod u=rx file        (Give the owner rx permissions, not w)
     chmod go-rwx file      (Deny rwx permission for group, others)
     chmod g+w file         (Give write permission to the group)
     chmod a+x file1 file2  (Give execute permission to everybody)
     chmod g+rx,o+x file    (OK to combine like this with a comma)
agents

u owner
g group
o everyone else

operations
= set permissions
+ add permissions
- remove permissions

permissions
r read
w write
x execute
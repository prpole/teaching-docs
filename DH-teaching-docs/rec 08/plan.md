# Lecture 2: Word

## How to do things with words (command line)


### Putting all your fruits into one basket

> lines and words, destructive vs. non-destructive transformations
> (munging), more pipes

1. add your fruits  
`   echo "orange banana pear tomato banana pear orange apple apple strawberry nectarine" > fruit.txt`

2. add another one  
`    echo "banana" >> fruit.txt`

3. substitute space for newlines  
`    sed 's/\s/\n/g'` (Linux)  
`    sed 's/[[:space:]]/\'$'\n/g' fruits.txt` (Mac)  

4. remove bad fruit  
`    echo "nectarine" > bad-fruit.txt`  
`    echo "tomato" >> bad-fruit.txt`  
`    cat fruit.txt | grep -vf bad-fruit.txt`  
`    cat fruit.txt` (to see if it worked)  

5. sort and count  


`    sort fruits.txt > sorted-fruits.txt`  
`    uniq -c sorted-fruits.txt`  


Redo everything with one long pipe

TR

for lower:

`   tr "[:upper:]" "[:lower:]"`

for punct:

`  tr -d "[:punct:]"`



text = ['one', 'day', 'he', 'saw', 'a', 'squid', 'and', 'a', 'lobster', 'put', 'in', 'the', 'tank', 'and', 'in', 'connection', 'with', 'them', 'was', 'witness', 'to', 'a', 'tragedy', 'which', 'stayed', 'with', 'him', 'all', 'his', 'life', 'and', 'cleared', 'things', 'up', 'considerably', 'intellectually', 'the', 'lobster', 'it', 'appeared', 'from', 'the', 'talk', 'of', 'the', 'idle', 'bystanders', 'was', 'offered', 'no', 'food', 'as', 'the', 'squid', 'was', 'considered', 'his', 'rightful', 'prey']

count = 0

word = input('what is the word')

for n in text:
    if n == word:
        count = count + 1
print(count)


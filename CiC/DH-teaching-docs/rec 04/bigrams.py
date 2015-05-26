text = ['one', 'day', 'he', 'saw', 'a', 'squid', 'and', 'a', 'lobster', 'put', 'in', 'the', 'tank', 'and', 'in', 'connection', 'with', 'them', 'was', 'witness', 'to', 'a', 'tragedy', 'which', 'stayed', 'with', 'him', 'all', 'his', 'life', 'and', 'cleared', 'things', 'up', 'considerably', 'intellectually', 'the', 'lobster', 'it', 'appeared', 'from', 'the', 'talk', 'of', 'the', 'idle', 'bystanders', 'was', 'offered', 'no', 'food', 'as', 'the', 'squid', 'was', 'considered', 'his', 'rightful', 'prey']

ndx = 0
new_list = []

#begin with first word rather than beginning one ahead; alternative is also fine
while ndx < len(text) - 1:
	new_list.append(text[ndx:ndx+2])
	ndx += 1

print(new_list)

from googlesearch import search
query = input("search:  ")
for j in search(query, num_results=6):
  print(j)
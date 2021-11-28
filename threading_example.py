tmap = {'a':1, 'b':2, 'c':3}


def doit(k):
	print("doit: {k} = {tmap[k]}")


def doit2(t):
	k,v = t
	print(f"doit: {k} = {v}")


with ThreadPoolExecutor(max_workers=2) as pool:
	pool.map(doit, tmap, chunksize=1)
	pool.map(doit2, tmap.items(), chunksize=1)
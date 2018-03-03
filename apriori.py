def checkDuplicateSet(c,result):
	duplicate = False
	for cElement in c:
		if cElement == result:
			duplicate = True
		
	if duplicate == False:
		c.append(result)
		
def multiplySet(fk,f0,k):
	ckplus1 = []
	for item in f0:
		for itemSet in fk:
			result = set(itemSet).union(item)
			if len(result) == k+1:
				checkDuplicateSet(ckplus1, result)
	return ckplus1
	
	
database = [ ['a','c','e'], ['b','c','e'], ['a','b','c','e'], ['b','e','d'] ]

# Holds the lists that represent generations of frequent itemsets
frequencyList = []
ck = {}

# Scan database to generate f1 (1-itemset frequency set) 
for transaction in database:
	for element in transaction:
		if element in ck.keys():
			ck[element] = ck[element] + 1
		else:
			ck[element] = 1
fk = {i:ck[i] for i in ck if ck[i] > 1}
fk = fk.keys()
frequencyList.append(fk)
			
k = 1 # k = 1 since f1 has already been generated

while (len(fk) != 0):
	# Generate new candidate set
	ck_sets = multiplySet(fk,frequencyList[0], k) 
	
	fk = [] # fk will now list the sets of frequent k-itemsets
	# Scan database to find itemset frequencies for ck 
	for itemset in ck_sets:
		itemsetCount = 0; # During the scan, I keep count of the transactions that contain the itemset
		for transaction in database:
			if itemset.issubset(transaction):
				itemsetCount = itemsetCount + 1
				
		if itemsetCount > 1: # If the current itemset meets the minimum support, then add to fk
			fk.append(itemset)
	
	# Store fk in frequencyList for reference and collection
	frequencyList.append(fk) # Example: frequencyList[0] = f0	
	k = k + 1	
	

print("\nFrequent itemsets: ")

k = 0
for frequencySet in frequencyList:
	print("======= F" + str(k) + " =====")
	for itemSet in frequencySet:
		print(itemSet)
	k = k + 1
	
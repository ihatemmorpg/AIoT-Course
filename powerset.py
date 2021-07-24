def powerset(s):
	if not len(s):
		return
	result = [s]
	for i in range(len(s)):
		result.append(s[:i]+s[i+1:])
		subpowerset = powerset(s[:i]+s[i+1:])
		if subpowerset:
			for item in powerset(s[:i]+s[i+1:]):
				if item not in result:
					result.append(item)
	return result

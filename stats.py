from collections import Counter 
def char_count(s):
    s = s.lower()
    count = Counter(s)
    result = dict(count)    
    return result

def word_count(text):
	data = text.split()
	return len(data)

def get_list(counter:dict):
    list = []
    for key, value in counter.items():
        list.append((key, value))
    list.sort(key=lambda x: x[1], reverse=True)
    return list
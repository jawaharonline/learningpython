dict = {"fast": "In a quick manner", 
"exoctic": "strange",
"marks": [1, 2, 3, 5],
"anyother": {'Jawahar': 'Student'},
1 : 3 
}

# Dictoinary methods
# print(dict.keys())
print(list(dict.keys())) #keys of dictionary
print(dict.values()) #print values
print(dict.items()) #prints (key, value) for all contents same 
print(dict)
updatedict = {
    "Lovish": "friend",
   "exoctic": "unknown" 
}
dict.update(updatedict) #update dicts by adding key value pairs from updateDict
print(dict)

print(dict.get("exoctic")) #printss value associated with key
print(dict.get("exoctic3")) #returns None as it is not presenr
# print(dict.get["exoctic3"]) #throws an error as it is not present in the dict (not a pro way)

print('marks2' not in dict) #returns TRUE as marks2 is not in dict.
print('marks' in dict) #returns TRUE as it is their , vice versa
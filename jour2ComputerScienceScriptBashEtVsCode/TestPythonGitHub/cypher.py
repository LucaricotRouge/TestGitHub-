import sys

mode = None

def usage(): 
    print('python3 cypher.py [cypher/decypher], key, message')

key = sys.argv[2]
mot = sys.argv[3]

if(len(sys.argv) != 4):
    usage()
    sys.exit(0)

elif (sys.argv[1] == "cypher"): 
    mode = "cypher"
    key = int(sys.argv[2]) % 26
elif(sys.argv[1] == "decypher"): 
    mode = "decypher"
    key = -(int(sys.argv[2]) % 26)
else:
    print("commande non supportee : {sys.argv[1]}")
    usage()
    sys.exit(0)

response = ''
for current_character in sys.argv[3]:
    dec = ord(current_character) + key 
    if(dec > ord('z')):
        dec -= 26
    elif(dec < ord('a')): 
        dec += 26
    response += chr(dec)

print(response)



# lMot = len(mot)
# print(ord(mot[0]))

# nMot = mot

#if(mode == "cypher"):
    #for i in range(lMot):
        #nMot[i] = chr(ord(nMot[i]) + key)
    #print("Le mot chiffré est : ", nMot)


#else:
    #for i in range(lMot): 
        #nMot[i] = chr(ord(nMot[i])) - key
    #print("Le mot déchiffré est : ", nMot)


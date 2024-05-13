# to check for double space in string
st="this is a  string with  double spaces"
doublespaces=st.find("  ")
print(doublespaces)


#to replace double space with single space
st=st.replace("  "," ")
print(st)

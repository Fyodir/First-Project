x = input("Please insert Chromosomal Nucleotide Sequence ")
x = x.upper()

def conv(y):
    z = []
    for i in y:
        if i == "G":
            z.append("C")
        elif i == "C":
            z.append("G")
        elif i == "A":
            z.append("U")
        elif i == "T":
            z.append("A")
    return (z)

x =  "".join(conv(x))

print("")
print("Nucleotide Sequence of Complimentary Strand (RNA):")
print(x)

print("")
print("Read Frame 1: Triplet Code Sequence of Complimentary Strand (RNA):")
x1 = ([x[i:i + 3] for i in range(0, len(x), 3)])
print (x1)

print("")
print("Read Frame 2: Triplet Code Sequence of Complimentary Strand (RNA):")
x2 = ([x[i:i + 3] for i in range(1, len(x), 3)])
print (x2)

print("")
print("Read Frame 3: Triplet Code Sequence of Complimentary Strand (RNA):")
x3 = ([x[i:i + 3] for i in range(2, len(x), 3)])
print (x3)

print("")


# develop code below to call codons beginning with a START codon, ending in a STOP codon

def start_stop(sequence):
  result = []
  a = 0 
  for i in sequence:
    if a == 0:
      pass
    elif i == "AUG":
      a+= 1
      result.append(i)
    elif i != "AUG" or "UAA" or "UAG" or "UAA" and a != 0:
      result.append(i)
    elif i == "UAA" or "UAG" or "UAA":
      return
  return(result)
      

# print(start_stop(x1))

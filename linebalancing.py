from line2 import next_person
import copy


def plus_next_per(li_2):
    seq = []
    for se in li_2:
        seq = seq + se
    li_3 = []
    if next_person(seq) == [[]]:
        li_3.append(li_2)
    else:
        for se_2 in next_person(seq):
            li_2_b = copy.copy(li_2)
            li_2_b.append(se_2)
            li_3.append(li_2_b)
    return li_3


def next_phase(li_3):
    sequences = []
    for past_phase in li_3:
        sequences = sequences + plus_next_per(past_phase)
    return sequences


def all_phase():
    sequences_b = [[]]
    while True:
        sequences_b = next_phase(sequences_b)
        if sequences_b == next_phase(sequences_b):
            break
    return sequences_b


A = all_phase()
# for i in A:
#     print(i)

Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]

B = []
for line in A:
    B_line = []
    for person in line:
        B_person = []
        for task in person:
            B_person.append(Alphabet[task])
        B_line.append(B_person)
    B.append(B_line)


for line in B:
    print(line)

print(len(A))

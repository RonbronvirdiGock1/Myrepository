amount=int(input("enter an amount to withdraw"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes of 100",note_1)
print("notes of 50",note_2)
print("notes os 10",note_3)
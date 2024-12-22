name=input("Enter your name:")

def relation_to_Luke(name):
    count=1
    person=["Darth Vader","Leia","Han","R2D2"]
    relation=["Father","Sister","Brother in Law","Droid"]
    for i in range(4):
        if name.lower()==person[i].lower():
            print(f"Luke,I am your {relation[i]}.")
            count+=1
            break
    if count==1:
        print("Luke! I have no relation with you!!!")


relation_to_Luke(name)
#Class assignments
#Subfields of artificial intelligence
class SubfieldsInAI():
    def subfields():
        list1 = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing","Natural Language Processing"]
        print("Subfields of AI are:")
        for i in range(len(list1)):
            print(list1[i])
            
    def oddoreven():
        num1=int(input("Enter num 1"))
        if(num1%2 == 0):
            print("Even")
        else:
            print("Odd")
            
    def marriageeligible():
        gender=input("Enter the gender")
        age=int(input("Enter the age"))
        if(gender == "Male" and age >= 21):
            print("Eligible")
        elif(gender == "Female" and age >= 18):
            print("Eligible")
        else:
            print("Not Eligible")

    def calcavg():
        totalno = int(input("Enter the total no of Subjects : "))
        list1 = []
        totalmarks =0
        for i in range(totalno):
            mark = int(input(f"Subject{i+1}:"))
            list1.append(mark)
        for i in range(len(list1)):
            totalmarks = totalmarks + list1[i]
        print(totalmarks/totalno)

    def calareaper():
        option = int(input("Enter 1 and 2 to calculate area and perimeter respectively"))
        if(option == 1):
            h1 = float(input("Enter Height1"))
            b = float(input("Enter breadth"))
            area = (h1*b)/2
            print(area)
        elif(option == 2):
            h1 = float(input("Enter Height1"))
            h2 = float(input("Enter Height2"))
            b = float(input("Enter breadth"))
            per = h1+h2+b
            print(per)
        else:
            print("Enter 1 or 2 only")    
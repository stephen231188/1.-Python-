class multipleFunctions():
    
    def Subfields():
        list = ["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in list:
            print(i)
            
    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print(num, "is odd Number")
        else:
            print(num, "is even Number")  

    def Elegible():
        Gender=input("Your Gender: ")
        Age=int(input("Your Age: "))
        if(Gender=="Male"):
          if(Age >=21):
            print("ELIGIBLE")
            message="ELIGIBLE"
          else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        elif(Gender=="Female"):
          if(Age >18):
            print("ELIGIBLE")
            message="ELIGIBLE"
          else:
            print("ELIGIBLE")
            message="NOT ELIGIBLE"
                       
    def percentage():
        a=int(input("Subject1= "))
        b=int(input("Subject2= "))
        c=int(input("Subject3= "))
        d=int(input("Subject4= "))
        e=int(input("Subject5= "))
        add=a+b+c+d+e
        print(("Total: "), add)
        message="Total"
        per=(add)*(100/500)
        print(("Percentage: "),per)
        message="Percentage"
        
    def triangle():
        Height = float(input('Height: '))
        Breadth = float(input('Breadth: '))
        formula = (Height*Breadth)/2
        print ("Area formula: (Height*Breadth)/2\nArea of Triangle:", formula)
        Height1 = int(input('Height1: '))
        Height2 = int(input('Height2: '))
        Breadth1 = int(input('Breadth1: '))
        formula = Height1+Height2+Breadth1
        print ("Perimeter formula: Height1+Height2+Breadth\nPerimeter of Triangle:", formula)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
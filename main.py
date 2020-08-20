import gen 
# import creat
import os



disease_list = []

def add_new():
    with open("diseases.txt") as fi:
        fi = fi.read()
        disease_list = fi.split("\n")
    na = input("new disease name: ")  ### input name of new disease
    if disease_list.count(na)>0:
        print("disease already exists\nexiting program")
        exit()
    with open("diseases.txt","a") as fi:
        fi.write("\n"+na)
    fi = open("./Disease descriptions/"+na+".txt","w")
    fi.write(input("enter desease description: "))
    fi.close()
    fi= open("./Disease treatments/"+na+".txt","w")
    fi.write(input("enter disease treatments: "))

    with open("symptoms.txt") as fi:
        fi = fi.read()
        symptom_list = fi.split("\n")

    print("does the disease have the following symptoms?")
    fi = open("./Disease symptoms/"+na+".txt","w")
    fir=0
    for symptom in symptom_list:
        inti=  input(symptom+": ")
        if (fir ==0):
            fi.write(inti )
            fir+=1
        else:
            fi.write("\n"+ inti)

    fi_2 = open("symptoms.txt","a")
    while (input("new symptom?  ")=="yes"):  ############### asks if you want to input a new symptom
        inti = input("symptom: ")
        fi_2.write("\n"+inti)
        fi.write("\nyes")
    
        list_edit = os.listdir("./Disease symptoms")
        for fil in list_edit:
            if fil != (na+".txt"):
                fit = open("./Disease symptoms/"+fil,"a")
                fit.write("\nno")
                fit.close()
    print("succesfully added new disease")




if __name__ == "__main__":

    if input("are you a doctor: ") =="yes":  ### asks if you are doctor if you are it creates new disease 
        print("welcome\n adding new disease")
        add_new()
        print("thanks")
             
    else :                         ########### patient (actual program)
        gen.gen_exec()  ## generates knowledge base  (check creat.py)
        print("created knowledge base")

        import creat  ### creat is created righ tabove so importing it before is not possible
        creat.patient_inter()
        # os.system('cmd /c "py creat.py"')  ## query knowledge base
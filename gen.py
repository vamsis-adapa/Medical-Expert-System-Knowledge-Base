
def gen_exec():

    with open("creat.py","w") as final:
        

        with open("segs/1.txt") as fi:
            fi_r = fi.read()
            final.write(fi_r)
        
        symptoms_list = []

        with open("symptoms.txt") as fi_s:
            sym = fi_s.read()
            symptoms_list = sym.split('\n')
        # print(symptoms_list)
        num =0
        for symptom in symptoms_list:
            # print(symptom)
            final.write("	@Rule(Fact(action='find_disease'), NOT(Fact("+symptom+"=W())),salience = 1)\n")
            final.write("	def symptom_"+str(num)+"(self):\n"+"		self.declare(Fact("+symptom+"=input(\""+symptom+": \")))\n\n")
            num+=1

        diseases_list =[]

        with open("diseases.txt") as di_s:
            dis = di_s.read()
            diseases_list = dis.split('\n')
        num=0
        for disease in diseases_list:
            final.write("	@Rule(Fact(action='find_disease')")
            dis_sym_val =[]
            with open("./Disease symptoms/"+disease+".txt") as sym_dis:
                dis_sym_val_t = sym_dis.read()
                dis_sym_val = dis_sym_val_t.split("\n")
            for i in range(len(symptoms_list)):
                final.write(",Fact("+symptoms_list[i]+"=\""+dis_sym_val[i]+"\")")
            final.write(")\n")
            final.write("	def disease_"+str(num)+"(self):\n"+"		self.declare(Fact(disease=\""+disease+"\"))\n\n")
            num+=1
        
        with open("segs/2.txt") as fi:
            fi_r = fi.read()
            final.write(fi_r)
        
        final.write("	@Rule(Fact(action='find_disease'),\n")
        for symptom in symptoms_list:
            final.write("		  Fact("+symptom+"=MATCH."+symptom+"),\n")
        final.write("		  NOT(Fact(disease=MATCH.disease)),salience = -999)\n\n")

        final.write("	def not_matched(self")
        for sym in symptoms_list:
            final.write(", "+sym)
        final.write("):\n		print(\"Did not find any disease that matches your exact symptoms\")\n		lis = [")
        for i in range(len(symptoms_list)):
            if i == len(symptoms_list)-1:
                final.write(symptoms_list[i]+"]\n")
            else:
                final.write(symptoms_list[i]+", ")
        with open("segs/3.txt") as fi:
            fi_r = fi.read()
            final.write(fi_r)


if __name__ == "__main__":
    gen_exec()
        



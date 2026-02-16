import pandas as pd
#sample data
data = {"Name":["Ravi", "sitha", "Ajay", "Anita"],
        "Marks": [85,78,92,66]}
df=pd.DataFrame(data)
#print average marks
print ("Average marks:", df["Marks"].mean())
#students above 80 marks
top_students= df[df['Marks'] > 80]
print("top students:\n",top_students)

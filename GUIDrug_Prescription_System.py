# All the required Libraries are listed here.
from tkinter import *
import pickle
import tkinter as tk
from time import sleep


symptoms=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
    ' Migraine','Cervical spondylosis',
    'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

drugSolution = {'Fungal infection': 'fluconazole','Allergy' : 'Antihistamines','GERD': 'omeprazole',
'Chronic cholestasis': 'Ursodeoxycholic Acid','Drug Reaction': 'Diphenhydramine (Benadryl)',
    'Peptic ulcer diseae':'Proton pump inhibitors (PPIs)','AIDS':'dronabinol','Diabetes':'hydrochlorothiazide',
    'Gastroenteritis':'erythromycin','Bronchial Asthma' : 'prednisolone','Hypertension':'lisinopril',
    ' Migraine':'Sumatriptan','Cervical spondylosis':'ibuprofen','Paralysis (brain hemorrhage)' : 'Cyklokapron',
    'Jaundice':'Phenobarbital','Malaria': 'Mefloquine','Chicken pox' : 'Valacyclovir ','Dengue':'Acetaminophen',
    'Typhoid':'Ciprofloxacin','hepatitis A':'Immune Globulin Intramuscular',
    'Hepatitis B':'Entecavir','Hepatitis C':'Ribavirin','Hepatitis D':'Pegylated interferon alpha','Hepatitis E':'Ribavirin',
    'Alcoholic hepatitis':' Corticosteroids','Tuberculosis':'Prednisone',
    'Common Cold':'Diphenhydramine','Pneumonia':'Prednisone','Dimorphic hemmorhoids(piles)':'Hydrocortisone',
    'Heartattack':'Captopril','Varicoseveins':'Asclera (polidocanol)',
    'Hypothyroidism':'Levothyroxine','Hyperthyroidism':'Methimazole','Hypoglycemia':'Glucagon','Osteoarthristis':'Diclofenac',
    'Arthritis':'Methotrexate','(vertigo) Paroymsal  Positional Vertigo':'Antivert',
    'Acne':'Doxycycline','Urinary tract infection':'Ciprofloxacin','Psoriasis':'Clobetasol',
    'Impetigo':'Mupirocin'
}

dr=[]
for i in range(0,len(symptoms)):
    dr.append(0)


root = Tk()
pred1=StringVar()
pred2=StringVar()
pred3=StringVar()
pred4=StringVar()
Name = StringVar()
feed=False
prescription=StringVar()
disease_estimator=""
drugName=""



def clear():
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)

def submit():
    print('Drug Name:{}'.format(entry_name.get()))
    print('Disease:{}'.format(entry_email.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    if((str(entry_name.get)=="") or (str(entry_email.get())=="") or (str(textcomment.get(1.0,END))=="")):
        sym=messagebox.askokcancel("System","Please fill the required fields.")
        if sym:
            root1.mainloop()
    else:
        sleep(3)
        print("Your FeedBack is being Collected !...")
        sleep(2)
        print(" The Message is sent to the server !.")
        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        feed=False
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)
        root1.destroy()

def feedback():
    from tkinter import ttk
    global entry_name
    global emaillabel
    global entry_email
    global commentlabel
    global textcomment
    global myvar
    global email
    global root1
    global frame_header
    global frame_content
    root1 = tk.Tk()
    frame_header = ttk.Frame(root1)
    frame_header.pack()
    myvar = StringVar()
    email = StringVar()
    headerlabel = ttk.Label(frame_header, text='Customer Feedback', foreground='Black',
                        font=('Times', 24))
    headerlabel.grid(row=0, column=1)
    frame_content = ttk.Frame(root1)
    frame_content.pack()
    namelabel = ttk.Label(frame_content, text='Drug Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')

    entry_name = ttk.Entry(frame_content, width=18, font=('Times', 12), textvariable=myvar)
    entry_name.grid(row=1, column=0)

    emaillabel = ttk.Label(frame_content, text='Disease')
    emaillabel.grid(row=0, column=1, sticky='sw')

    entry_email = ttk.Entry(frame_content, width=18, font=('Times', 12), textvariable=email)
    entry_email.grid(row=1, column=1)

    commentlabel = ttk.Label(frame_content, text='Feedback', font=('Times', 10))
    commentlabel.grid(row=2, column=0, sticky='sw')

    textcomment = Text(frame_content, width=55, height=10)
    textcomment.grid(row=3, column=0, columnspan=2)
    textcomment.config(wrap ='word')
    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')
    root1.mainloop()

def ModelsPrediction():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        print(NameEn.get())

        dtc_model=pickle.load(open('dtc_model.sav','rb'))
        gnb_model=pickle.load(open('GNB_model.sav','rb'))
        knn_model=pickle.load(open('knn_model.sav','rb'))
        rf_model=pickle.load(open('RandomForest_model.sav','rb'))

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
        
        for k in range(0,len(symptoms)):
            for z in psymptoms:
                if(z==symptoms[k]):
                    dr[k]=1
        
        inputtest = [dr]
        predict_dtc = dtc_model.predict(inputtest)
        predict_gnb = gnb_model.predict(inputtest)
        predict_knn = knn_model.predict(inputtest)
        predict_rf = rf_model.predict(inputtest)
        predicted_dtc=predict_dtc[0]
        predicted_gnb=predict_gnb[0]
        predicted_knn=predict_knn[0]
        predicted_rf=predict_rf[0]
        
        h='no'
        for a in range(0,len(disease)):
            if(predicted_dtc == a):
                h1='yes'
            if(predicted_gnb == a):
                h2='yes'
            if(predicted_knn == a):
                h3='yes'
            if(predicted_rf==a):
                h4='yes'
    
        if (h1=='yes' and h2=='yes' and h3=='yes' and h4=='yes'):
            pred1.set(" ")
            pred2.set(" ")
            pred3.set(" ")
            pred4.set(" ")
            pred1.set(disease[predicted_dtc])
            pred2.set(disease[predicted_gnb])
            pred3.set(disease[predicted_knn])
            pred4.set(disease[predicted_rf])
            diseases_models=[pred1.get(),pred2.get(),pred3.get(),pred4.get()]
            highest_occur = {i:diseases_models.count(i) for i in diseases_models}
            disease_estimator=max(highest_occur,key=highest_occur.get)
            drugName=drugSolution[disease_estimator]
            prescription.set("The patient is suffering from "+disease_estimator+"\nThe Prescribed Drug is "+drugName+".")
            feed=True
        if(feed):
            feedback()
        else:
            pred1.set(" ")
            pred1.set("Not Found")




        
#Tk class is used to create a root window
root.configure(background='Ivory')
root.title('Drug Prescription System')
root.resizable(0,0)

#First input as symptom
Symptom1 = StringVar()
Symptom1.set("Select Here")

#Second input as symptom
Symptom2 = StringVar()
Symptom2.set("Select Here")

#Third input as symptom
Symptom3 = StringVar()
Symptom3.set("Select Here")

#Fourth input as symptom
Symptom4 = StringVar()
Symptom4.set("Select Here")

#Fifth input as symptom
Symptom5 = StringVar()
Symptom5.set("Select Here")


# function to Reset the given inputs to initial position
prev_win=None
def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")
    
    NameEn.delete(first=0,last=100)
    
    pred1.set(" ")
    pred2.set(" ")
    pred3.set(" ")
    pred4.set(" ")
    try:
        prev_win.destroy()
        prev_win=None
    except AttributeError:
        pass
    
# Exit button to come out of system
from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    if qExit:
        root.destroy()
        exit()
        
# Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="Drug Prescription System using Machine Learning", fg="Black", bg="Ivory")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)

# Label for the name
NameLb = Label(root, text="Patient Name", fg="Black", bg="Ivory")
NameLb.config(font=("Times",15,"bold"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)

# Creating Labels for the symtoms
S1Lb = Label(root, text="Symptom 1", fg="Black", bg="Ivory")
S1Lb.config(font=("Times",15,"bold"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="Black", bg="Ivory")
S2Lb.config(font=("Times",15,"bold"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Black",bg="Ivory")
S3Lb.config(font=("Times",15,"bold"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="Ivory")
S4Lb.config(font=("Times",15,"bold"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="Ivory")
S5Lb.config(font=("Times",15,"bold"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)


dst = Button(root, text="Prediction", command=ModelsPrediction,bg="White",fg="Black")
dst.config(font=("Times",15,"bold"))
dst.grid(row=15, column=0,padx=10)

rs = Button(root,text="Reset Inputs", command=Reset,bg="white",fg="Black",width=15)
rs.config(font=("Times",15,"bold"))
rs.grid(row=17,column=0,padx=10)

ex = Button(root,text="Exit System", command=Exit,bg="red",fg="white",width=15)
ex.config(font=("Times",15,"bold"))
ex.grid(row=20,column=0,padx=10)

OPTIONS = sorted(symptoms)

# Name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

# Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)


t1=Label(root,font=("Times",10),text=" ",textvariable=prescription,height=10,bg="White",width=45,fg="Black",relief="sunken").grid(row=15, column=1, padx=15)

root.mainloop()
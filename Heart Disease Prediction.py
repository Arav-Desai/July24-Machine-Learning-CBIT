import tkinter
from tkinter import ttk
import pandas as p

#connecting to Excel sheet
b = p.read_excel('D:/Arav C/Downloads/heart disease prediction.xlsx')
b.to_excel(excel_writer='heart disease prediction.xlsx', sheet_name='heart disease prediction')
table = p.DataFrame(b)

#taking a single column from Excel
df = p.ExcelFile('D:/Arav C/Downloads/heart disease prediction.xlsx').parse('heart disease prediction.xlsx')

sc=tkinter.Tk()
#sc1=tkinter.Tk()

global nm, age,sx,cpt,choles,rbp,fbs,ecg,ea,st,maxHR,op ,Heart_disease,pro_cpt ,pro_fbs_hd , pro_ecg_hd , pro_ea_hd , pro_st_hd

pro_cpt=0
pro_fbs_hd =0
pro_ecg_hd =0
pro_ea_hd =0
pro_st_hd=0
nm=""
age=0
sx=''
cpt=""
choles=0
rbp=0
fbs=0
ecg=''
ea=''
st=0
maxHR=0
op=0

def submit():
    global nm, age, sx, cpt, choles, rbp, fbs, ecg, ea, st, maxHR, op, Heart_disease, pro_cpt, pro_fbs_hd, pro_ecg_hd, pro_ea_hd, pro_st_hd
    age=spn1.get()
    nm=name.get()
    sx=cb.get()
    cpt = cb1.get()
    choles = spn3.get()
    rbp = spn2.get()
    fbs = 1 if cb2.get()=='HIGH' else 0
    ecg = cb3.get()
    ea = 'Y' if cb4.get() =='YES' else 'N'
    st = cb5.get()
    maxHR = spn4.get()
    op = spn5.get()

    sc1=tkinter.Tk()
    sc1.title("Confirmation")
    sc1.geometry("250x300")
    #strg= "Age Entered by " + nm +" "+ str(age)
    labl1 = ttk.Label(sc1, text='Name: '+nm, width=50)
    labl1.grid(column=10, row=1)

    labl2 = ttk.Label(sc1, text='Age: '+str(age),width=50)
    labl2.grid(column=10, row=2)

    labl3=ttk.Label(sc1,text="Gender"+sx,width=50)
    labl3.grid(column=10,row=3)

    labl4 = ttk.Label(sc1, text='Resting BP: '+str(rbp), width=50)
    labl4.grid(column=10, row=4)

    labl5 = ttk.Label(sc1, text='Cholesterol: '+str(choles), width=50)
    labl5.grid(column=10, row=5)

    labl6 = ttk.Label(sc1, text='Chest Pain Type: '+cpt, width=50)
    labl6.grid(column=10, row=6)

    labl7 = ttk.Label(sc1, text='Fasting Blood Sugar: '+str(fbs), width=50)
    labl7.grid(column=10, row=7)

    labl8 = ttk.Label(sc1, text="Resting ECG: "+ecg, width=50)
    labl8.grid(column=10, row=8)

    labl9 = ttk.Label(sc1, text="Excercise Angina : "+str(ea), width=50)
    labl9.grid(column=10, row=9)

    labl10 = ttk.Label(sc1, text="St Slope: "+st, width=50)
    labl10.grid(column=10, row=10)

    labl11 = ttk.Label(sc1, text="old Peak: "+str(op), width=50)
    labl11.grid(column=10, row=11)

    labl12 = ttk.Label(sc1, text="Max Heart Rate: "+str(maxHR), width=50)
    labl12.grid(column=10, row=12)

    btn11 = ttk.Button(sc1, text="OK", width=10, command=sc1.destroy)
    btn11.grid(column=10, row=13)

    sc.destroy()
    sc1.mainloop()


sc.title("Prototype")
sc.geometry("300x300")

#taking name
lbl1=ttk.Label(sc,text="Name:",width=15,justify="left")
lbl1.grid(column=5,row=10)

name= ttk.Entry(width=20)
name.grid(column=15,row=10)

#taking age
lbl2=ttk.Label(sc,text="Age :",width=15,justify="left")
lbl2.grid(column=5, row=15)

spn1=ttk.Spinbox(from_=0,increment=1,to=100,width=20)
spn1.grid(column=15,row=15)

#taking sex
lbl3=ttk.Label(sc,text="Gender:",width=15)
lbl3.grid(column=5,row=20)

cb=ttk.Combobox(sc,state="readonly",width=20)
cb['values']=('MALE','FEMALE')
cb.grid(column=15,row=20)

#taking chest pain type
lbl4=ttk.Label(sc,text="Chest Pain Type :",width=15,justify="left")
lbl4.grid(column=5,row=25)

cb1=ttk.Combobox(sc,state="readonly",width=20)
cb1['values']=('ATA','TA','ASY','NAP')
cb1.grid(column=15,row=25)

#taking resting BP
lbl5=ttk.Label(sc,text='Resting Blood Pressure',width=20)
lbl5.grid(column=5,row=30)

spn2=ttk.Spinbox(sc,from_=70,to=200,width=20,increment=1)
spn2.grid(column=15,row=30)

#taking cholesterol
lbl6=ttk.Label(sc,text='Cholesterol',width=15)
lbl6.grid(column=5,row=35)

spn3=ttk.Spinbox(sc,from_=0,to=700,increment=1,width=20)
spn3.grid(column=15,row=35)

#taking Fasting Blood sugar
lbl7=ttk.Label(sc,text='Fasting Blood Sugar',width=20)
lbl7.grid(column=5,row=40)

cb2=ttk.Combobox(sc,state="readonly",width=20)
cb2['values']=('HIGH','LOW')
cb2.grid(column=15,row=40)

#taking Resting ECG
lbl8=ttk.Label(sc,text='Resting ECG',width=15)
lbl8.grid(column=5,row=45)

cb3=ttk.Combobox(sc,state="readonly",width=20)
cb3['values']=('NORMAL','LVH','ST')
cb3.grid(column=15,row=45)

#taking Max HR
lbl9=ttk.Label(sc,text='Maximum Heart Rate',width=20)
lbl9.grid(column=5,row=50)

spn4=ttk.Spinbox(sc,from_=50,to=250,increment=1,width=20)
spn4.grid(column=15,row=50)

#taking excersise angina
lbl10=ttk.Label(sc,text='Excersise Angina',width=15)
lbl10.grid(column=5,row=55)

cb4=ttk.Combobox(sc,state="readonly",width=20)
cb4['values']=('YES','NO')
cb4.grid(column=15,row=55)

#taking Old Peak
lbl11=ttk.Label(sc,text='Old Peak',width=15)
lbl11.grid(column=5,row=60)

spn5=ttk.Spinbox(sc,from_=0,to=2,increment=1,width=20)
spn5.grid(column=15,row=60)

#taking ST slope
lbl12=ttk.Label(sc,text='ST Slope',width=15)
lbl12.grid(column=5,row=65)

cb5=ttk.Combobox(sc,state='readonly',width=20)
cb5['values']=('UP','DOWN','FLAT')
cb5.grid(column=15,row=65)

#submit button
btn= ttk.Button(sc,text="Submit",command=submit)
btn.grid(column=15, row=70)

sc.mainloop()


def Heart ():
    global pro_cpt, pro_fbs_hd, pro_ecg_hd, pro_ea_hd, pro_st_hd, pro_cpt_not, pro_ecg_nothd, pro_fbs_nothd, pro_ea_nothd, pro_st_nothd,Heart_disease,pro_sex,pro_notsex,pro_cpt,pro_cpt_not,pro_fbs_hd,pro_fbs_nothd,pro_ecg_nothd,pro_ecg_hd,pro_ea_hd,pro_ea_nothd,pro_st_hd ,pro_st_nothd
    pro_cpt_not=0
    pro_ecg_nothd=0
    pro_fbs_nothd=0
    pro_ea_nothd=0
    pro_st_nothd=0
    pro_sex=0
    pro_notsex=0
    pro_cpt =0
    pro_cpt_not =0
    pro_fbs_hd =0
    pro_fbs_nothd=0
    pro_ecg_hd =0
    pro_ecg_nothd =0
    pro_ea_hd=0
    pro_ea_nothd=0
    pro_st_hd=0
    pro_st_nothd=0

    # universal probability
    uni_pro={'rows_hd':508/919,'rows_nothd':410/919}

    #first all discrete values probabilities will be counted
    #sex probabilities
    sex_pro={'pro_m_hd':458/508,'pro_f_hd':50/508,'pro_m_nothd':267/411,'pro_f_nothd':143/411}

    pro_sex=sex_pro['pro_m_hd'] if sx=='MALE' else sex_pro['pro_f_hd']
    pro_notsex=sex_pro['pro_m_nothd'] if sx=='MALE' else sex_pro['pro_f_nothd']

    #chest pain probabilities
    cpt_pro={'pro_asy_hd':392 / 508,
             'pro_nap_hd':72 / 508,
             'pro_ata_hd':24 / 508,
             'pro_ta_hd':20 / 508,
             'pro_asy_nothd':104 / 414,
             'pro_ata_nothd':149 / 414,
             'pro_ta_nothd':26 / 414,
             'pro_nap_nothd':131 / 414}

    if cpt == 'ASY':
        pro_cpt = cpt_pro['pro_asy_hd']
        pro_cpt_not = cpt_pro['pro_asy_nothd']
    elif cpt == 'NAP':
        pro_cpt = cpt_pro['pro_nap_hd']
        pro_cpt_not = cpt_pro['pro_nap_nothd']
    elif cpt == 'ATA':
        pro_cpt = cpt_pro['pro_ata_hd']
        pro_cpt_not = cpt_pro['pro_ata_nothd']
    elif cpt == 'TA':
        pro_cpt = cpt_pro['pro_ta_hd']
        pro_cpt_not = cpt_pro['pro_ta_nothd']

    #fasting blood sugar probabilities
    fbs_pro={'pro_low_hd':338/508,
            'pro_high_hd':170/508,
            'pro_low_nothd':336/414,
            'pro_high_nothd':78/414}

    if fbs == 1:
        pro_fbs_hd=fbs_pro['pro_high_hd']
        pro_fbs_nothd = fbs_pro['pro_high_nothd']
    elif fbs== 0:
        pro_fbs_hd=fbs_pro['pro_low_hd']
        pro_fbs_nothd=fbs_pro['pro_low_nothd']

    #resting ecg probabilities
    ecg_pro={'pro_lvh_hd':106/508,
            'pro_normal_hd':285/508,
            'pro_st_hd':117/508,
            'pro_lvh_nothd':82/414,
            'pro_st_nothd':61/414,
            'pro_normal_nothd':267/414}

    if ecg=='LVH':
        pro_ecg_hd=ecg_pro['pro_lvh_hd']
        pro_ecg_nothd=ecg_pro['pro_lvh_nothd']
    elif ecg=='NORMAL':
        pro_ecg_hd = ecg_pro['pro_normal_hd']
        pro_ecg_nothd = ecg_pro['pro_normal_nothd']
    elif ecg=='ST':
        pro_ecg_hd = ecg_pro['pro_st_hd']
        pro_ecg_nothd = ecg_pro['pro_st_nothd']

    #exc angina probabilities
    ea_pro={'pro_yes_hd':316/508,
            'pro_no_hd':192/508,
            'pro_yes_nothd':55/414,
            'pro_no_nothd':355/414}

    if ea=='Y':
        pro_ea_hd=ea_pro['pro_yes_hd']
        pro_ea_nothd=ea_pro['pro_yes_hd']
    elif ea=='N':
        pro_ea_hd = ea_pro['pro_no_hd']
        pro_ea_nothd =ea_pro['pro_no_nothd']

    #st slope probability
    st_pro={'pro_up_hd':78/508,
            'pro_down_hd':49/508,
            'pro_flat_hd':381/508,
            'pro_up_nothd':317/414,
            'pro_down_nothd':14/414,
            'pro_flat_nothd':79/414}

    if st=='UP':
        pro_st_hd=st_pro['pro_up_hd']
        pro_st_nothd=st_pro['pro_up_nothd']
    elif st=='DOWN':
        pro_st_hd = st_pro['pro_down_hd']
        pro_st_nothd = st_pro['pro_down_nothd']
    elif st=='FLAT':
        pro_st_hd = st_pro['pro_flat_hd']
        pro_st_nothd =st_pro['pro_flat_nothd']

    #probability of all continuous data
    #age probability
    age_nothd=0
    age_hd=0
    i=0
    for rownum in df.Age:
        if df.HeartDisease[i]==0:
            #age_nothd.append(df['Age'][i])
            age_nothd = age_nothd + int(df['Age'][i])
        else:
            #age_hd.append(df['Age'][i])
            age_hd=age_hd+int(df['Age'][i])
        i=i+1
    age_hd=age_hd/508
    age_nothd=age_nothd/414


    #resting blood pressure probility
    bp_nothd =0
    bp_hd = 0
    i = 0
    for rownum in df.RestingBP:
        if df.HeartDisease[i] == 0:
            bp_nothd=bp_nothd+int(df['RestingBP'][i])
        else:
            bp_hd=bp_hd+int(df['RestingBP'][i])
        i = i + 1
    bp_hd=bp_hd/508
    bp_nothd=bp_nothd/414


    #cholesterol probability
    choles_nothd = 0
    choles_hd = 0
    i = 0
    for rownum in df.Cholesterol:
        if df.HeartDisease[i] == 0:
            choles_nothd=choles_nothd+int(df['Cholesterol'][i])
        else:
            choles_hd=choles_hd+int(df['Cholesterol'][i])
        i = i + 1
    choles_hd=choles_hd/508
    choles_nothd=choles_nothd/414


    #heart rate probability
    hr_nothd = 0
    hr_hd = 0
    i = 0
    for rownum in df.MaxHR:
        if df.HeartDisease[i] == 0:
            hr_nothd=hr_nothd+int(df['MaxHR'][i])
        else:
            hr_hd=hr_hd+int(df['MaxHR'][i])
        i = i + 1
    hr_hd=hr_hd/508
    hr_nothd=hr_nothd/414


    #old peak
    op_nothd = 0
    op_hd = 0
    i = 0
    for rownum in df.Oldpeak:
        if df.HeartDisease[i] == 0:
            op_nothd=op_nothd+int(df.Oldpeak[i])
        else:
            op_hd=op_hd+int(df.Oldpeak[i])
        i = i + 1
    op_hd=op_hd/508
    op_nothd=op_nothd/414


    #probabilities of heart disease and not heart disease
    hd=uni_pro['rows_hd']* pro_sex * pro_cpt * pro_fbs_hd * pro_ecg_hd * pro_ea_hd * pro_st_hd * age_hd * bp_hd*choles_hd*hr_hd*op_hd
    nothd=uni_pro['rows_nothd'] * pro_notsex * pro_cpt_not * pro_ecg_nothd * pro_fbs_nothd * pro_ea_nothd * pro_st_nothd *age_nothd*bp_nothd*choles_nothd*hr_nothd*op_nothd

    #comparing the data provided by patient
    if hd>=nothd:
        Heart_disease='True'
    elif hd<nothd:
        Heart_disease='False'
    else:
        Heart_disease='not able to do'

    return Heart_disease
#sx, cpt, fbs, ecg, ea, st, df

sc3=tkinter.Tk()
sc3.title("Results")
sc3.geometry("500x250")

label1=ttk.Label(sc3,text="Name:"+nm,width=20)
label1.grid(column=1,row=1)

label2=ttk.Label(sc3,text="Results:-",width=10)
label2.grid(column=1,row=2)

res=''
result=Heart()
if result:
    res="High chances of heart disease"
elif not result:
    res="Low chances of heart disease"

label3=ttk.Label(sc3, text=res ,width=50)
label3.grid(column=2,row=3)

bt=ttk.Button(sc3,text="Ok",command=sc3.destroy,width=5)
bt.grid(column=1,row=5)

sc3.mainloop()

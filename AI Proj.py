import datetime
from tkinter import *
import tkinter.messagebox
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
global patcount
global riskcount
global reportcount
global far
patcount = 0
riskcount = 0
reportcount = 0
SymptomDB = []

#add database window class
class DbaseWindow:
    def __init__(self, win2):

        self.L6 = Label(win2, text = "Add Dengue Symptoms", fg = '#D5D9FE', bg='#37394C' ,)
        self.L6.place(x = 10,y = 10)
        self.namevar1 = Entry(win2,bd = 3)
        self.namevar1.place(x = 200,y = 10)



        self.namevar2 = Entry(win2,bd = 3)
        self.namevar2.place(x = 200,y = 30)

        self.namevar3 = Entry(win2,bd = 3)
        self.namevar3.place(x = 200,y = 50)

        self.namevar4 = Entry(win2,bd = 3)
        self.namevar4.place(x = 200,y = 70)

        self.namevar5 = Entry(win2,bd = 3)
        self.namevar5.place(x = 200,y = 90)

        self.B1 = Button(win2, text = "Accept", fg = '#D5D9FE', bg='#37394C' , command = self.getval)
        self.B1.place(x = 240,y = 150)

    def getval(self):
        global SymptomDB
        symptom = self.namevar1.get()
        symptom2 = self.namevar2.get()
        symptom3 = self.namevar3.get()
        symptom4 = self.namevar4.get()
        symptom5 = self.namevar5.get()
        SymptomDB.append(symptom)
        SymptomDB.append(symptom2)
        SymptomDB.append(symptom3)
        SymptomDB.append(symptom4)
        SymptomDB.append(symptom5)
        print(*SymptomDB, sep = "\n")
        # An information box
        tkinter.messagebox.showinfo("Information","Entry recorded.")

        #creates text file if it does not exist. a+ assigns append authority
        f= open("symptoms.txt","a+")
        #append to file
        #               formats                variables
        f.write("%s \n%s \n%s \n%s \n%s \n" % (symptom, symptom2, symptom3, symptom4, symptom5))
        #close file
        f.close()

#diagnosis window class
class MyWindow:
    def __init__(self, win):
        self.L1 = Label(win, text = "Enter Patient's Name", fg = '#D5D9FE', bg='#37394C' )
        self.L1.place(x = 10,y = 10)
        self.namevar = Entry(win,bd = 3)
        self.namevar.place(x = 300,y = 10)

        self.L2 = Label(win, text = "Enter your Patient's temperature (°C)", fg = '#D5D9FE', bg='#37394C' )
        self.L2.place(x = 10,y = 40)
        self.ptemp = Entry(win,bd = 3)
        self.ptemp.place(x = 300,y = 40)

        self.L3 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 1st symptom (If Any)")
        self.L3.place(x = 10,y = 70)
        self.stsym = ""
        self.stsym = Entry(win,bd = 3)
        self.stsym.place(x = 300,y = 70)

        self.L4 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 2nd symptom (If Any")
        self.L4.place(x = 10,y = 110)
        self.ndsym = Entry(win,bd = 3)
        self.ndsym.place(x = 300,y = 110)

        self.L5 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 3rd symptom (If Any")
        self.L5.place(x = 10,y = 140)
        self.rdsym = Entry(win,bd = 3)
        self.rdsym.place(x = 300,y = 140)

        self.L6 = Label(win, fg = '#D5D9FE', bg='#37394C' ,text = "Enter your Patient's 4th symptom (If Any)")
        self.L6.place(x = 10,y = 170)
        self.foursym = Entry(win,bd = 3)
        self.foursym.place(x = 300,y = 170)


        self.L7 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 5th symptom (If Any)")
        self.L7.place(x = 10,y = 200)
        self.fivesym = Entry(win,bd = 3)
        self.fivesym.place(x = 300,y = 200)

        self.L8 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 6th symptom (If Any)")
        self.L8.place(x = 10,y = 230)
        self.sixsym = Entry(win,bd = 3)
        self.sixsym.place(x = 300,y = 230)

        self.L9 = Label(win, fg = '#D5D9FE', bg='#37394C' , text = "Enter your Patient's 7th symptom (If Any)")
        self.L9.place(x = 10,y = 260)
        self.sevensym = Entry(win,bd = 3)
        self.sevensym.place(x = 300,y = 260)

        self.B1 = Button(win, text = "Accept Patient Entry", fg = '#D5D9FE', bg='#37394C' , command = self.getvals)
        self.B1.place(x = 150,y = 300)

    def getvals(self):
        global reportcount
        pnam = self.namevar.get()
        firstsym = self.stsym.get()
        secondsym = self.ndsym.get()
        thirdsym = self.rdsym.get()
        sixthsym = self.sixsym.get()
        fifthsym = self.fivesym.get()
        seventhsym = self.sevensym.get()
        fourthsym = self.foursym.get()
        patienttemp = int(self.ptemp.get())
        currentdate = date.today()


        #creates text file if it does not exist. a+ assigns append authority
        f= open("patient.txt","a+")
        #append to file
        #               formats                variables
        f.write("%s %i %s %s %s %s %s %s %s %s \n" % (pnam, patienttemp, firstsym, secondsym, thirdsym, fourthsym, fifthsym, sixthsym, seventhsym, currentdate))
        #close file
        f.close()

        symcheck = 0
        symcheck1 = 0
        symcheck2 = 0
        symcheck3 = 0
        symcheck4 = 0
        symcheck5 = 0
        symcheck6 = 0
        points=0
        print(" ")
        print("****************DIAGNOSIS******************")


        with open('symptoms.txt') as f:
            datafile = f.readlines()

            if firstsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == firstsym:
                        print("%s is a Symptom of Dengue" %(firstsym))
                        symcheck += 1
                        points += 1

            if firstsym != "":
                if symcheck == 0:
                    print("%s is not a Dengue Symptom" %(firstsym))

            if secondsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == secondsym:
                        print("%s is a Symptom of Dengue" %(secondsym))
                        symcheck1 += 1
                        points += 1

            if secondsym != "":
                if symcheck1 == 0:
                    print("%s is not a Dengue Symptom" %(secondsym))

            if thirdsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == thirdsym:
                        print("%s is a Symptom of Dengue" %(thirdsym))
                        symcheck2 += 1
                        points += 1

            if thirdsym != "":
                if symcheck2 == 0:
                    print("%s is not a Dengue Symptom" %(thirdsym))

            if fourthsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == fourthsym:
                        print("%s is a Symptom of Dengue" %(fourthsym))
                        symcheck3 += 1
                        points += 1

            if fourthsym != "":
                if symcheck3 == 0:
                    print("%s is not a Dengue Symptom" %(fourthsym))

            if fifthsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == fifthsym:
                        print("%s is a Symptom of Dengue" %(fifthsym))
                        symcheck4 += 1
                        points += 1

            if fifthsym != "":
                if symcheck4 == 0:
                    print("%s is not a Dengue Symptom" %(fifthsym))

            if sixthsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == sixthsym:
                        print("%s is a Symptom of Dengue" %(sixthsym))
                        symcheck5 += 1
                        points += 1

            if sixthsym != "":
                if symcheck5 == 0:
                    print("%s is not a Dengue Symptom" %(sixthsym))

            if seventhsym != "":
                for line in datafile:
                    line = line.split('=')
                    line[0] = line[0].strip()
                    if line[0] == seventhsym:
                        print("%s is a Symptom of Dengue" %(seventhsym))
                        symcheck6 += 1
                        points += 1

            if seventhsym != "":
                if symcheck6 == 0:
                    print("%s is not a Dengue Symptom" %(seventhsym))

            f.close()

        far = patienttemp * 9/5 + 32
        if patienttemp > 37:
            points += 1
            print("You have a fever (%i" %(far)+'°F)')
        elif patienttemp == 37:
            print("Your temperature is normal (%i" %(far)+'°F)')
        else:
            print("Your temperature is not normal (%i" %(far)+'°F)')


        if points >= 7:
            print("You have severe Dengue")
            reportcount = reportcount + 1
            f= open("riskpatient.txt","a+")
            f.write("%s %i %s %s %s %s %s %s %s %s \n" % (pnam, patienttemp, firstsym, secondsym, thirdsym, fourthsym, fifthsym, sixthsym, seventhsym, currentdate))
            f.close()
        elif points == 3 or points == 4 or points == 5 or points == 6:
            print("There's a high risk you have dengue fever")
            reportcount = reportcount + 1
            f= open("riskpatient.txt","a+")
            f.write("%s %i %s %s %s %s %s %s %s %s \n" % (pnam, patienttemp, firstsym, secondsym, thirdsym, fourthsym, fifthsym, sixthsym, seventhsym, currentdate))
            f.close()
            f=open("MDengue.txt", "r")
            fl =f.readlines()
            html_out="***********Dengue Treatment************\n\n"
            for x in fl:
                html_out+=x
                html_out+="\n"
            tkinter.messagebox.showinfo("Information",html_out)
            f.close()
        else:
            print("You most likely don't have dengue fever")
            print(points)
            f=open("SDengue.txt", "r")
            fl =f.readlines()
            html_out="***********Dengue Prevention************\n\n"
            for x in fl:
                html_out+=x
                html_out+="\n"
            tkinter.messagebox.showinfo("Information",html_out)
            f.close()




#Main window class
class MainWindow:
    def __init__(self, win1):
        self.B0 = Button(win1, bg='#37394C', text = "Add to Database", fg = '#D5D9FE',  command = self.dbasewin)
        self.B0.place(x = 150,y = 20)
        self.B2 = Button(win1, bg='#37394C', text = "Diagnose Patient", fg = '#D5D9FE', command = self.dodiag)
        self.B2.place(x = 150,y = 80)
        self.B3 = Button(win1, bg='#37394C', text = "Display Statistics", fg = '#D5D9FE',  command = self.dispstats)
        self.B3.place(x = 150,y = 140)
        self.B3 = Button(win1, bg='#37394C', text = "  Display Query   ", fg = '#D5D9FE', command = self.query)
        self.B3.place(x = 150,y = 200)
        self.B4 = Button(win1, bg='#37394C', text="  Display Report  ", fg='#D5D9FE', command=self.report)
        self.B4.place(x=150, y=260)

    #Display add to database window
    def dbasewin(self):
        top2=Tk()
        mywin2=DbaseWindow(top2)
        top2.configure(bg='#434774')
        top2.title('Add to database')
        top2.geometry("500x300+20+20")
        top2.mainloop()

    #Display diagnosis window
    def dodiag(self):
        top=Tk()
        mywin=MyWindow(top)
        top.configure(bg='#434774')
        top.title('Diagnosis')
        top.geometry("500x400+20+20")
        top.mainloop()

    def report(self):
        january = '2020-01-'
        february = '2020-02-'
        march = '2020-03-'
        april = '2020-04-'
        may = '202-05-'
        june = '2020-06-'
        july = '2020-07-'
        august = '2020-08-'
        september = '2020-09-'
        october = '2020-10-'
        november = '2020-11-'
        december = '2020-12-'
        jantot = 0
        rjantot = 0
        febtot = 0
        rfebtot = 0
        martot = 0
        rmartot = 0
        aprtot = 0
        raprtot = 0
        maytot = 0
        rmaytot = 0
        juntot = 0
        rjuntot = 0
        jultot = 0
        rjultot = 0
        augtot = 0
        raugtot = 0
        septot = 0
        rseptot = 0
        octtot = 0
        rocttot = 0
        novtot = 0
        rnovtot = 0
        dectot = 0
        rdectot = 0

        with open('patient.txt') as filly:
            linechart = filly.readlines()
        for line in linechart:
            if january in line:
                jantot += 1
            if february in line:
                febtot += 1
            if march in line:
                martot += 1
            if april in line:
                aprtot += 1
            if may in line:
                maytot += 1
            if june in line:
                juntot += 1
            if july in line:
                jultot += 1
            if august in line:
                augtot += 1
            if september in line:
                septot += 1
            if october in line:
                octtot += 1
            if november in line:
                novtot += 1
            if december in line:
                dectot += 1
        filly.close()

        with open('riskpatient.txt') as fil:
            linechart = fil.readlines()
        for line in linechart:
            if january in line:
                rjantot += 1
            if february in line:
                rfebtot += 1
            if march in line:
                rmartot += 1
            if april in line:
                raprtot += 1
            if may in line:
                rmaytot += 1
            if june in line:
                rjuntot += 1
            if july in line:
                rjultot += 1
            if august in line:
                raugtot += 1
            if september in line:
                rseptot += 1
            if october in line:
                rocttot += 1
            if november in line:
                rnovtot += 1
            if december in line:
                rdectot += 1
        fil.close()

        # data to plot
        n_groups = 12
        patients = (jantot, febtot, martot, aprtot, maytot, juntot, jultot, augtot, septot, octtot, novtot, dectot)
        riskpatients = (rjantot, rfebtot, rmartot, raprtot, rmaytot, rjuntot, rjultot, raugtot, rseptot, rocttot, rnovtot, rdectot)

        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, patients, bar_width, alpha=opacity, color='b', label='Patients')

        rects2 = plt.bar(index + bar_width, riskpatients, bar_width, alpha=opacity, color='r', label='Patients at Risk')

        plt.xlabel('Month')
        plt.ylabel('Amount of Patients')
        plt.title('Admitted Patients and Patients at risk')
        plt.xticks(index + bar_width, ('January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
        plt.legend()

        plt.tight_layout()
        plt.show()

    def query(self):
        global patcount
        global riskcount
        global reportcount

        with open('patient.txt') as f:
            for line in f:
                patcount += 1
        f.close()

        with open('riskpatient.txt') as f:
            for line in f:
                riskcount += 1
        f.close()

        totalperc = riskcount / patcount * 100
        print ("The total Percentage of people at risk of Dengue Fever is %i" %(round(totalperc))+'%')

    def dispstats(self):
        global patcount
        global riskcount
        global reportcount

        with open('patient.txt') as f:
            for line in f:
                patcount += 1
        f.close()

        with open('riskpatient.txt') as f:
            for line in f:
                riskcount += 1
        f.close()

        print(" ")
        print("****************STATISTICS******************")
        print("Total number of patients:")
        print(patcount)
        print("Persons at risk for Dengue:")
        print(riskcount)

        today = date.today()

        if today == date.today():
            if reportcount > 2:
                print("There is an unusual increase in Dengue fever today")

        #Open the file back and read the contents
        f = open("patient.txt", "r")
        #readlines reads the individual line into a list
        fl = f.readlines()

        #output to messagebox
        html_out="***********Patient Data************\n\n"
        for x in fl:
            html_out+=x
            html_out+="\n"
        tkinter.messagebox.showinfo("Information",html_out)
        f.close()

#Displays main window
top1=Tk()
mywin1=MainWindow(top1)
top1.title('Main Menu')
top1.configure(bg='#434774')
top1.geometry("400x300+20+20")
top1.mainloop()
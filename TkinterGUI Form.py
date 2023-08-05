from csv import DictWriter
import os
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('GUI')

# Creat lebel
name_label = ttk.Label(win,text='Enter your name : ')
# name_label.pack()
name_label.grid(row = 0 ,column=0,sticky=tk.W)

email_label = ttk.Label(win,text='Enter your email : ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label = ttk.Label(win,text='Enter your age : ')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label = ttk.Label(win,text='Select your gender : ')
gender_label.grid(row=3,column=0,sticky=tk.W)

# Creat Entrybox
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=25,textvariable=name_var)
name_entrybox.grid(row=0,column=1,sticky=tk.W)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=25,textvariable=email_var)
email_entrybox.grid(row=1,column=1,sticky=tk.W)
# email_entrybox.focus()
age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width= 25,textvariable=age_var)
age_entrybox.grid(row=2,column=1,sticky=tk.W)


# Create Combobox
gender_var = tk.StringVar()
gender_combox  = ttk.Combobox(win,width=22,textvariable=gender_var,state='readonly')
gender_combox['values'] = ('Male','Female','Others')
gender_combox.current(0)
gender_combox.grid(row=3,column=1,sticky=tk.W)

#Create Radiobutton
usertype = tk.StringVar()
radiobutton1 = ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobutton1.grid(row=4,column=0,sticky=tk.W)

radiobutton2 = ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobutton2.grid(row=4,column=1,sticky=tk.W)

# Cheak Button
cheak_var = tk.IntVar()
cheakbutton = ttk.Checkbutton(win,text='cheak of subscribe our newslatter',variable=cheak_var)
cheakbutton.grid(row=5,columnspan=3,sticky=tk.W)


# Create button 
# def action():
#     user_name = name_var.get()
#     user_email = email_var.get()
#     user_age = age_var.get()
#     user_gender = gender_var.get()
#     user_type = usertype.get()
    # print(f"{user_name} is {user_age} year old {user_gender} {user_type}, their email is {user_email}")
    # if cheak_var.get()==0:
    #     subscribed = 'NO'
    # else:
    #     subscribed = 'yes'
    # print(f"Is the user subscribed the newslatter : {subscribed}")
    # with open('data_gui_1st.txt','a') as f :
        # f.write(f'username : {user_name}\n userage : {user_email}\n userage : {user_age} \n usergender : {user_gender} \n usertype : {user_type} \n subcribed : {subscribed}\n')
    # name_entrybox.delete(0,tk.END)
    # email_entrybox.delete(0,tk.END)
    # age_entrybox.delete(0,tk.END)
    # name_label.configure(foreground='blue')
    # email_label.configure(foreground='blue')
    # age_label.configure(foreground='blue')
    # gender_label.configure(foreground='blue')
    # radiobutton1.configure(foreground='blue')
    # radiobutton2.configure(foreground='blue')
    # cheakbutton.configure(foregroung = 'blue')
    # submit_button.configure(background='blue')
# submit_button = ttk.Button(win,width=13,text='Submit',command=action)    # because is has no attibute backgroung (it needs styling)



# write in csv
def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if cheak_var.get()==0:
        subscribed = 'NO'
    else:
        subscribed = 'yes'
    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Red')
    email_label.configure(foreground='Red')
    age_label.configure(foreground='blue')
    gender_label.configure(foreground='blue')
    submit_button.configure(background='blue')

    with open ('data_gui_1st.csv','a') as rf :
        dict_writer = DictWriter(rf,fieldnames=['User Name','User Email Adress','User Age','User Gender','User Type','User Sbscribed'])
        if os.stat('data_gui_1st.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name' : user_name,
            'User Email Adress': user_email,
            'User Age': user_age,
            'User Gender': user_gender,
            'User Type': user_type,
            'User Sbscribed': subscribed
        })

submit_button = tk.Button(win,width=13,text='Submit',command=action)
submit_button.grid(row=6,column=0)


win.mainloop()

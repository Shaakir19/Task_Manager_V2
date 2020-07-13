# Task Number : 1
# File Name : task_manger.py
# Written by : Shaakir Caroto
# Date Written : 21/02/2020
# Date modified : 04/03/2020
# The function of this program : This program is used for a small business that has a login and allows the user to do multiple tasks 
# like registering user and tasks and stores them in text file
# this program also uses function

# This function is the admin's menu function which allows the admin to see all the option they have to choose from.
def admin_menu():

   print("Please select one of the following options : ")
   print
   print("r - register user")
   print("a - add task")
   print("va - view all tasks")
   print("vm - view my tasks")
   print("gr - generate reports")
   print("ds - display statistics")
   print("e - exit")
   print

# This function is the user's menu function which allows any user who is not the admin to view all the option they have to choose from
def user_menu():
   
   print("Please select one of the following options : ")
   print
   print("a - add task")
   print("va - view all tasks")
   print("vm - view my tasks")
   print("e - exit")
   print 

# This function is used in another function called reg_user 
# This function check if the new user being register has already been registered 
def check_user(new_user,new_pass,file_user,in_pass,in_user):
    
    # This is open the text file to read
    f = open(file_user,"r")

    for line in f:
       # For line in the text file f
       # Make line into a list by using list
         line = line.split(",")
       # Replace the space of line[1] with nothing
         line[1] = line[1].replace(" ","")
       # Replace the "\n" of line[1] with nothing
         line[1] = line[1].replace("\n","")
       
       # if the new_user entered equals line[0] then it continues
         if new_user == line[0]:
            # new_user a user input variable 
            # if new_user equal any of the items in the list line
            # Display the following message

            msg = "Please re-enter the username \n This username is already in use"
            print(msg)

            # And set the boolean variable "in_user" to true
            in_user = True 
    else:  
        # if the new_user entered does not equal line[0] then to continues
         if new_user != line[0]:
            # else Display the following message
            msg = "The user is alright"
            print(msg)

            # And set the boolean variable "in_user" to false
            in_user = False
         
    # Close the file
    f.close()
    
    # opening the text file to read 
    f = open(file_user,"r")

    for line in f:
         # For line in the text file f
         # Make line into a list by using list
         line = line.split(",")
         # Replace the space of line[1] with nothing
         line[1] = line[1].replace(" ","")
         # Replace the "\n" of line[1] with nothing
         line[1] = line[1].replace("\n","")

         # if  the  new_pass entered equals line[1] then it continues
         if new_pass == line[1]:
            # new_pass a user inputted variable 
            # new_pass equals any of the password int the line list 
            # Display the following message
            msg = "Please re-enter the password \n This password is already in use "
            print(msg)

            # And set the boolean variable "in_pass" to true
            in_pass = True
    else: 
         # if the new_pass entered does not equal line[1] then to continues
         if new_pass != line[1]:
            
            # else Display the following message 
            msg = "The password is alright"
            print(msg)

            # And set the boolean variable "in_pass" to false
            in_pass = False
      
    # Close the file
    f.close()
    # Return the boolean variables
    return in_user, in_pass

# This function is used to register new users and their passwords to the users text file for the login process
def reg_user(new_user,new_pass,file_user,in_pass,in_user):
   
   # Open the text file to append which allows the user to write to the text file without clearing the text file
   f_user = open(file_user,"a")

   # Using a while true to do the following
   while True:
      # Calling the check_user function to check if the user is allready registered
      check_user(new_user,new_pass,file_user,in_pass,in_user)

      if (in_pass == True) and (in_user == True):
         # if any of the boolean variables from the check funnctions are to the two boolean variables then it will do the following
         # Make the inputs equal nothing 
         new_pass = ""
         new_user = ""
         # Asks for new inputs
         new_user = input("Please enter the username again as the previous one is in use : ")
         new_pass = input("Please enter the password again as the previous one is in use : ")
         
      if (in_pass == False) or (in_user == True):
         # One the boolean variables are true 
         # Clears the string variable and asks for the input again
         new_user = ""
         new_user = input("Please enter the username again as the previous one is in use : ")

      if (in_pass == True) or (in_user == False):
         # One the boolean variables are true 
         # Clears the string variable and asks for the input again
         new_pass = ""
         new_pass = input("Please enter the password again as the previous one is in use : ")
      
      if (in_pass == False) and (in_user == False):
         # if none of them are true 
         # the loop will break
         break

   # Requests input for  vaildation
   vail_pass = input("Please enter the password of the new user again : ")
   
   while True:
      # Using a while true for so the continues can continues until a break is called
      if new_pass == vail_pass:
         # Display the following messages and then calls the break to break the loop
         print("Thank you")
         print("You have added a new user")
         break
      else:
         # else it will display a message  and then ask for the input again
         print("The passwords are not the same please try again")
         vail_pass = input("Please enter the password of the new user again : ")

   # The inputs will be assigned a variable as string
   user = f"{new_user}, {new_pass}"
   # The variable is then written to the text file
   f_user.writelines(f"{user}\n")
   # Displays a message to the user
   print("The user has been registered and now can use the program")
   # Closes the text file
   f_user.close()

# This function is used to add a new task to the task text file
def add_task(task_user,title_task,description_task,issue_task,due_date_task,task_complete,file_task):
   
   # The text file is first opening to append which allows the user to write without clearing the whole text file
   f_task = open(file_task,"a")
  
   # the while loop checks if any of the inputs are empty
   while task_user == " " or task_user == "" or title_task == " " or title_task == "" or description_task == " " or description_task == "" or issue_task == " " or issue_task == "" or due_date_task == "" or due_date_task == " " or  task_complete == "" or task_complete == " ":
      # it there is one that is empty then the program will ask you to input all of the inputs again
      print("Please re-input your answers")
      task_user = input('Enter the name of the user who is going to do the task : ')
      title_task = input("Enter the title of the task : ")
      description_task = input("Enter the description of the task : ")
      print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
      issue_task = input("Enter the current date of the task bring issued : ")
      print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
      due_date_task = input("Enter the date the task is due : ")
      print("Please enter yes or no ")
      task_complete = input("Enter if the task is complete or not : ").lower()
      task_complete.capitalize()
   else:
      # else a message will be displayed and the information assigned to a variable 
      print("You have answered all the questions")
      task = f"{task_user}, {title_task}, {description_task}, {issue_task}, {due_date_task}, {task_complete}\n"
   
   # then the variable will be written to the task file
   f_task.writelines(f"{task}")
   
   # Closing the text file
   f_task.close()

# This function is the view all function which allows the user to view all of the tasks in the task file 
def view_all(file_task):

   # Openning the text file to read first 
   f = open(file_task,"r")

   for line in f:
      # for line in the text file f
      # Replace the "\n" in line
      # And split the line by using the commas
      line = line.replace("\n","")
      line = line.split(",")

      # Assign each item to a variable and check if the first item is empty
      user_assigned = line[0]
      if line[0] == "":
         break
      title = line[1]
      description = line[2]
      date_issued = line[3]
      date_due = line[4]
      task_comp = line[5]

      # Display display each variable in a user friendly manner
      print(f"The title of the task : {title}")
      print(f"The user that this task is assigned : {user_assigned}")
      print(f"The description of the task : {description}")
      print(f"The date the task is issued : {date_issued}")
      print(f"The due date of the task  : {date_due}")
      print(f"Is the task completed : {task_comp}")
      print("")

   # Close the file 
   f.close()

# This function allows the user to view of their tasks and they are able to edit them if need be
def view_mine(ent_user,file_task) :

    # First openning the file to read
    f = open(file_task,"r")


    for no ,line in enumerate(f):
       # for no and line in the enumerate of f the text file
       # increase no by one each time
       # Replace the \n in line
       # Split by the comma in line
       no += 1
       line = line.replace("\n","")
       line = line.split(",")

       if ent_user in line:
          # if the username signed in is equal to the line then
          # Assign each item a variable
           user_assigned = line[0]
           title = line[1]
           description = line[2]
           date_issued = line[3]
           date_due = line[4]
           task_comp = line[5]

           # Display each of the variable in a user friendly manner
           print(f"Task Number : {no}")
           print(f"The title of the task : {title}")
           print(f"The user that this task is assigned : {user_assigned}")
           print(f"The description of the task : {description}")
           print(f"The date the task is issued : {date_issued}")
           print(f"The due date of the task  : {date_due}")
           print(f"Is the task completed : {task_comp}")
           print("")

    # Close the reading file
    f.close()

    # open the file to read again
    f = open(file_task,"r")
    
    # Ask the user if they want to view a specific task by a number input
    spec_task = int(input("Enter a specific task you would like to look at (Enter -1 if you want to go the menu) : "))
    
    if spec_task == -1:
        # If the user inputs "-1" then the following message will display
         print("You have choosen to not edit the task.")
    else:
       
       for no ,line in enumerate(f.readlines()) :
           # for no and line in the enumerate in f.readlines
           # Replace "\n" in line
           # Split line by comma
           # increase no by 1
           line = line.replace("\n","")
           line = line.split(",")
           no += 1
    
           if  ent_user == line[0] and spec_task == no:
              # If the ent_user equals line[0] and spac_task equals no
              # Assign each item a variable 
              # and display in a user friendly manner
              user_assigned = line[0]
              title = line[1]
              description = line[2]
              date_issued = line[3]
              date_due = line[4]
              task_comp = line[5]
              print(f"Task Number : {no}")
              print(f"The title of the task : {title}")
              print(f"The user that this task is assigned : {user_assigned}")
              print(f"The description of the task : {description}")
              print(f"The date the task is issued : {date_issued}")
              print(f"The due date of the task  : {date_due}")
              print(f"Is the task completed : {task_comp}")
              print("") 
    
       # close the file
       f.close()

       # Creating a new list and it has nothing
       # this will be used in the storing of the none selected lines
       new_line = []
       
       # Open the text file to read and write
       f = open(file_task, "r+")
    
       for no, line in enumerate(f.readlines()):
          # For no and line in the enumerate in f.readlines
          # Split line by spaces
          # increase no by 1
          line = line.split(" ")
          no += 1

          if spec_task != no:
             # if spec_task does not equal no
             for x in line:
                 # for x in line
                 # Append x to the list new_line
                 new_line.append(f"{x} ")     
      
       # close the text file
       f.close()
 
       # open the text file to read and write
       f = open(file_task, "r+")
    
       # Create a holding string variable to help with the editing of the tasks
       ed_task = ""
    
       for no, line in enumerate(f.readlines()):
          # for no and line in the enumerate of f.readlines
          # increase no by 1
           line = line.split(",")
           no += 1
          
           if ent_user == line[0] and spec_task == no : 
              # if ent_user equals line[0] and spec_task equals no
              # Request an input from the user
               edit_task = input("Would you like to mark the task as complete or change something else about the task (Please answer with other or mark) : ").lower()
                
               if edit_task == "other" :
                  # if edit_task equal "other"
                  #  Request a new input from the user 
                  # This input is meant  to help the user to input a specific item they want to edit
                  task_comp = input("Enter the name of the compenent that you wolud like to edit (Please enter user, title, description or due date) : ").lower()
    
                  if task_comp == "user":
                     # if the user inputs "user"
                     # Request an input from the user
                     # Assign the new input to the list 
                     # Assign all the items to a new variable
                     # use truncate to clear the file
                    edit = input("What would you like to change it to : ")
                    line[0] = edit
                    ed_task = f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}"
                    f.truncate(0)

                    # close the file
                    f.close()
                    # Open a new file to write too
                    f = open(file_task, "w")
    
                    for x in new_line:
                       # for x in new_line
                       # the list holder all of the unselected tasks
                       # Write x to the f
                       f.write(f"{x}")
                    # write the newly edited list to the text file
                    f.write(ed_task)
                    # Close the file
                    f.close()
    
    
                  elif task_comp == "title":
                     # if the user inputs "title"
                     # Request an input from the user
                     # Assign the new input to the list 
                     # Assign all the items to a new variable
                     # use truncate to clear the file
                    edit = input("What would you like to change it to : ")
                    line[1] = edit
                    ed_task = f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}"
                    f.truncate(0)

                     # close the file
                    f.close()
                     # Open a new file to write too
                    f = open(file_task, "w")
    
                    for x in new_line:
                        # for x in new_line
                       # the list holder all of the unselected tasks
                       # Write x to the f
                       f.write(f"{x}")
                    # write the newly edited list to the text file   
                    f.write(ed_task)
                     # Close the file
                    f.close()
    
    
                  elif task_comp == "description":
                     # if the user inputs "description"
                     # Request an input from the user
                     # Assign the new input to the list 
                     # Assign all the items to a new variable
                     # use truncate to clear the file
                    edit = input("What would you like to change it to : ")
                    line[2] = edit
                    ed_task = f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}"
                    f.truncate(0)

                     # close the file
                    f.close()
                    # Open a new file to write too
                    f = open(file_task, "w")


                    for x in new_line:
                        # for x in new_line
                       # the list holder all of the unselected tasks
                       # Write x to the f
                       f.write(f"{x}")
                    # write the newly edited list to the text file    
                    f.write(ed_task)
                    # Close the file
                    f.close()
    
    
                  elif task_comp == "due date":
                      # if the user inputs "due date"
                     # Request an input from the user
                     # Assign the new input to the list 
                     # Assign all the items to a new variable
                     # use truncate to clear the file
                    edit = input("What would you like to change it to : ")
                    line[4] = edit
                    ed_task = f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}"
                    f.truncate(0)

                     # close the file
                    f.close()
                     # Open a new file to write too
                    f = open(file_task, "w")

                    for x in new_line:
                       # for x in new_line
                       # the list holder all of the unselected tasks
                       # Write x to the f
                       f.write(f"{x}")
                    # write the newly edited list to the text file    
                    f.write(ed_task)
                     # Close the file
                    f.close()
    
                  else:
                     # else if the user does not input the correct input 
                     print("The option unavailble or not able to change")
                   
                  # if the user wants to edit if the task is complete
                  if edit_task == "mark":
                     # if the user inputs "mark"
                     # Request an input from the user
                     # Assign the new input to the list 
                     # Assign all the items to a new variable
                     # use truncate to clear the file
                     # making edit lower and then capitalizing it to help with statistics later in the program
                    edit = input("What would you like to change it to : ").lower()
                    edit.capitalize()
                    line[5] = edit + "\n"
                    ed_task = f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}"
                    f.truncate(0)

                    # close the file
                    f.close()
                    # Open a new file to write too
                    f = open(file_task, "w")

                    for x in new_line:
                        # for x in new_line
                       # the list holder all of the unselected tasks
                       # Write x to the f
                       f.write(f"{x}")
                    # write the newly edited list to the text file    
                    f.write(ed_task)
                    # Close the file
                    f.close()
       
       # Closing the text file
       f.close()

# This function generate reports to show the user the statistics of the company 
def gen_report(re_f_task,re_f_user,file_task,file_user,month_dir):
   
   # opening both the task file and the user file
   f_task = open(file_task,"r")
   f_user = open(file_user,"r")
   
   # creating a date variable to help with date compairson
   currect_date = datetime.date.today()

   # creating integer variable and assigning them to 0
   i = 0
   comp = 0
   not_comp = 0
   overdue = 0
   
   # Creating the two new file to help with statistics
   # opening them to write and read
   re_f_task = open("task_overview.txt","w+")


   for line in f_task:
      # for line in the f_task file
      # replace the "\n" with line
      # Split line by comma
      # Increase i by 1
      # Replace the space of line[5] with nothing
      line = line.replace("\n","")
      line = line.split(",")
      i += 1
      line[5] = line[5].replace(" ","")


      # line[5] equals "yes"
      # increase comp by 1
      if line[5] == "Yes":
         comp += 1

      # if line[5] equals "No"
      # increase no_comp by 1
      if line[5] == "No":
         not_comp += 1

      # Line[4] is striped
      # And it is split by the spaces
      # Making the second item into the integer version of the month
      # Using a dictionary to do the convertion
      # Assing the new value to the list 
      # And converting it to a date  
      line[4] = line[4].strip()
      date = line[4].split(" ")
      month = month_dir[date[1]]
      date[1] = month
      date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
      
      # Comparing the date to see if it is overdue and no complete
      if date < currect_date and line[5] != "Yes":
         overdue += 1
  
  # Using the information to do calculations
   per_ovedue = (overdue/i) * 100
   per_not = (not_comp/i) * 100

   # Dsiplaying the information in a user friendly manner and writing it to the text file
   re_f_task.write(f"The total nummber of task's : {i} \n")
   re_f_task.write(f"The total number of task's completed : {comp} \n")
   re_f_task.write(f"The total number of task's incomplete : {not_comp} \n")
   re_f_task.write(f"The total number of task's overdue : {overdue} \n")
   re_f_task.write(f"The percentage of task's that are overdue : {per_ovedue:.0f} % \n")
   re_f_task.write(f"The percentage of task's that are incomplete : {per_not:.0f} % \n")

   # Closing the text file f_task
   f_task.close()
   
   # Closing the text file re_f_task
   re_f_task.close()

   # Creating the new text file user_overview to help with the statistics and openning it to write
   re_f_user = open("user_overview.txt","w+")

   # Creating a new integer variable and making it zero
   num_user = 0


   for line in f_user :
      # for line in the file f_user 
      # Replace the "\n" in line with nothing
      # Split line by comma
      # increase num_user by 1
      line = line.replace("\n","")
      line = line.split(",")
      num_user += 1
    
   # write the information to the file
   re_f_user.write(f"The total number of users : {num_user} \n")
   re_f_user.write(f"The total number of tasks : {i} \n")
   # close both of the files
   f_user.close()
   re_f_user.close()
   
   # Open the users and task file again to read
   f_user = open(file_user,"r")
   f_task = open(file_task,"r")
   
   # creating an empty list
   user_lst = []


   for no,line in  enumerate(f_user.readlines()):
      # for no and line in enumerate f_user.readlines
      # Split line by the comma
      # line equal line[0]
      # Append line to user_lst
      no = no
      line = line.split(",")
      line = line[0]
      user_lst.append(line)
  
  # Close both text files
   f_task.close()
   f_user.close()

   while True:
      # While true to continue reading until there is a break found
      # creating integer variables and assign then 0
      task_num = 0
      user_com = 0
      user_not = 0
      user_overdue = 0

      # open the task file to read
      # opne the user_overview to append
      f_task = open(file_task,"r")
      re_f_user = open("user_overview.txt","a")

      while user_lst != []:
         # While the user_lst not empty
         # Write the user name to the text file
         re_f_user.write(f"User : {user_lst[0]} \n")

         for task in f_task:
            # for task in f_task file
            # Split task by comma
            task = task.split(",")

            if user_lst[0] in task[0]:
               # if user_lst is in the task list
               # Increase task_num by one
               # Replace the "\n" and the space with nothing in task[5]
               task_num += 1
               task[5] = task[5].replace("\n","")
               task[5] = task[5].replace(" ","")

               # If task[5] is equal to "Yes"
               # increase user_com by 1
               if task[5] == "Yes":
                     user_com += 1

               # If task[5] is equal to "No"
               # increase user_com by 1
               if task[5] == "No":
                     user_not += 1


               # Line[4] is striped
               # And it is split by the spaces
               # Making the second item into the integer version of the month
               # Using a dictionary to do the convertion
               # Assing the new value to the list 
               # And converting it to a date            
               task[4] = task[4].strip()
               date = task[4].split(" ")
               month = month_dir[date[1]]
               date[1] = month
               date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
      
               # Comparing the date to see if it is overdue and no complete
               if date < currect_date and task[5] != "Yes":
                  user_overdue += 1

         # Writing the information to the text file and doing calculations and checking if the information equals 0
         re_f_user.write(f"The Total number of task from {user_lst[0]} : {task_num} \n")
         user_task_per = (task_num/i) * 100
         re_f_user.write(f"The percentage of tasks for {user_lst[0]} : {user_task_per:.0f} % \n")
         if user_com != 0:
            user_com_per = (user_com/task_num) * 100
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {user_com_per:.0f}% \n")
         else:
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {0} % \n")

         if user_not != 0:
            user_not_per = (user_not/task_num) * 100
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {user_not_per:.0f}% \n")
         else:
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {0} % \n")
         
         if user_not != 0 :
            user_overdue_per = (user_overdue/task_num) * 100
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {user_overdue_per:.0f}% \n")
         else: 
            re_f_user.write(f"The percentage of complete tasks for {user_lst[0]} : {0} % \n")

         # Using pop to delete the first item from the text file
         user_lst.pop(0)

         # Closing both the text file
         f_task.close()
         re_f_user.close()

         # breaking the loop
         break

   # Closing the text file
   f_task.close()
   f_user.close()

# This function displays the information generated in the gen_report function                  
def display_statistic(re_f_task,re_f_user,file_task,file_user,month_dir):
   # assigning the files a variable
   re_f_task = "task_overview.txt"
   re_f_user = "user_overview.txt"

   # Checking if the file paths exists
   # Which creates a boolean variable
   exist_task = path.exists(re_f_task)
   exist_user = path.exists(re_f_user)


   if exist_task != True and exist_user != True:
     # exist_task and exist_user does not equal true
     # Dislpay the following messages
      print("The text file that you need have not been generated")
      print("Please generate the reports first")
      print("You can do that by selecting the gr option")
      

   if exist_task == True and exist_user == True:
      # if they both equal true
      # display the follow message 
      print("This is the task report:")
      print("=" * 50)

      # Open the text file to read 
      report_task = open(re_f_task,"r")

      for line in report_task:
         # for line in the report_task
         # replace the "\n" with nothing
         line = line.replace("\n","")
         # Display the line
         print(line)
      # Display the "\n"
      print("\n")
      
      # Display the follow message
      print("This is the user report:")
      print("=" * 50)

      # Open the text file to read
      report_user = open(re_f_user,"r")

      for line in report_user:
         # for line in the report_user
         # replace the "\n" with nothing
         line = line.replace("\n","")
         # Display the line
         print(line)
       # Display the "\n"
      print("\n")
   
   # Close both of the text files
   report_task.close()
   report_user.close()
 
# Importing packages to help with running of the program
from datetime import datetime
import datetime
import os.path 
from os import path

# Created a dictionary to convert the string to the integer month
month_dir = {"Jan" : 1 ,
             "Feb" : 2 ,
             "Mar" : 3 ,
             "Apr" : 4 , 
             "May" : 5 , 
             "Jun" : 6 ,
             "Jul" : 7 ,
             "Aug" : 8 , 
             "Sep" : 9 ,
             "Oct" : 10 ,
             "Nov" : 11 ,
             "Dec" : 12}      

# This opening the user.txt 
# These lines of code (lines 809 - 817 ) are getting the admin's username and password to check if the user enters the admin information
# line 817 is the file being closes for later use 
f_user = open("user.txt","r")
line = f_user.readline()
line = line.replace("\n","")
line = line.split(",")
line[1] = line[1].replace(" ","")
line[1] = line[1].replace("\n","")
admin = line[0]
admin_pass = line[1]
f_user.close()

# lines 820 and 821 are the user inputs for the login in process
ent_user = input("Enter your username : ")
ent_pass = input("Enter your password : ")

# if the user inputs the admins username and password
if (ent_user == admin) and (ent_pass == admin_pass):
   # Using a while true to continue until a break is called
   while True : 
      # Displaying the username and the admin's menu function
      print(f"Welcome : {ent_user}")
      print("=" * 50)
      admin_menu()
   
      print()
      
      # Requesting a input from the user
      option_int = input("Enter which option you would like to use : ").lower()
   
      while option_int == "r" or option_int == "a" or option_int == "vm" or option_int == "va" or option_int == "gr" or option_int == "ds" or option_int == "e":
         # While the inputs equal the following above 
         # This is used if the user does not input the correct the inputs

         # This is if the user wants to register a new user
         if option_int == "r":
            
            # Displaying which option the user wants
            print("=" * 50)
            print("You have chosen to register a new user")
            print("Please enter the username and the password of the new user")

            # Requesting input from the user
            new_user = input("Enter the username of the new user : ")
            new_pass = input("Enter the password of the new password : ")
            
            # Declaring the variables for the function
            file_user = "user.txt"
            in_pass = False
            in_user = False

            # Calling the reg_user function 
            reg_user(new_user,new_pass,file_user,in_pass,in_user)

            # Displaying that the registeration is complete
            print("You have registered a new user")

            # requesting input from the user
            another = input("Would you like to input another user (Yes or No) : ").lower()

            if another == "yes":
               # If the user inputs "yes" then the process will repeat
               print("You have choosen to enter a another user")

            if another == "no":
               # else the user will go back to the menu and breaks the loop
               print("You have chosen to go back to the menu")
               break

         # This is if the user wants to add a new task to the task file
         elif option_int == "a":
              # declaring the variable for the function 
              file_task = "tasks.txt"

              # Telling the user want option they have selected
              print("The option you have chosen is to add a new task to the task text file.")
              print("=" * 50)  
              print("This option uses you to add the users name and other details to construct the complete task file.")   

              # Requesting inputs from the user
              task_user = input('Enter the name of the user who is going to do the task : ')
              title_task = input("Enter the title of the task : ")
              description_task = input("Enter the description of the task : ")
              print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
              issue_task = input("Enter the current date of the task bing issued  :")
              print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
              due_date_task = input("Enter the date the task is due : ")
              print("Please enter yes or no ")
              task_complete = input("Enter if the task is complete or not : ").lower()
              task_complete = "No"

              # Calling the add_task function
              add_task(task_user,title_task,description_task,issue_task,due_date_task,task_complete,file_task)

              # Requesting the input from the user
              another = input("Would you like to input another user (Yes or No) : ").lower()

              if another == "yes":
                 # If the user inputs "yes" then the process will repeat
                print("You have choosen to enter a another task")

              if another == "no":
                 # else the user will go back to the menu and breaks the loop
                 print("You have chosen to go back to the menu")
                 break
              

         # This is the option if the user wants to view will the task that have been recorded in the task text file
         elif option_int == "va":
            # Displaying what option the user has picked
            print("You have chosen to view of the available tasks ")
            print("=" * 50)

            # Displaying the title of the information being displayed
            print("Task information")
            print("=" * 50)

            # Declaring a variable for the function
            file_task = "tasks.txt"

            # Calling the view_all file
            view_all(file_task)

            # Requesting input from the user
            another = input("Would you like to go to the menu (Yes or No) : ").lower()

            if another == "yes":
              # If the user inputs "yes" the user will go back to the menu
              print("You have chosen to go back to the menu")
              break

            if another == "no":
              # if the user inputs "no" then the information will continue being displayed
              print("You have to continue viewing")

             
         # This is the view mine option this allows the user to view their personally task 
         elif option_int == "vm":
            # Display to the user what option they have requested
            print(f"You have chosen to view your personal tasks of {ent_user}")
            print("=" * 50)

            # Declaring a variable for the function
            file_task = "tasks.txt"

            # calling the view_mine function
            view_mine(ent_user,file_task)

            # Requesting input from the user
            another = input("Would you like to go to the menu (Yes or No) : ").lower()

            
            if another == "yes":
               # If the user inputs "yes" the user will go back to the menu
               print("You have chosen to go back to the menu")
               break
      
            if another == "no":
               # if the user inputs "no" then the information will continue being displayed
               print("You have to continue viewing")
               
               # Requests an input from the user again 
               another = input("Would you like to go to the menu (Yes or No) : ").lower()
               if another == "yes":
                  # if the user inputs "yes" 
                  # The program will break
                  break

            
         # This is generate option that allows the user to generate reports so the user may view the statistics of the business
         elif option_int == "gr":
            # Dsiplay what option the user has choosen
            print("You have chosen to generate reports")
            print("=" * 50)

            # Declaring variables for the function
            re_f_user = ""
            re_f_task = ""
            file_user = "user.txt"
            file_task = "tasks.txt"

            # Calling the gen_report function
            gen_report(re_f_task,re_f_user,file_task,file_user,month_dir)

            # Displaying a message to the user
            print("The reports are completed")

            # Requesting input from the user
            another = input("Would you like to go to the menu (Yes or No) : ").lower()

            if another == "yes":
              # If the user inputs "yes" the user will go back to the menu
              print("You have chosen to go back to the menu")
              break

         # This is the display the statistic function 
         # This allows the user to view all the statistics of the two file and uses the information from the gen_reports function to get the information
         elif option_int == "ds":
           # Displaying to the user what option they have picked
           print("You have chosen to see the statistics of the files ")
           print("=" * 50)
           print("\n")

           # Declaring variables for the function to user
           re_f_user = ""
           re_f_task = ""
           file_user = "user.txt"
           file_task = "tasks.txt"

           # Calling the display_statistics function
           display_statistic(re_f_task,re_f_user,file_task,file_user,month_dir)

           # Requesting input from the user 
           another = input("Would you like to go to the menu (Yes or No) : ").lower()

           if another == "yes":
               # If the user inputs "yes" the user will go back to the menu
               print("You have chosen to go back to the menu")
               break
      
           if another == "no":
               # if the user inputs "no" then the information will continue being displayed
               print("You have to continue viewing")
         else:
            # This breaks the while loop
            break
      else:
         # if the user input the incorrect values
         print("Please try entering an option again please ")

      # This option if the user wants to exit the program  
      if option_int == "e":
        print("You have chosen to exit the program")
        break
      
else:
   # Opening the file to find the other user trtying to login
   f_user = open("user.txt","r")

   for line in f_user :
      # for line in the text file f_user
      # Replace the "\n" with nothing
      # Split line by the commas
      line = line.replace(" ","")
      line = line.replace("\n","")
      line = line.split(",")
   
      if line[0] == ent_user and line[1] == ent_pass:
         # if the two inputs are found in the text file
         # Close the file 
         f_user.close()
   
         while True:
            # Use a while true to continue running until a break is found
            print(f"Welcome : {ent_user}")

            # Calling the user function
            user_menu() 

            # Requesting an input from the user
            option_int = input("Enter which option you would like to use : ").lower()

            while option_int == "a" or option_int == "vm" or option_int == "va" or option_int == "e":
               
               # While the inputs equal the following above 
               # This is used if the user does not input the correct the inputs

               # This is if the user wants to add a new task to the task file
               if option_int == "a":
                  # declaring the variable for the function 
                  file_task = "tasks.txt"

                  # Telling the user want option they have selected
                  print("The option you have chosen is to add a new task to the task text file.")
                  print("=" * 50)  
                  print("This option uses you to add the users name and other details to construct the complete task file.")   

                  # Requesting inputs from the user
                  task_user = input('Enter the name of the user who is going to do the task : ')
                  title_task = input("Enter the title of the task : ")
                  description_task = input("Enter the description of the task : ")
                  print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
                  issue_task = input("Enter the current date of the task bing issued  :")
                  print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
                  due_date_task = input("Enter the date the task is due : ")
                  print("Please enter yes or no ")
                  task_complete = input("Enter if the task is complete or not : ").lower()
                  task_complete = "No"

                  # Calling the add_task function
                  add_task(task_user,title_task,description_task,issue_task,due_date_task,task_complete,file_task)

                  # Requesting the input from the user
                  another = input("Would you like to input another user (Yes or No) : ").lower()

                  if another == "yes":
                     # If the user inputs "yes" then the process will repeat
                     print("You have choosen to enter a another task")

                  if another == "no":
                     # else the user will go back to the menu and breaks the loop
                     print("You have chosen to go back to the menu")
                     break

               # This is the option if the user wants to view will the task that have been recorded in the task text file
               elif option_int == "va":
                  # Displaying what option the user has picked
                  print("You have chosen to view of the available tasks ")
                  print("=" * 50)

                  # Displaying the title of the information being displayed
                  print("Task information")
                  print("=" * 50)

                  # Declaring a variable for the function
                  file_task = "tasks.txt"

                  # Calling the view_all file
                  view_all(file_task)

                  # Requesting input from the user
                  another = input("Would you like to go to the menu (Yes or No) : ").lower()

                  if another == "yes":
                     # If the user inputs "yes" the user will go back to the menu
                     print("You have chosen to go back to the menu")
                     break

                  if another == "no":
                     # if the user inputs "no" then the information will continue being displayed
                     print("You have to continue viewing")

   
               # This is the view mine option this allows the user to view their personally task 
               elif option_int == "vm":
                  # Display to the user what option they have requested
                  print(f"You have chosen to view your personal tasks of {ent_user}")
                  print("=" * 50)

                  # Declaring a variable for the function
                  file_task = "tasks.txt"

                  # calling the view_mine function
                  view_mine(ent_user,file_task)

                  # Requesting input from the user
                  another = input("Would you like to go to the menu (Yes or No) : ").lower()

                  
                  if another == "yes":
                     # If the user inputs "yes" the user will go back to the menu
                     print("You have chosen to go back to the menu")
                     break
            
                  if another == "no":
                     # if the user inputs "no" then the information will continue being displayed
                     print("You have to continue viewing")

                     # Requests an input from the user again 
                     another = input("Would you like to go to the menu (Yes or No) : ").lower()
                     
                     if another == "yes":
                        # if the user inputs "yes" 
                        # The program will break
                        break

               else:
                  # This breaks the while loop
                  break
            else:
               # if the user inputs the incorrect options
               print("Please enter the correct option")

         # If the user wants to exit the program
         if option_int == "e":
            # Displays the following message 
            # and breaks the program
           print("You have chosen to exit the program")
           break
   else:
     # If the user is not found the program will display the following message
     if line[0] != ent_user and line[1] != ent_pass:
         print('Username not found')
      
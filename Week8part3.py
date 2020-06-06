#Firstly, I am importing the tkinter package.
#It is required to create a GUI 
import tkinter
#Secondly, I am creating a class named "UpdateLabel".
#This class will contain the whole appliacation:
#attributes, functions etc.
class UpdateLabel():
    #Now, I am defining the class constructor method.
    #This method is automaticly invoked every time the UpdateLabel()
    #class object is created.
    def __init__(self):
        self.window = tkinter.Tk()#This command opens a new window
        #The following command sets the window title
        # to the "You can change the label too"
        self.window.title("You can change the label too")
        #The following line of code sets the window dimension
        self.window.geometry("320x120")

        #I am using a grid layout inside my window.
        #This kind of layout organizes widgets
        #in a table-like structure in the parent widget.
        #I am adding the text label widget to the window.
        self.aLabel = tkinter.Label(text = "Type some text here: ")
        #This label will display the text "Type some text here: ".
        self.aLabel.grid(row="0", column="0")
        #This label will be loacted in the row number 0 and
        #column number 0 of the grid layout.

        #The following two lines of code creates entry text field,
        #where the user can input some text to update the label
        self.UserEntry = tkinter.Entry(width="34")
        self.UserEntry.grid(row="0", column="1")
        #The width this field is 34.
        #In the next two lines of code I am defining the UpdateButton,
        #which once clicked changes the bLabel(not defined yet).
        self.UpdateButton = tkinter.Button(self.window, text = "UPDATE",
            activebackground="red", width=12, height=2,command =self.updateText)
        self.UpdateButton.grid(row="1",column="0")
        #On this button appears "UPDATE" word, when is clicked its colour
        #changes to red, it has width equal to 12 and height equal to 2.
        #When this button is clicked the updateText action is performed.
        #I attached this label to window in grid layout on position 1,0.

        #The following lines of code defines the next label. This label
        #named bLabel will be that one changed by the user's interaction
        #with the application via "UPDATE" button.
        self.bLabel = tkinter.Label(text="Change me...")
        self.bLabel.grid(row="1",column="1")
        #The text displayed via this label is "Change me...",
        #of course until the user press the "UPDATE"
        #This label is also attached to the grid layout.

        #The following command is used to draw the window and start
        #the application
        self.window.mainloop()
# The next step is to define the action that is performed onece "UPDATE"
#button is clicked.
    def updateText(self):
        #This function changes the text displayed on the label using
        #config method for the label. The get method is used to source the text
        #from the UserEntry filed. This value is assigned to the
        #text value of the bLabel.
        self.bLabel.config(text=self.UserEntry.get())
#main 
#The following comand creates an instance of the UpdateLabel class.
#This command can be removed from here and pasted to the Python shell
#with the same result.
s=UpdateLabel()
        
        
        
        
        

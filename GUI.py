#Jeffrey Almanzar
from tkinter import*
from Euler import Euler_CT
import tkinter.messagebox


class GUI:
    """top level class. Display all the widgets in the window."""
    
    def __init__(self,win):
        '''post: Creates all the frames '''
        self.Euler = Euler_CT()
        self.win = win
        self.top = Frame(self.win,width=950,height=30,bg='#0b4214')#top frame

        self.widgets =[] #will keep the widgets that I want to unplace later on 
        
        self.left = Frame(self.win,height=350,width=475,bg="white",bd=5)#left frame
        self.subleft= Frame(self.left, height =250, width =475,bg="white",bd=0)
        
        self.right = Frame(self.win,height=350,width=475,bg="white",bd=5)#right frame
        self.subright = Frame(self.right,height=335,width=475,bg="white",bd=0)
        
        self.bottom = Frame(self.win,height=140,width=950,bg="white",bd=5)#bottom frame
        self.subbottom=Frame(self.bottom,height=125,width=950,bg="white",bd=5)


    def create_win(self):
        '''post: modifies the window configuration'''
        self.win.configure(background='#0b4214') #change background
        self.win.title("Euler CT")#change title
        self.win.geometry("950x560")#set width and height

        #win's title
        title = Label(self.top,text ="Euler Circuit and Trail",relief=FLAT,font="Helvetica 16 bold",fg="white",bg='#0b4214')
        title.place(x=385)

        #right side
        right = Label(self.right, text = "Undireted Graph and Degrees:",bg='white',font="Arial 12 bold")
        right.place(x=15,y=10)

        #bottom
        result = Label(self.bottom, text = "Result:",bg='white',font="Arial 12 bold")
        result.place(x=15,y=10)

    def pack_frames(self):
        '''post: places all the frames in the window'''
        #Placing all frames in the window
        self.top.grid(row=0,column =0,pady=10,sticky="W",columnspan=2)
        self.left.grid(row=1,column=0,sticky="W")
        self.right.grid(row=1,column=1,sticky="W",padx=10)
        self.bottom.grid(row=2,column=0,pady=10,columnspan=2,sticky="W")
        self.subleft.place(x=0,y=125)
        self.subright.place(x=0,y=15)
        self.subbottom.place(x=0,y=11)
        
    def unpack_frame(self):
        """post: destroy all the widgets in self.widgest."""
        for i in self.widgets:
            i.destroy()
        
    def reset(self):
        """It will reset the program.
        post: clears the vertices and edges and displaces the right and bottom widgest."""
        reset = Button(self.right,width=10,text ="Reset",font="Helvetica 12 bold",fg='white',bg='#ed0000',bd=3)
        reset.place(x=320,y=300)
        reset.bind("<Button-1>",self.clear_frame)
        
    def clear_frame(self,event):
        """post: clear the vertices and edges and destroy all the widgets in self.widgest. """

        event.widget.place_forget()#unplace the reset button
        self.unpack_frame()#destroy all the widgets in self.widgest.

        #clearing the vertices and edges containers
        self.Euler.vertices.clear()
        self.Euler.edges.clear()
        
        self.input_source()#display input sources

    def clear_box(self,event):
        '''post: empties the textbox'''
        event.widget.delete(0,END)

    
    def display_info(self,vertices,edges):
        """pre: vertices and edges are created.
        post: displays vertices, edges, degree and result."""
        self.display_degree()
        self.display_vertex_edge(vertices,edges)
        self.results()
        
    def display_degree(self):
        """pre: vertices and edges are created.
        post: display the degree of each vertex."""
        degree = Label(self.subright,text="Degrees:",bg='white', font="Helvetica 11 bold")#Degrees label
        degree.place(x=15,y=100)
        p=120
        for i in self.Euler.vertices:#Degree of each vertex 
            n = self.Euler.get_degree(i)
            t = Label(self.subright,text="deg("+i+") ="+str(n),bg='white', font="Helvetica 10")
            t.place(x=20,y=p)
            p+=20
            self.widgets.append(t)
        #---------------------------------------------------------------------------------------------------------
        #appending the widgest to be destroyed later
        self.widgets.append(degree)
            
    def display_vertex_edge(self,vertices,edges):
        """pre: vertices and edges are created.
        post: display the vertices and edges in the window."""
        verts =Label(self.subright,text="Vertices: ",bg='white', font="Helvetica 11 bold")
        v = Label(self.subright,text=vertices,bg='white', font="Helvetica 10")
        
        edgs = Label(self.subright,text="Edges: ",bg='white', font="Helvetica 11 bold")
        ed = Label(self.subright,text =edges,bg='white', font="Helvetica 10")
        #placing then in the screen
        verts.place(x=15,y=40)
        v.place(x=85,y=40)
        edgs.place(x=15, y = 70)
        ed.place(x =70,y=70)
        #---------------------------------------------------------------------------------------------------------
        #appending the widgest to be destroyed later
        self.widgets.append(verts)
        self.widgets.append(v)
        self.widgets.append(edgs)
        self.widgets.append(ed)

    def results(self):
        """pre: vertices and edges are created and the decree of each vertex is known.
        post: display wheter the graph has an Euler circui or trail or neither"""
        first = Label(self.subbottom,text="Assuming the graph is undirected and connected:",bg='white', font="Helvetica 10 bold")
        first.place(x=15,y=20)

        trail = self.Euler.has_trail()
        circuit = self.Euler.has_circuit()

        t = "*The graph has an Euler trail.There are only 2 vertices with odd degree."
        c = "*The graph has an Euler circuit.All the verices have even degree."
        nt = "*The graph does not have an Euler trail. Must be only two vertices with odd degree."
        nc="*The graph does not have an Euler circuit. All the vertices must have even degree."
        
        if trail ==True:#has an Euler trail
            has_trail = Label(self.subbottom, text = t,bg='white', font="Helvetica 10",fg="#08631c")
            has_circuit =Label(self.subbottom, text=nc,bg='white', font="Helvetica 10",fg="#ed0000")#red
        elif circuit==True:#has an Euler circuit
            has_trail = Label(self.subbottom, text = nt,bg='white', font="Helvetica 10",fg="#ed0000")#red
            has_circuit =Label(self.subbottom, text=c,bg='white', font="Helvetica 10",fg="#08631c")
        else:#neither
            has_trail = Label(self.subbottom, text = nt,bg='white', font="Helvetica 10",fg="#ed0000")
            has_circuit =Label(self.subbottom, text=nc,bg='white', font="Helvetica 10",fg="#ed0000")
            
        #placing the result in the window   
        has_trail.place(x=30,y=40)
        has_circuit.place(x=30,y=60)
        #---------------------------------------------------------------------------------------------------------
        #appending the widgest to be destroyed later
        self.widgets.append(first)
        self.widgets.append(has_trail)
        self.widgets.append(has_circuit)          
        
    def get_graph(self,vertices,edges):
        """pre: vertices and edges are lists of strings 
        post: creates all the vertices and edges."""
        self.disable_submit(self.submit)
        if len(vertices)>0 and len(edges)>0:
            try:
                self.get_vert_ed(vertices,edges)
                self.display_info(vertices,edges)
                self.reset()
            except IndexError:
                tkinter.messagebox.showerror("Type Error",'Type as suggested, try again')#message
                self.disable.place_forget()#unpack the submit button
                self.Euler.vertices.clear()
                self.Euler.edges.clear()
                self.get_input_from_keyboard()
        else:
            tkinter.messagebox.showerror("Missing vertices or edges","Expecting one or more vertices/edges.")#message 
            self.disable.place_forget()
            self.get_input_from_keyboard()

    def get_vert_ed(self,vertices,edges):
        """post: creates all the vertices and edges."""
        for v in vertices:
            if v.isalpha() or v.isdigit():
                self.Euler.create_vertex(v)
        for e in edges.split():
            self.Euler.create_edge(e[1],e[3])
    
    def input_source(self):
        """post:display the input sources in the window and
        binds the widgets for the calling of specific methods if specific events occurs."""
        indicator = Label(self.left,text="Please provide the graph:",bg='white',font="Arial 12 bold")
        indicator.place(x=15,y=15)
                            
        self.v = IntVar()
        self.v.set(0)
        source = Label(self.left,text="Input Source:",bg="white",font="Arial 11 bold") 
        keyboard = Radiobutton(self.left,text="Keyboard",bg="white",variable=self.v,value=1,font=("Arial",10),selectcolor="#e8ffeb")
        file = Radiobutton(self.left,text="file",bg="white",variable=self.v,value=2,font=("Arial",10),selectcolor="#e8ffeb")

        keyboard.bind("<Button-1>",self.from_keyboard)
        file.bind("<Button-1>",self.from_file)

        #placing the widgets in the window
        source.place(x=15,y=50)
        keyboard.place(x=30,y=80)
        file.place(x=30,y=100)

    def get_input_from_file(self):
        """post: gets file name."""
        file = Label(self.subleft,text="File Name: ",bg='white',font=("Arial",12))
        box = Entry(self.subleft,width=35,bg='#e8ffeb')
        box.insert(0,'Ex: graph.txt')
        box.bind("<Button-1>",self.clear_box)#will clear the text box when clicked

        self.submit2 = Button(self.subleft,width=15,text ="Submit",font="Helvetica 12 bold",fg='white',bg='#0b4214',bd=3)
        self.submit2.bind("<Button-1>",lambda e: self._help_input_file(box.get()))
        #placing widgets in the window
        file.place(x=15,y=20)
        box.place(x=100,y=20)
        self.submit2.place(x=100,y=55)

        #---------------------------------------------------------------------------------------------------------
        #appending the widgest to be destroyed later
        self.widgets.append(file)
        self.widgets.append(box)
        self.widgets.append(self.submit2)
        
    def _help_input_file(self,file):
        """post: gets the vertices and edges from the file"""
        self.disable_submit(self.submit2)#disable the submit buttom
        try:
            vertices,edges = self.Euler.get_file_info(file)
            self.display_info(vertices,edges)
            self.reset()
        except FileNotFoundError: # if file not found
            tkinter.messagebox.showerror("File Error",'Check file name and try again')#message
            self.disable.place_forget()#unpack the submit button
            self.get_input_from_file() #get the file's name again
               
    def get_input_from_keyboard(self):
        '''post: gets vertices and edges from the user.'''

        #Vertex prompt
        vertex = Label(self.subleft,text="Vertex: ",bg='white',font=("Arial",12))
        box = Entry(self.subleft,width=35,bg='#e8ffeb')
        box.insert(0,'Ex: a,b,c,d,...')
        box.bind("<Button-1>",self.clear_box)#will clear the text box when clicked
        
        #edges prompt
        edges= Label(self.subleft,text="Edges: ",bg='white',font=("Arial",12))
        box2 = Entry(self.subleft,width=35,bg='#e8ffeb')
        box2.insert(0,'Ex: (a,b) (a,d) (b,c) ...space in btw')
        box2.bind("<Button-1>",self.clear_box) #will clear the text box when clicked

        #submit button
        self.submit = Button(self.subleft,width=15,text ="Submit",font="Helvetica 12 bold",fg='white',bg='#0b4214',bd=3)
        self.submit.bind("<Button-1>",lambda e: self.get_graph(box.get(),box2.get()))
        
        #Placing every widget in the window
        vertex.place(x=15,y=20)
        box.place(x=75,y=20)
        edges.place(x=15,y=55)
        box2.place(x=75,y=55)
        self.submit.place(x=75,y=90)
        #---------------------------------------------------------------------------------------------------------
        #appending the widgest to be destroyed later
        self.widgets.append(vertex)
        self.widgets.append(box)
        self.widgets.append(box2)
        self.widgets.append(edges)
        self.widgets.append(self.submit)
            
    def disable_submit(self,butoon):
        """post: unplace the submit bottom and place a Label in his place."""
        butoon.place_forget()
        self.disable = Label(self.left,height=2,width=15,text ="Submit",font="Helvetica 12 bold",fg='white',bg='#628c74',bd=1,relief=FLAT)
        self.disable.place(x=75,y=250)
        self.widgets.append(self.disable)

    def from_file(self,event):
        """post: destroy the widgets in self.widgets if any is in there, clears vertices and edges and display the widgets to get
        the vertices and edges from the user."""
        if len(self.widgets)>0:
            self.unpack_frame()
            self.Euler.vertices.clear()
            self.Euler.edges.clear()
        self.get_input_from_file()

    def from_keyboard(self,event):
        """post: destroy the widgets in self.widgets if any is in there, clears vertices and edges and display the widgets to get
        the file name from the user."""
        if len(self.widgets)>0:# if it is some
            self.unpack_frame()
            self.Euler.vertices.clear()
            self.Euler.edges.clear()
        self.get_input_from_keyboard()
        
        
    def main(self):
        '''controls the whole app.
        post: it modyfies the windows, place the frames in the screen and display the input sources'''
        self.create_win() #modify the window
        self.pack_frames()#place all frame in the screen
        self.input_source()# gets input source
        
        
        



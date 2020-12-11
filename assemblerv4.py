from sys import argv



      
    
class Parser():
    def __init__(self, assemb_file):
        self.assemb_file=assemb_file
        # command_instruction
         
        # line = assemb_file.readline()
        # print(line[0])
        
        # while line:            
            # print(line.strip())
            # line=assemb_file.readline()   
    
           
    def hasMoreCommands(self,line): #are there more commands in the input?, returns boolean
        if (line[0] != '/') and (line != "\n"):
            return True
        else: return False
        
        
        # if (line[0] != '/') and (not(line[0].isspace())):
            # return True
        # else: return False
            
        
        
    
    def advance(self): #goes to next line and makes it the current command, only call if hasmoreCommands=1
        line = self.assemb_file.readline()
        return(line)
        # if(self.hasMoreCommands(line)):
            # return(line)
        
        
        
        # Bincode=""
        
        # while line:
            # if(self.hasMoreCommands(line)):
                # # print("real line")    
                # # self.commandType(line)
                # # self.symbol(line)
                # if(self.commandType(line)=="A"):
                    
                # if(self.commandType(line)=="C"):
                    # print(self.jump(line))
                # line=self.assemb_file.readline()
                
            # else: 
                # # print("no")
                # line=self.assemb_file.readline()
    
    
    def commandType(self,line): #returns A_command (for @xxx is a symbol or #), C_command for dest=comp;jump; L_command for ( (xxx) symbol)
        # print(line,end='')
        #print(line)
        if(line[0]=='@'):
            return("A")
        elif(line[0]=='('):
            return("L")
        else: return("C")
        
    
    def symbol(self,line): #returns string; returns symbol or decimal xxx or the current command @xxx or (xxx); called when comm() is A or L command
        if(self.commandType(line)=="A"):
            return(line[1:])
        # if(self.commandType(line)=="L"):
    
   
    
    def dest(self,line): #returns dest mnemonic in current C-command when commandtype() is C_command; returns string
        dest_command=line.split('=')[0]
        
        if(dest_command=="M"):
            return("001")
        elif(dest_command=="D"):
            return("010")
        elif(dest_command=="MD"):
            return("011")
        elif(dest_command=="A"):
            return("100")
        elif(dest_command=="AM"):
            return("101")
        elif(dest_command=="AD"):
            return("110")
        elif(dest_command=="AMD"):
            return("111")
        else: return("000")
        
   
    
    def comp(self,line): #returns comp mnemonic in current C-command when commandtype() is C_command; returns string
        # print(line)
        comp_command=line.split('=')[1].rstrip('\n')
        # print(comp_command)
        # print(str(comp_command)=='A')
        # print(type(comp_command))
        # print(type("A"))
        
        if(comp_command=="0"):
            return("0101010")
        elif(comp_command=="1"):
            return("0111111")
        elif(comp_command=="-1"):
            return("0111010")
        elif(comp_command=="D"):
            return("0001100")
        elif(comp_command=="A"):
            return("0110000")
        elif(comp_command=="M"):
            return("1110000")           
        elif(comp_command=="!D"):
            return("0001101")
        elif(comp_command=="!A"):
            return("0110001")
        elif(comp_command=="!M"):
            return("1110001")            
        elif(comp_command=="-D"):
            return("0001111")
        elif(comp_command=="-A"):
            return("0110011")
        elif(comp_command=="-M"):
            return("1110011")           
            
        elif(comp_command=="D+1"):
            return("0011111")
            
        elif(comp_command=="A+1"):
            return("0110111")
        elif(comp_command=="M+1"):
            return("1110111")
            
        elif(comp_command=="D-1"):
            return("0001110")
            
        
        elif(comp_command=="A-1"):
            return("0110010")
        elif(comp_command=="M-1"):
            return("1110010")
            
            
        elif(comp_command=="D+A"):
            return("0000010")
        elif(comp_command=="D+M"):
            return("1000010")
            
            
        elif(comp_command=="D-A"):
            return("0010011")
        elif(comp_command=="D-M"):
            return("1010011")
            
            
        elif(comp_command=="A-D"):
            return("0000111")
        elif(comp_command=="M-D"):
            return("1000111")
            
        elif(comp_command=="D&A"):
            return("0000000")
        elif(comp_command=="D&M"):
            return("1000000")
            
            
        
        elif(comp_command=="D|A"):
            return("0010101")
        elif(comp_command=="D|M"):
            return("1010101")
            
        else: return("error")
    
    
    def jump(self,line): #returns jump mnemonic in current C-command when commandtype() is C_command; returns string
        
        jump_command=""
        
        if ';' in line:
            jump_command=line.split(';')[1] #.rstrip('\n')
            jump_command=jump_command[0:3]
            #print(jump_command)            
            
            if(jump_command=="JGT"):
                return("001")
            elif(jump_command=="JEQ"):
                return("010")
            elif(jump_command=="JGE"):
                return("011")
            elif(jump_command=="JLT"):
                return("100")
            elif(jump_command=="JNE"):
                return("101")
            elif(jump_command=="JLE"):
                return("110")
            elif(jump_command=="JMP"):
                return("111")
            else: return("000")
        else: return("000")
              


class SymbolTable():
    def __init__(self): #creates new symbol table
        self.Table={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,"SCREEN":16384,"KBD":24576}
        
    
    
    def addEntry(self, symbol, address): #adds the pair to table
        self.Table[symbol]=address
        print(self.Table)
        
    def Contains(self, symbol): # returns boolean - for whether table contains the symbol
        if symbol in self.Table:
            return True
        else: return False
    
    def GetAddress(self, symbol): # returns address associated w/ symbol
        return(self.Table(symbol))
    
    
    
    
def Main():
    # print("test")
    #assemb_file = file.read()
    
    with open(argv[1],"r") as readfile: #move to parser function
        A = Parser(readfile)
        writefilename = str(argv[1])[:-4]+".hack"
        open(writefilename,"w")
        line_number=0 #should start at 1?
        
        Symbols=SymbolTable()
        for line in readfile:
            if(A.hasMoreCommands(line)):
                stripped_line = line.strip()
                #print(stripped_line)
                #A.commandType(stripped_line)
                if(A.commandType(stripped_line) =="A") or (A.commandType(stripped_line) =="C"):
                    # print("test")
                    line_number+=1
                    #print(stripped_line)
                if(stripped_line[0]=="("): #change to "("
                    print("test")
                    Symbols.addEntry(stripped_line[1:-1],line_number)
            
            
        
        
        # for line in readfile:
            # if(A.hasMoreCommands(line)):                
                # command_instruction=A.commandType(line)
                
                # if (command_instruction=="A"):              
                    # print(format(int(A.symbol(line)),'016b'),file=open(writefilename,"a"))
                # elif (command_instruction=="C"):
                    # dest_code=A.dest(line)
                    # comp_code=A.comp(line)
                    # jump_code=A.jump(line)                    
                    # c_code="111"+comp_code+dest_code+jump_code
                    # print(c_code)
                    # print(c_code,file=open(writefilename,"a"))
            
      


Main()
            
  
    
    
    
    
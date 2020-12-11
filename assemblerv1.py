from sys import argv



      
    
class Parser():
    def __init__(self, assemb_file):
        self.assemb_file=assemb_file         
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
        
        while line:
            if(self.hasMoreCommands(line)):
                # print("real line")
                # self.commandType(line)
                # self.symbol(line)
                if(self.commandType(line)=="C"):
                    print(self.jump(line))
                line=self.assemb_file.readline()
                
            else: 
                # print("no")
                line=self.assemb_file.readline()
    
    
    def commandType(self,line): #returns A_command (for @xxx is a symbol or #), C_command for dest=comp;jump; L_command for ( (xxx) symbol)
        # print(line,end='')
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
            return("101010")
        elif(comp_command=="1"):
            return("111111")
        elif(comp_command=="-1"):
            return("111010")
        elif(comp_command=="D"):
            return("001100")
        elif(comp_command=="A") or (comp_command=="M"):
            return("110000")
        elif(comp_command=="!D"):
            return("001101")
        elif(comp_command=="!A") or (comp_command=="!M"):
            return("110001")
        elif(comp_command=="-D"):
            return("001111")
        elif(comp_command=="-A") or (comp_command=="-M"):
            return("110011")
        elif(comp_command=="D+1"):
            return("011111")
        elif(comp_command=="A+1") or (comp_command=="M+1"):
            return("110111")
        elif(comp_command=="D-1"):
            return("001110")
        elif(comp_command=="A-1") or (comp_command=="M-1"):
            return("110010")
        elif(comp_command=="D+A") or (comp_command=="D+M"):
            return("000010")
        elif(comp_command=="D-A") or (comp_command=="D-M"):
            return("010011")
        elif(comp_command=="A-D") or (comp_command=="M-D"):
            return("000111")
        elif(comp_command=="D&A") or (comp_command=="D&M"):
            return("000000")
        elif(comp_command=="D|A") or (comp_command=="D|M"):
            return("010101")
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
        else: return("")
              
        
    
    

class Code():
  def __init__(self):
  
  def dest(self, dest_code): # returns 3 bits - binary code of dest_code
  
  def comp(self, comp_code): # returns 7 bits - binary code of comp_code
  
  def jump(self, jump_code): # returns 3 bits - binary code of jump_code
    

# class SymbolTable():
#     def __init__(self): #creates new symbol table
    
#     def addEntry(self, symbol, address): #adds the pair to table
    
#     def Contains(self, symbol): # returns boolean - for whether table contains the symbol
    
#     def GetAddress(self, symbol): # returns address associated w/ symbol 
    
    
    
    
def Main():
    # print("test")
    #assemb_file = file.read()
    
    with open(argv[1],"r") as file: #move to parser function
        A = Parser(file)
        A.advance()
    
    
    
        


Main()
            
  
    
    
    
    
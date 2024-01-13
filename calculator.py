# packages import
import  math
from tkinter import *
import numpy as np
# creating a method to display additions and substractions 
def add_or_substract(a,b,operation_symbol=None):# a and modification for decimal operations
    # a and modification for decimal operations
    a_original=a
    a_str=str(a_original).replace(".",",")
    a=int(str(a).replace(".",""))
    b_original=b
    b_str=str(b_original).replace(".",",")
    b=int(str(b).replace(".",""))
    a_str=a_str[::-1]
    b_str=b_str[::-1]
    # condition for the operation
    result=0
    if operation_symbol=="-":
        result=a_original-b_original
        a_str=a_str[::-1]
        b_str=b_str[::-1]
    elif operation_symbol=="+":
        result=a_original+b_original
    elif operation_symbol=="×":
        result=a_original*b_original
    # getting the operation deductions
    deductions=[]
    for i in range((len(str(a))+len(str(b)))//2):
        if (i<len(a_str) and i<len(b_str)):
            if a_str[i]!="," and b_str[i]!=",":
                deductions.append(eval(str(a_str[i])+(operation_symbol if operation_symbol!="×" else "*")+str(b_str[i]))//10)
                # substractions deductions system
                if operation_symbol=="-":
                    if int(b_str[i])<int(a_str[i]):
                        deductions.append(abs((int(b_str[i])+10)//10))
    # the invertion of the string of the factor is not nessesary for the substraction because the deductions computing system don't need it
    if operation_symbol!="-":
        a_str=a_str[::-1]
        b_str=b_str[::-1]
    # creating the code to display the deductions
    deductions_displaying_code=chr(10)+"result_canvas.create_text(xb+20,yb+8,text=\'"   +("  ".join(list(map(str,deductions))).replace("0","  "))+"\',fill=\'gray\',font=(\'Arial\',10))"
    # result transformation for decimal operations
    result_str=str(result).replace(".",",")
    # posed operation displaying code returning
    return """
xb=int(result_canvas['width'])//2
yb=int(result_canvas['height'])//2
result_canvas.create_text(xb+20,yb+20,text=\'"""+a_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_text(xb+20+"""+str((len(str(int(a)))-len(str(int(b))))*9 if len(str(int(b)))!=len(str(int(a))) else 0)+""",yb+40,text=\'"""+b_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_text(xb-"""+str(len(str(b))*20)+""",yb+40,text=\'"""+str(operation_symbol)+"""\',fill=\'gray\',font=(\'Arial\',10))
result_canvas.create_line(xb-30,yb+47,xb+70,yb+47,fill=\'gray\')
result_canvas.create_text(xb+20,yb+50,text=\'"""+str(result_str)+"""\',font=(\'Arial\',20),fill=\'gray\')
    """+deductions_displaying_code
def multiply(a,b):
    # condition for the code to display the posed multiplication
    if len(str(b))==1:
        return add_or_substract(a,b,operation_symbol="×")
    else:
        # a and modification for decimal operations
        a_original=a
        a_str=str(a_original).replace(".",",")
        a=int(str(a).replace(".",""))
        b_original=b
        b_str=str(b_original).replace(".",",")
        b=int(str(b).replace(".",""))
        # result storing for numbers positions,displaying,etc...
        result=a_original*b_original
        result_str=str(result).replace(".",",")
        # operation computing
        base_posed_operation="""
xb=int(result_canvas['width'])//2
yb=int(result_canvas['height'])//2
result_canvas.create_text(xb+20,yb+20,text=\'"""+a_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_text(xb+20,yb+40,text=\'"""+b_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_text(xb-20,yb+40,text=\'×\',fill=\'gray\',font=(\'Arial\',10))
result_canvas.create_line(xb-30,yb+47,xb+37,yb+47,fill=\'gray\')
result_canvas.create_text(xb+20,yb+60,text=\'"""+str(a*int(str(b)[::-1][0]))+"""\',font=(\'Arial\',20),fill=\'gray\')
"""
        code_end="""
result_canvas.create_text(xb+20,yb+10+"""+str(len(str(b))*50)+""",text=\'"""+str(result_str)+"""\',font=(\'Arial\',20),fill=\'gray\')
result_canvas.create_text(xb-"""+str(len(str(a*int(str(b)[0]))))+""",yb+60,text=\'+\',fill=\'gray\',font=(\'Arial\',10))
result_canvas.create_line(xb-50*"""+str(len(str(b))+len(str(a*int(len(str(b)[len(str(b))-1])))))+""",yb+"""+str(len(str(b))*50)+""",xb+"""+str(len(str(b))*50)+""",yb+"""+str((len(str(b)))*50)+""",fill=\'gray\')
"""
        code_adding=""
        zeros="0"
        addition_terms=[str(a*int(str(b)[0])+pow(len(str(b)),10))]
        for i in reversed(range(1,len(str(b)))):
            text=str(a*int(str(b)[i]))+zeros
            addition_terms.append(text)
            code_adding+="result_canvas.create_text(xb-"+str(len(str(a*int(str(b)[i]))))+",yb+40+"+str(len(str(b))*20)+",text=\'+\',fill=\'gray\',font=(\'Arial\',10))\nresult_canvas.create_text(xb+20,yb+20+"+str(i*20+40)+",text=\'"+text+"\',fill=\'gray\',font=(\'Arial\',20))\n"
            zeros+="0"
        # getting the operation deductions
        # function to calculate the deductions of an addition
        def get_deduction(*kwargs):
            return sum(map(int,kwargs))//10
        # deductions computing
        deductions=list(map(get_deduction,*list(map(list,addition_terms))))
        # creating the code to display the deductions
        deductions_displaying_code=chr(10)+"result_canvas.create_text(xb+10,yb+48,text=\'"+("  ".join(list(map(str,deductions))).replace("0",""))+"\',fill=\'gray\',font=(\'Arial\',10))"
        # code returning
        return base_posed_operation+code_adding+deductions_displaying_code+code_end
def divide(a,b):
    # a and modification for decimal operations
    a_original=a
    a_str=str(a_original).replace(".",",")
    a=int(str(a).replace(".",""))
    b_original=b
    b_str=str(b_original).replace(".",",")
    b=int(str(b).replace(".",""))
    # result and modulo result storing for numbers positions,displaying,etc...
    result=a/b
    result_str=str(result).replace(".",",")
    modulo_result=a%b
    modulo_result_str=str(result).replace(".",",")
    # displaying code start
    displaying_code_start="""
xb=int(result_canvas['width'])//2
yb=int(result_canvas['height'])//2
result_canvas.create_text(xb+4,yb,text=\'"""+b_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_line(xb-10,yb+10,xb+40,yb+10,fill=\'gray\')
result_canvas.create_line(xb-10,yb-10,xb-10,yb+70,fill=\'gray\')
result_canvas.create_text(xb-80,yb,text=\'"""+a_str+"""\',fill=\'gray\',font=(\'Arial\',20))
result_canvas.create_text(xb+4,yb+20,text=\'"""+result_str+"""\',fill=\'gray\',font=(\'Arial\',20))

"""
    # doing operation
    displaying_code_adding=""
    last_modulo_result_str=""
    a_str=a_str.replace(",","")
    for i in range(len(a_str)):
        # setting the value of __a__ to it value at the beigining of the operation if the frist didgit of a is less than b else return it value like in the reest of the operation
        if i>0:
            __a__=int(last_modulo_result_str+a_str[i])
        else:
            __a__=0
            i=0
            while __a__<b:
                __a__=int(a_str.replace(",","")[:(i+1)])
                i+=1
        __b__=(__a__//b)* b
        last_modulo_result_str=str(__a__-__b__)
        displaying_code_adding+=add_or_substract(__a__,__b__,operation_symbol="-").replace("xb=int(result_canvas['width'])//2"+chr(10)+"yb=int(result_canvas['height'])//2","xb=xb+"+str(len(str(__a__))*20)+chr(10)+"yb=yb+40"+chr(10))
    # displaying code returning
    return displaying_code_start+"xb-=147;yb-=45;"+displaying_code_adding
def square(a):
    return multiply(a,a)
def cube(a):
    # doing square to start
    code_start=square(a)
    # after, doing multiplication of the square reesult and the parameter
    code_end=multiply(a*a,a)
    base_x_coordinate_old_declaration="""
xb=int(result_canvas['width'])//2
"""
    base_x_coordinate_new_declaration="""
xb=int(result_canvas['width'])//4*3
"""
    code_end=code_end.replace(base_x_coordinate_old_declaration,base_x_coordinate_new_declaration)
    # after, retrn the code
    return code_start+code_end
def get_constant(name):
    code_start="""xb=int(result_canvas['width'])//2
yb=int(result_canvas['height'])//2
"""
    if name=="phi":
        return code_start+"result_canvas.create_text(xb-50,yb,text=\'φ≈1.61803398875\',fill=\'gray\',font=(\'Arial\',20))"
    else:
        symbol=""
        if name=="pi":
            symbol="𝜋"
        else:
            symbol=name
        return code_start+"result_canvas.create_text(xb-50,yb,text=\'"+str(symbol)+"≈"+str(eval("math."+str(name))).replace(".",",")+"\',fill=\'gray\',font=(\'Arial\',20))"
def use_methematical_function(function_name,params):
    result_str=str(eval("math."+function_name+"("+",".join(list(map(str,params)))+")")).replace(".",",")
    function_params_names_str=",".join(list(map(str,params)))
    return """xb=int(result_canvas['width'])//2
yb=int(result_canvas['height'])//2
result_canvas.create_text(xb-50,yb,text=\'"""+function_name+"""("""+function_params_names_str.replace(".",",")+""")="""+result_str+"""\',fill=\'gray\',font=(\'Arial\',20))
"""
# operation function researshing function
def do(query="addition(+ or ∑)",inputs=[]):
    #  base operation researtch dict
    base_operation_research_dict={
        "addition(+ or ∑)":{
            "function name":"add_or_substract",
            "keywords options":"operation_symbol='+'"
        },
        "substraction(-)":{
            "function name":"add_or_substract",
            "keywords options":"operation_symbol='-'"
        },
        "multiplication(×)":{
            "function name":"multiply",
            "keywords options":""
        },
        "division(÷)":{
            "function name":"divide",
            "keywords options":""
        },
        "square(√)":{
            "function name":"square",
            "keywords options":""
        },
        "cube(³)":{
            "function name":"cube",
            "keywords options":""
        }
    }
    # operation code creating
    if "getting" in query:
        return eval("get_constant('"+(query.replace(" getting","").replace("(φ or ϕ)","").replace("(∏)",""))+"')")
    elif query in base_operation_research_dict.keys():
        base_operation_dict=base_operation_research_dict[query]
        if base_operation_dict["keywords options"]!="":
            last_parameter_code=","+base_operation_dict["keywords options"]
        else:
            last_parameter_code=""
        return eval(base_operation_dict["function name"]+"("+(",".join(list(map(str,inputs))))+last_parameter_code+")")
    else:
        query=query.replace("(e)","").replace("onential","").replace("(f∑)","").replace("(lde)","").replace("(permutation)","").replace("(fre)","").replace("(y)","").replace("(ly)","")
        return eval("use_methematical_function('"+query+"',"+str(inputs)+")")
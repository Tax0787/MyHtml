#Cython : cdef str source
source = '<!DOCTYPE html>'
def tag(name : str, sourse : str, close = True, **attrebute):
    assert isinstance(close, bool), "TypeError : close tag bool must be bool"
    #Cython : cdef str return
    #Cython : cdef str end
    #Cython : cdef str option
    option=''
    if attrebute:
        for key, value in attrebute.items(): #make attrebute 4 for roop
            option+=f' {key} = "{value}"'
    if close:
        end = f'{sourse}</{name}>' #make both close and sourse(C-Data)
    else:
        end = '' #Don't close
    returns = f'<{name}{option}>{end}' #return tags
    return returns
def web(head_data, body_data, lang = None, id = None, **attrebute): #head_data, body_data 각각 맞는 입력값 만들기
    assert lang == None or isinstance(lang, str), "TypeError : Web page language must be None or string data"
    assert lang == None or isinstance(id, str), "TypeError : html tag's id must be None(Undefined) or string data"
    #Cython : cdef str sourse
    #Cython : cdef dict option
    #Cython : cdef str sourse
    option = attrebute #make local var 2 copying attrebute
    if lang != None:
        option.update({'lang':lang}) #Web page Langauge ㅇOption
    if lang != None:
        option.update({'id':id}) #html tag id define
    sourse='<h1> Error : 503 </h1>'
    tag('html',sourse,**attrebute)
#def 작성중...
pass #Thinking...
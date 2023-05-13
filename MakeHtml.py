#Cython : cdef str source
source = '<!DOCTYPE html>'

def tag(name : str, sourse : str, close = True, **attrebute):
    '''
    html tag editing
    '''
    assert isinstance(close, bool), "TypeError : close tag bool must be bool"
    #Cython : cdef str returns
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

def head(meta_data : tuple, encoding = 'UTF-8', id = None, style = None, title = None, script = None, link = None, **attrebute):
    '''
    make head part of html DOCS
    '''
    assert encoding == None or isinstance(encoding, str), "TypeError : Web page encoding must be None or string data"
    assert id == None or isinstance(id, str), "TypeError : Web page encoding must be None or string data"
    assert style == None or isinstance(style, str), "TypeError : Web page encoding must be None or string data"
    assert title == None or isinstance(title, str), "TypeError : Web page encoding must be None or string data"
    assert script == None or isinstance(script, str), "TypeError : Web page encoding must be None or string data"
    assert link == None or isinstance(link, str), "TypeError : Web page encoding must be None or string data"
    assert isinstance(meta_data[0], str) or isinstance(meta_data[1], str), "TypeError : meta data start 2 end"
    #Cython : cdef dict option
    #Cython : cdef str sourse
    sourse = meta_data[0]
    option = attrebute #make local var 2 copying attrebute
    if id != None:
        option.update({'id':id}) #html tag id define
    if encoding != None:
        sourse += tag('meta', '', close = False, charset = encoding) #setting web encoding
    if link != None:
        sourse += tag('link', link) #linking
    if title != None:
        sourse += tag('title', title) #title
    if style != None:
        sourse += tag('style', style) #make CSS 4 style
    if script != None:
        sourse += tag('script', script) #make JS 2 script
    sourse += meta_data[1]
    returns = tag('head',sourse,**option)
    return returns

def body(meta_data : tuple, encoding = 'UTF-8', id = None, style = None, title = None, script = None, link = None, **attrebute):
    '''
    make head part of html DOCS
    '''
    assert encoding == None or isinstance(encoding, str), "TypeError : Web page encoding must be None or string data"
    assert id == None or isinstance(id, str), "TypeError : Web page encoding must be None or string data"
    assert style == None or isinstance(style, str), "TypeError : Web page encoding must be None or string data"
    assert title == None or isinstance(title, str), "TypeError : Web page encoding must be None or string data"
    assert script == None or isinstance(script, str), "TypeError : Web page encoding must be None or string data"
    assert link == None or isinstance(link, str), "TypeError : Web page encoding must be None or string data"
    assert isinstance(meta_data[0], str) or isinstance(meta_data[1], str), "TypeError : meta data start 2 end"
    #Cython : cdef dict option
    #Cython : cdef str sourse
    sourse = meta_data[0]
    option = attrebute #make local var 2 copying attrebute
    if id != None:
        option.update({'id':id}) #html tag id define
    if encoding != None:
        sourse += tag('meta', '', close = False, charset = encoding) #setting web encoding
    if link != None:
        sourse += tag('link', link) #linking
    if title != None:
        sourse += tag('title', title) #title
    if style != None:
        sourse += tag('style', style) #make CSS 4 style
    if script != None:
        sourse += tag('script', script) #make JS 2 script
    sourse += meta_data[1]
    returns = tag('head',sourse,**option)
    return returns

def web(head_data:str, body_data:str, lang = None, id = None, **attrebute): #head_data, body_data 각각 맞는 입력값 만들기
    '''
    make web site by form
    '''
    assert lang == None or isinstance(lang, str), "TypeError : Web page language must be None or string data"
    assert id == None or isinstance(id, str), "TypeError : html tag's id must be None(Undefined) or string data"
    #Cython : cdef str returns
    #Cython : cdef str sourse
    #Cython : cdef dict option
    option = attrebute #make local var 2 copying attrebute
    if lang != None:
        option.update({'lang':lang}) #Web page Langauge Option
    if id != None:
        option.update({'id':id}) #html tag id define
    sourse=head_data+body_data
    returns = tag('html',sourse,**option)
    return returns

def HTML(head_data:str, body_data:str, lang = None, id = None, **attrebute):
    #Cython : cdef str docs
    docs = source + '\n' + web(head_data, body_data, lang = lang, id = id, **attrebute)
    return docs

def test():
    #lol it will work
    #Cython : cdef str data
    data=HTML(head(('', ''), title='test page'),'<h1>test</h1>',lang='en')
    print(data)
    with open('index.html','w') as f:
        f.write(data)

def main():
    test()

if __name__ == "__main__":main()

pass #Thinking...
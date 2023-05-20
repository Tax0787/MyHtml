#Cython : cdef str source
source = '<!DOCTYPE html>'

def tag(name : str, sourse : str, close = True, self_closing = False, **attrebute):
    '''
    html tag editing

    if raised error, input anything in *NoError
    '''
    assert isinstance(close, bool), "TypeError : close tag bool must be bool"
    assert isinstance(self_closing, bool), "TypeError : self_closing bool must be bool"
    #Cython : cdef str returns
    #Cython : cdef str end
    #Cython : cdef str option
    option=''
    if attrebute:
        for key, value in attrebute.items(): #make attrebute 4 for roop
            option += f' {key} = "{value}"'
    if self_closing:
        option += ' /'
    if close:
        end = f'{sourse}</{name}>' #make both close and sourse(C-Data)
    else:
        end = '' #Don't close
    returns = f'<{name}{option}>{end}' #return tags
    return returns

"""
this is html markup generater

=== Sourse code that did'nt active : IF We Need, We'll add it ===
def tag_no_special_so_no_error(name : str, sourse : str, **attrebute):
    '''
    It's Vervatim
    oh, **attrebute is not a special option, don't get me wrong
    '''
    return tag(name, sourse, close = True, self_closing = False, **attrebute)

def tnssne(name : str, sourse : str, **attrebute):
    '''
    It's short name of tag_no_special_so_no_error()
    '''
    return tag_no_special_so_no_error(name, sourse, **attrebute)

=== Like .^. but under 63|class TagObject:, It's Extensions for Modularization ===
def MakeTagObjectClass(name : str, docs : str, SubFunctions):
    return type(
        name,
        (TagObject, ),
        {
            '__doc__':docs,
            '__init__':SubFunctions
        }
    )

def MTOC(name : str, docs : str, SubFunctions):
    '''
    It's MakeTagObjectClass()
    '''
    return MakeTagObjectClass(name, docs, SubFunctions)
"""

class TagObject:
    '''
    Tag Object, It's Verbatim
    
    oh, It's not a Real FW -ic Object, don't get me wrong
    It's just functionic Object
    get a sourse to make tag
    '''
    def __init__(self, name : str, close = True, self_closing = False, **attrebute):
        '''
        init function... part....
        '''
        self.name = name
        self.close = close
        self.self_closing = self_closing
        self.attrebute = attrebute
    def __call__(self, sourse):
        '''
        return to tag -> string
        '''
        return tag(self.name, sourse, close = self.close, self_closing = self.self_closing, **self.attrebute)

class TitleBarOption(TagObject):
    '''

    use title_bar()'s argv title_bar_option

    header : Tag Object
    '''
    def __init__(self, close=True, self_closing=False, **attrebute):
        super().__init__('header', close = close, self_closing = self_closing, **attrebute)

class MainBodyOption(TagObject):
    '''

    use title_bar()'s argv main_body_option

    main : Tag Object
    '''
    def __init__(self, close=True, self_closing=False, **attrebute):
        super().__init__('main', close = close, self_closing = self_closing, **attrebute)

class MenuOption(TagObject):
    '''
    title_bar() option "menu" has menu-object [ key : value <==> name : options ]
    
    It used to setting that options

    spen : Tag Object
    '''
    def __init__(self, close=True, self_closing=False, **attrebute):
        super().__init__('spen', close = close, self_closing = self_closing, **attrebute)

class TitleOption(TagObject):
    '''
    use to FoldMenu()'s title_option

    summary : Tag Object
    '''
    def __init__(self, close=True, self_closing=False, **attrebute):
        super().__init__('summary', close = close, self_closing = self_closing, **attrebute)

class MainPartOption(TagObject):
    '''
    use to FoldMenu()'s main_part_options

    div : Tag Object
    '''
    def __init__(self, close=True, self_closing=False, **attrebute):
        super().__init__('div', close = close, self_closing = self_closing, **attrebute)

def FoldMenu(title : str, source : str , main_part_options : MainPartOption, title_option : TitleOption, **options):
    return tag('details', title_option(title) + main_part_options(source), **options)

def title_bar(title : str, title_bar_option : TitleBarOption, main_body_option : MainBodyOption, main_body_sourse : str, **options):
    '''
    making title_bar
    options has Required Data
     ===== [ options's form ] ===== 
    **{
        'titles' : [html argv that title_bar's title],
        'menu' : {
            'bar' : [html argv that title_bar's menu_bar],
            'menu-object' : {
                [name (html)] : [options (MenuOption)],
                ...
                ..
                ..
                .
                .
                .
            }
        }
    }
     ===== [ options real like this] ===== 
    **{
        'titles' : {},
        'menu' : {
            'bar' : {},
            'menu-object' : {
                'lol OwO' : MenuOption(id = 'happy first menu :) '),
                'lol OwO' : MenuOption(id = 'happy second menu :) '),
                'lol OwO' : MenuOption(id = 'happy third menu ;) hahahahahahahahahahhha ')
            }
        }
    }
    '''
    menu = ''
    for x,y in options['menu']['menu-object'].items():
        assert isinstance(y, MenuOption), "menu-object option must be <MenuOption> object"
        menu += y(x)
    title_bar_source = tag('h1', title, **options['titles']) + tag('nav', menu, **options['menu']['bar'])
    return title_bar_option(title_bar_source) + main_body_option(main_body_sourse)

def head_func_title_bar(title_bar, mode:str):
    assert title_bar == None or isinstance(title_bar[0], str), "TypeError : Web page title bar option must be pair that (string, data) or None because of form : if linking css to make title_bar acitve, input 'link', or use style tag, 'style'"
    if title_bar == None:
        pass
    elif title_bar[0] == mode and mode == 'link' and title_bar[0] == 'link':
        print('temp')
        ret = tag('link','',close = False, self_closing = True, rel = "stylesheet", href = title_bar[1]+".css")
        print(ret)
        return ret
    elif title_bar[0] == mode and mode == 'style' and title_bar[0] == 'style':
        print('temp')
        if title_bar[1] != None:
            a = title_bar[1]
        else:
            a = 'header{position:fixed;top:0;left:0;right:0;}main{padding:1rem;height:100%;}body{padding-top:75px;}body,html{height:200%;}*{box-sizing:border-box;}'
        print(a,sep='\n')
        return '\n' + a
    elif title_bar[0] != mode:
        pass
    else:
        raise TypeError("mode must be link or style, It's css, It raise to Active!!!!!!!")

def head(meta_data : tuple, title_bar = None, encoding = 'UTF-8', id = None, style = None, title = None, script = None, link = None, PyScript = False, PyScriptStyle = False, **attrebute):
    '''
    make head part of html DOCS

    argv assert Tips : 
    
    01 | assert title_bar == None or isinstance(title_bar[0], str), "TypeError : Web page title bar option must be pair that (string, data) or None because of form : if linking css to make title_bar acitve, input 'link', or use style tag, 'style'"
    02 | assert encoding == None or isinstance(encoding, str), "TypeError : Web page encoding must be None or string data"
    03 | assert id == None or isinstance(id, str), "TypeError : Web page encoding must be None or string data"
    04 | assert style == None or isinstance(style, str), "TypeError : Web page style must be None or string data"
    05 | assert title == None or isinstance(title, str), "TypeError : Web page title must be None or string data"
    06 | assert script == None or isinstance(script, str), "TypeError : Web page script must be None or string data"
    07 | assert link == None or isinstance(link, dict), "TypeError : Web page link-data must be None or dict data"
    08 | assert isinstance(meta_data[0], str) or isinstance(meta_data[1], str), "TypeError : meta data start 2 end"
    09 | assert isinstance(PyScript, bool), "TypeError : PyScript Bool must be bool"
    10 | assert isinstance(PyScriptStyle, bool), "TypeError : PyScriptStyle Bool must be bool"

    '''
    assert title_bar == None or isinstance(title_bar[0], str), "TypeError : Web page title bar option must be pair that (string, data) or None because of form : if linking css to make title_bar acitve, input 'link', or use style tag, 'style'"
    assert encoding == None or isinstance(encoding, str), "TypeError : Web page encoding must be None or string data"
    assert id == None or isinstance(id, str), "TypeError : Web page encoding must be None or string data"
    assert style == None or isinstance(style, str), "TypeError : Web page style must be None or string data"
    assert title == None or isinstance(title, str), "TypeError : Web page title must be None or string data"
    assert script == None or isinstance(script, str), "TypeError : Web page script must be None or string data"
    assert link == None or isinstance(link, dict), "TypeError : Web page link-data must be None or dict data"
    assert isinstance(meta_data[0], str) or isinstance(meta_data[1], str), "TypeError : meta data start 2 end"
    assert isinstance(PyScript, bool), "TypeError : PyScript Bool must be bool"
    assert isinstance(PyScriptStyle, bool), "TypeError : PyScriptStyle Bool must be bool"
    #Cython : cdef dict option
    #Cython : cdef str sourse
    sourse = meta_data[0]
    option = attrebute #make local var 2 copying attrebute

    if id != None:
        option.update({'id':id}) #html tag id define
        
    if encoding != None:
        sourse += tag('meta', '', close = False, charset = encoding) #setting web encoding
    
    #Pyscript 연관 ~

    #stap1 : style-link
    if PyScriptStyle:
        sourse += head_func_title_bar(title_bar, 'link')
        if link != None:
            sourse += tag('link','',close = False, self_closing = True, rel = link['rel'], href = link['URI'])
        else:
            sourse += tag('link','',close = False, self_closing = True, rel = "stylesheet", href = "https://pyscript.net/latest/pyscript.css")
    else:
        sourse += head_func_title_bar(title_bar, 'link')
        if link != None:
            sourse += tag('link','',close = False, self_closing = True, rel = link['rel'], href = link['URI'])

    #stap2 : main

    if PyScript:
        sourse += tag('script','',**{'defer src':'https://pyscript.net/latest/pyscript.js'})

    #~ Pyscript 연관

    if title != None:
        sourse += tag('title', title) #title

    if style != None:
        style2 = style
        style2 += head_func_title_bar(title_bar, 'style')
        sourse += tag('style', style2) #make CSS 4 style
    elif title_bar != None:
        if title_bar[0] == 'style':
            style2 = ''
            style2 += head_func_title_bar(title_bar, 'style')
            sourse += tag('style', style2) #make CSS 4 style
    else:
        pass

    if script != None:
        sourse += tag('script', script) #make JS 2 script
    
    sourse += meta_data[1]
    returns = tag('head',sourse,**option)
    return returns

def body(sourse : str, id = None, **attrebute):
    '''
    make body part of html DOCS
    '''
    assert id == None or isinstance(id, str), "TypeError : Web page body-id must be None or string data"
    #Cython : cdef dict option
    #Cython : cdef str sourse
    option = attrebute #make local var 2 copying attrebute
    if id != None:
        option.update({'id' : id}) #html tag id define
    returns = tag('body', sourse, **option)
    return returns

def web(head_data:str, body_data:str, lang = None, id = None, **attrebute): #head_data, body_data 각각 맞는 입력값 만들기
    '''
    make web site by form
    var "id" is html tag's id
    '''
    assert lang == None or isinstance(lang, str), "TypeError : Web page language must be None or string data"
    assert id == None or isinstance(id, str), "TypeError : html tag's id must be None(Undefined) or string data"
    #Cython : cdef str returns
    #Cython : cdef str sourse
    #Cython : cdef dict option
    option = attrebute #make local var 2 copying attrebute
    if lang != None:
        option.update({'lang' : lang}) #Web page Langauge Option
    if id != None:
        option.update({'id' : id}) #html tag id define
    sourse = head_data + body_data
    returns = tag('html', sourse, **option)
    return returns

def HTML(head_data:str, body_data:str, lang = None, id = None, **attrebute):
    #Cython : cdef str docs
    '''
    HTML Declaration + web()
    '''
    docs = source + '\n' + web(head_data, body_data, lang = lang, id = id, **attrebute)
    return docs

def test():
    #lol it will work
    #Cython : cdef str data
    with open('body_sourse.html', encoding = 'utf-8') as f:
        value = f.read()
    value=title_bar(
        '파이썬 사이트 테스트',
        TitleBarOption(id = 'H1_title'),
        MainBodyOption(id = 'main'),
        value,
        titles={},
        menu={
            'bar' : {
                'id' : 'menu_bar'
            },
            'menu-object':{        
                tag('a','만든놈',href='https://github.com/tax0787/') : MenuOption(id = 'auther'),
                tag('a','Gitub',href='https://github.com/tax0787/MyHtml') : MenuOption(id = 'repo'),
                tag('a','MarkDown',href='https://github.com/tax0787/MyHtml/blob/main/README.md') : MenuOption(id = 'md')
            }
        }
    )
    #data = HTML(head(('', ''), title_bar = ('link','./HTMLSource/상단바2'), id = 'head_tag', title = '시험적 웹사이트', PyScript = True), body(value, id = 'body_tag'), lang = 'ko')
    data = HTML(head(('', ''), title_bar = ('style',None), id = 'head_tag', title = '시험적 웹사이트', PyScript = True), body(value, id = 'body_tag'), lang = 'ko')
    print(data)
    with open('index.html', 'w', encoding = 'utf-8') as f:
        f.write(data)

def main():
    test()

if __name__ == "__main__":main()

pass #Thinking...
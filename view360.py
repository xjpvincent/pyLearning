# -*- coding: utf-8 -*-
import Image
import ImageTk
import json
import Tkinter  as tk
 
def getpagehtml(pageurl):
        '''获取目标网站任意一个页面的html代码'''
        req2=urllib2.Request(pageurl)
        _response2=urllib2.urlopen(req2)
        _d2=_response2.read()
        return _d2
 
def resize(w, h, w_box, h_box, pil_image):
    f1 = 1.0*w_box/w 
    f2 = 1.0*h_box/h
    factor = min([f1, f2])
    width = int(w*factor)
    height = int(h*factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)
def get360Joke():
    '''360门户'''
    res=getpagehtml("http://xiaohua.hao.360.cn")
    startMark = "var jokes = "
    endMark = "}]];"
    start =res.find(startMark)
    end = res.find(endMark)
    res=res[start+len(startMark):end+3]
    list = json.loads(res)
    return list
def ShowPic(value):
    global postion
    if(value==1):
        postion=postion-1
    if(value==2):
        postion=postion+1
    ShowAjoke(root,title,label,list[postion])
    return postion
def ShowAjoke(root,title,label,ajoke):
    url=ajoke[3]
    image_bytes = urllib.urlopen(url).read()
    # internal data file
    data_stream = io.BytesIO(image_bytes)
    # open as a PIL image object
    pil_image = Image.open(data_stream)
     
    # get the size of the image
    w, h = pil_image.size
    w_box = 600
    h_box = 550
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    wr, hr = pil_image_resized.size
    sf = " {} ({}x{})---360搞笑图片浏览器".format(url, wr, hr)
    root.title(sf)
  
    title['text']=ajoke[1]
    title.pack(fill = "x",expand = 1)
    tk_img = ImageTk.PhotoImage(pil_image_resized)
    label.configure(image = tk_img)
    label.image= tk_img
     
    label.pack(padx=5, pady=5)
'''入口'''   
if __name__ == '__main__':
    root = tk.Tk()
    w_box = 600
    h_box = 550
    list=get360Joke()
    postion=0
    ''' 标题定义'''
    title= tk.Label(root, text="",fg='blue' , bg='gray',font='Helvetica -18 bold')
    title.pack(fill = "x",expand = 1)
    ''' 翻页按钮定义'''
    button = tk.Button(root, text='前一个', command= lambda :ShowPic(1),activeforeground='white',activebackground='red')   
    button.pack(side = "left",padx=20)
    button = tk.Button(root, text='后一个', command= lambda :ShowPic(2),activeforeground='white',activebackground='red')      
    button.pack(side = "right",padx=20)
    ''' 图片框定义'''
    label = tk.Label(root, image="", width=w_box, height=h_box)
    label.pack(padx=15, pady=15)
    ShowAjoke(root,title,label,list[postion])
    root.mainloop()

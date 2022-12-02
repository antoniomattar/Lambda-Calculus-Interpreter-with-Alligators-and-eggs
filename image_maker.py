from ast import Raise
from logging import exception
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logic
import random
import datetime

def color_image(img,color):
    width = img.size[0] 
    height = img.size[1] 
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = img.getpixel((i,j))
            #print(data) #(255, 255, 255)
            if (data[0]==66 and data[1]==66 and data[2]==66):
                img.putpixel((i,j),(color[0], color[1], color[2]))
    return img

colors = ['black','blue','green','orange','pink','purple','red','yellow'] 

dic_colors={'black': (66,66,66), 'blue':(0,119,255), 'green':(0,255,6), 'orange':(255,135,10), 'pink':(249,161,207), 'purple':(255,0,237), 'red':(255,0,6), 'yellow':(247,255,0)} 

inverse_dic_colors={(66,66,66): 'black',(0,119,255):'blue', (0,255,6):'green',(255,135,10):'orange', (249,161,207):'pink', (255,0,237):'purple',(255,0,6):'red', (247,255,0):'yellow'  }

def associateVariableWithColorBis(variable):
    if str(variable) not in variables_colors_couple:
        variables_colors_couple[str(variable)] = dic_colors[colors[-1]]
        return colors.pop()
    else:
        return inverse_dic_colors[variables_colors_couple[str(variable)]]

def new_color():  
    for i in range(3):
        r = random.randint(0,255) 
        g = random.randint(0,255) 
        b = random.randint(0,255)
    return (r,g,b)

def close_colors(a,b):
    r = abs(a[0]-b[0])
    g = abs(a[1]-b[1])
    b = abs(a[2]-b[2])
    return r*r+g*g+b*b <= 100*100


variables_colors_couple = {}

def associateVariableWithColor(variable):
    assert (logic.isVariable(variable))
    c = new_color()
    colorss = list(variables_colors_couple.values())
    for color in colorss:
        if close_colors(c,color):
            associateVariableWithColor(variable)
            break
    if c in list(variables_colors_couple.values()):
        associateVariableWithColor(variable)    # recursive call to not get the same color
    if str(variable) not in variables_colors_couple:
        variables_colors_couple[str(variable)] = c
#------------------------------------------------------------------------------------------------------------------------------------------
class My_image:
    def __init__(self,image,b):
        self.image=image
        self.is_egg=b

    def resize(self,width,height):
        if not(self.is_egg):
            self.image.resize(width, height)
        else:
            self.image.resize(min(self.image.width,width), min(self.image.height,height))
#---------------------------------------------------------------------------------------------------------------------------------
def createVarImage(variable): 
    assert (logic.isVariable(variable)) 
    if len(colors)!=0: 
        k=associateVariableWithColorBis(variable) 
        egg_img = Image.open("figures/egg_"+k+".png") 
        image=My_image(egg_img,True) 
        return egg_img.convert("RGB")
    else: 
        associateVariableWithColor(variable) 
        egg_img = Image.open("figures/egg_black.png") 
        egg_img = egg_img.convert("RGB")
        egg_img = color_image(egg_img,variables_colors_couple[str(variable)]) 
        image=My_image(egg_img,True)
        return egg_img.convert("RGB")

def createAlligator(terme):
    assert (logic.isVariable(terme))
    if len(colors)!=0:
      k=associateVariableWithColorBis(terme) 
      alligator_img = Image.open("figures/alligator_"+k+".png") 
      image=My_image(alligator_img,False) 
      return alligator_img 
    else: 
      associateVariableWithColor(terme) 
      alligator_img = Image.open("figures/alligator_black.png") 
      alligator_img = alligator_img.convert("RGB") 
      alligator_img = color_image(alligator_img,variables_colors_couple[str(terme)]) 
      image=My_image(alligator_img,False) 
      return alligator_img 

def createAbsImage(terme):
    assert (logic.isAbstraction(terme))
    input = logic.getInputFromAbs(terme)
    output = logic.getOutputFromAbs(terme)
    im1 =createAlligator(input)
    im2 = createImage(output)
    im1 = im1.resize((max(im2.image.width, im1.width), max((int(im1.height * im2.image.width / im1.width),im1.height))) )
    abstraction = Image.new('RGB', (max(im1.width, im2.image.width), im1.height + im2.image.height), (255, 255, 255))
    abstraction.paste(im1, ((max(im1.width, im2.image.width)-im1.width) // 2, 0))
    abstraction.paste(im2.image, ( 0 , im1.height))
    return abstraction

space_width = 0

def get_space_wdith():
    return space_width

def get_concat_h_multi_resize(im_list, resample=Image.BILINEAR):
    global space_width
    max_height=max(im.height for im in im_list)
    min_height = min(im.height for im in im_list)
    # max_width = sum(im.width for im in im_list)
    min_width=min(im.width for im in im_list)
    if space_width == 0:
        space_width=(int(min_width*0.3))
    else:
        space_width=min(get_space_wdith(),int(min_width*0.3))
    total_init_width = sum(im.width for im in im_list) + get_space_wdith() * (len(im_list) - 1)
    # im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height), resample=resample)
    #                   for im in im_list]
    # total_width = sum(im.width for im in im_list_resize) + (len(im_list_resize) -1) * space_width
    dst = Image.new('RGB', (total_init_width, max_height),(255,255,255))
    pos_x = 0
    for im in im_list:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width + space_width
    return dst


def createOldAlligator():
    old_alligator_img = Image.open("figures/old_alligator.png")
    return old_alligator_img

def createOldAlligatorFamily(terme):
    old_alli_img = createOldAlligator()
    family_img = createImage(terme)
    old_alli_img = old_alli_img.resize((max(family_img.image.width, old_alli_img.width), max((int(old_alli_img.height * family_img.image.width / old_alli_img.width),old_alli_img.height))) )
    old_alligator_fam = Image.new('RGB', (max(old_alli_img.width, family_img.image.width), old_alli_img.height + family_img.image.height), (255, 255, 255))
    old_alligator_fam.paste(old_alli_img, ((max(old_alli_img.width, family_img.image.width)-old_alli_img.width) // 2, 0))
    old_alligator_fam.paste(family_img.image, ( 0 , old_alli_img.height))
    return old_alligator_fam

def addNumberToImage(image,number):
    draw = ImageDraw.Draw(image.image)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("AllerDisplay_Std_Rg.ttf", 150)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((5, 0),str(number),(0,0,0),font=font)
    return image

def createAppImage(terme):
    assert (logic.isApplication(terme))
    left = logic.getFirstTerm(terme)
    right = logic.getSecondTerm(terme)
    im1 = createImage(left)
    if len(terme) == 4:
        im1 = addNumberToImage(im1,terme[3])
        left = left[:3]
    if len(terme) == 5:
        im1 = addNumberToImage(im1,terme[-1])
    if logic.isApplication(right):
        im2 = createOldAlligatorFamily(right)
        application = get_concat_h_multi_resize([im1.image,im2])
    else:
        im2 = createImage(right)
        application = get_concat_h_multi_resize([im1.image,im2.image])
    return application

def createImage(terme):
    if logic.isVariable(terme):
        return My_image(createVarImage(terme),True)
    if logic.isAbstraction(terme):
        im = createAbsImage(terme)
        if im.width * im.height > 2073600:
            if ((im.width * 0.5 ) * (im.height * 0.5)) < 518400:
                im = im.resize((int(im.width * 0.7), int(im.height * 0.7)))
            else:
                im = im.resize((int(im.width * 0.5), int(im.height * 0.5)))
        return My_image(im,False)
    if logic.isApplication(terme):
        im = createAppImage(terme)
        if im.width * im.height > 2073600:
            if ((im.width * 0.5 ) * (im.height * 0.5)) < 518400:
                im = im.resize((int(im.width * 0.7), int(im.height * 0.7)))
            else:
                im = im.resize((int(im.width * 0.5), int(im.height * 0.5)))
        return My_image(im,False)
    else:
        raise Exception("Unsupported term type")

def saveImage(image,name,path,date=True):
    if date:
        now = datetime.datetime.now()
        now_string = now.strftime("%Y-%m-%d__%H-%M-%S")
        if path == None:
            image.image.save(now_string+'---'+name+'.jpeg', 'jpeg',optimize=True,quality=85)
        else:
            image.image.save(path+'/'+now_string+'---'+name+'.jpeg', 'jpeg',optimize=True,quality=85)
    else:
        if path == None:
            image.image.save(name+'.jpeg', 'jpeg',optimize=True,quality=85)
        else:
            image.image.save(path+'/'+name+'.jpeg', 'jpeg',optimize=True,quality=85)

import os
import moviepy.decorators
import moviepy.editor
import random
import pytube
import wikipedia
from gtts import gTTS

URLvideos = []
PathVideos = []
Videos = []

resize_possible = True
try:
    import cv2
    import numpy as np
    def resizer(pic, newsize):
        lx, ly = int(newsize[0]), int(newsize[1])
        if lx > pic.shape[1] or ly > pic.shape[0]:
            interpolation = cv2.INTER_LINEAR
        else:
            interpolation = cv2.INTER_AREA
        return cv2.resize(+pic.astype('uint8'), (lx, ly), interpolation=interpolation)
    resizer.origin = "cv2"
except ImportError:
    try:
        from PIL import Image
        import numpy as np
        def resizer(pic, newsize):
            newsize = list(map(int, newsize))[::-1]
            shape = pic.shape
            if len(shape) == 3:
                newshape = (newsize[0], newsize[1], shape[2])
            else:
                newshape = (newsize[0], newsize[1])
            pilim = Image.fromarray(pic)
            resized_pil = pilim.resize(newsize[::-1], Image.ANTIALIAS)
            return np.array(resized_pil)
        resizer.origin = "PIL"
    except ImportError:
        try:
            from scipy.misc import imresize
            resizer = lambda pic, newsize: imresize(pic, map(int, newsize[::-1]))
            resizer.origin = "Scipy"
        except ImportError:
            resize_possible = False
from moviepy.decorators import apply_to_mask
def resize(clip, newsize=None, height=None, width=None, apply_to_mask=True):
    w, h = clip.size
    if newsize is not None:
        def trans_newsize(ns):
            if isinstance(ns, (int, float)):
                return [ns * w, ns * h]
            else:
                return ns
        if hasattr(newsize, "__call__"):
            newsize2 = lambda t: trans_newsize(newsize(t))
            if clip.ismask:
                fun = lambda gf, t: (1.0 * resizer((255 * gf(t)).astype('uint8'), newsize2(t)) / 255)
            else:
                fun = lambda gf, t: resizer(gf(t).astype('uint8'), newsize2(t))
            return clip.fl(fun, keep_duration=True, apply_to=(["mask"] if apply_to_mask else []))
        else:
            newsize = trans_newsize(newsize)
    elif height is not None:
        if hasattr(height, "__call__"):
            fun = lambda t: 1.0 * int(height(t)) / h
            return resize(clip, fun)
        else:
            newsize = [w * height / h, height]
    elif width is not None:
        if hasattr(width, "__call__"):
            fun = lambda t: 1.0 * width(t) / w
            return resize(clip, fun)
        newsize = [width, h * width / w]
    if clip.ismask:
        fl = lambda pic: 1.0 * resizer((255 * pic).astype('uint8'), newsize) / 255.0
    else:
        fl = lambda pic: resizer(pic.astype('uint8'), newsize)
    newclip = clip.fl_image(fl)
    if apply_to_mask and clip.mask is not None:
        newclip.mask = resize(clip.mask, newsize, apply_to_mask=False)
    return newclip
if not resize_possible:
    doc = resize.__doc__
    def resize(clip, newsize=None, height=None, width=None):
        raise ImportError("fx resize needs OpenCV or Scipy or PIL")
    resize.__doc__ = doc

def ActiveURL(i):
    q = False
    d = input("\nURL Youtube Видео №" + str(i + 1) + " : com/")
    z = "https://www.youtube.com/" + d
    try:
        pytube.YouTube(z)
        q = False
    except:
        print("\nЭто не рабочий URL!")
        q = True
        l = ActiveURL(i)

    if q == False:
        return z
    else:
        return l
def PathDetected():
    d = input("\nВвести путь на папку: ")
    q = os.path.isdir(d)
    if q == False:
        print("\nЭто не папка")
        d = PathDetected()
        return d
    else:
        b = "\\"
        d = d + b
        return d
def IntError(s):
    d = input(s)
    try:
        f = int(d)
    except:
        print("\nЭто не число")
        d = IntError(s)
    return d
def FloatError(s):
    d = input(s)
    try:
        f = float(d)
    except:
        print("\nЭто не дробное число")
        d = FloatError(s)
    return d
def start():
    c2 = PathDetected()
    x = int(IntError("\nСколько видео: "))
    ptab = PathDetectedText()
    i = 0
    while i < x:
        URLvideos.append(ActiveURL(i))
        i = i + 1
    print("\nВыполнена полная идентификация!")
    print("Начинается загрузка!")
    i = 0
    while i < x:
        downloadervideo(URLvideos[i], c2, i)
        i = i + 1
    print("\nЗагрузка завершена!")

    GenerateAudioBase(c2, ptab)
    pass

def downloadervideo(url, path, i):
    video = pytube.YouTube(url)
    video_type = video.streams.filter(progressive=True, file_extension="mp4").first()
    fp = video_type.download(path)
    PathVideos.append(fp)
    print("\nЗагружено видео №" + str(i+1) + "\nНазвание: " + video.title)
    return video.title

def RandomIDGenerator(length = 5):
    sID = ""
    i = 0
    while i < length:
        sID = sID + str(random.randint(0, 9))
        i = i + 1
    return sID
def PathDetectedText():
    d = input("\nВвести путь на текст: ")
    q = os.path.isfile(d)
    if q == False:
        print("\nЭто не файл .txt")
        d = PathDetected()
        return d
    else:
        return d
def GenerateAudioBase(c2 = "", ptab = ""):
    print("\nНачало генерации аудио-базы")
    randomID = RandomIDGenerator()
    pathsavesound = randomID + ".mp3"
    print(pathsavesound)
    TextAudioBase = ""
    fl = open(ptab, 'r')
    TextAudioBase = fl.read()
    print(TextAudioBase)
    sp = gTTS(text=TextAudioBase, lang="ru")
    sp.save(pathsavesound)
    GenerateVideoBase(pathsavesound, c2)
    print("\nКонец генерации аудио-базы")
    pass

def Translate(i):
    tr = ""
    h = 0
    m = 0
    while i >= 3600:
        i = i - 3600
        h = h + 1
    while i >= 60:
         i = i - 60
         m = m + 1
    s = i

    if h > 9:
        tr = tr + str(h)
    elif h < 10:
        tr = tr + "0" + str(h)
    tr = tr + ":"

    if m > 9:
        tr = tr + str(m)
    elif m < 10:
        tr = tr + "0" + str(m)
    tr = tr + ":"

    if s > 9:
        tr = tr + str(s)
    elif s < 10:
        tr = tr + "0" + str(s)

    return tr
def UnTranslate(i):
    tr = 0
    y = ""
    x = 0
    while x <= 8:
        if x == 0:
            y = y + i[x]
        if x == 1:
            y = y + i[x]
        if x == 2:
            tr = tr + int(y) * 3600
            y = ""
        if x == 3:
            y = y + i[x]
        if x == 4:
            y = y + i[x]
        if x == 5:
            tr = tr + int(y) * 60
            y = ""
        if x == 6:
            y = y + i[x]
        if x == 7:
            y = y + i[x]
        if x == 8:
            tr = tr + int(y)
            y = ""
        x = x + 1
        return tr

def GenerateKeys(Vid, lv):
    e = []
    try:
        VKeys = []
        l = lv
        vs = 0
        while l > 0:
            c = Vid[vs]
            ed = int(c.end)
            sp = random.randint(0, ed)
            cl = random.randint(1, int((ed - sp) / 3))
            if cl > 60: cl == 60
            if l < cl: cl = l
            ep = sp + cl
            l = l - cl
            pk = [Translate(sp), Translate(ep), vs]
            VKeys.append(pk)
            vs = random.randint(0, len(Vid) - 1)
        e = VKeys
    except:
        e = GenerateKeys(Vid, lv)
    return e
def GenerateVideoBase(pathaudiosound = "", c2 = ""):
    print("\nНачало генерации видео-базы")
    audioclip = moviepy.editor.AudioFileClip(pathaudiosound)
    i = 0
    while i < len(PathVideos):
        print(i + 1)
        c = moviepy.editor.VideoFileClip(PathVideos[i])
        if c.size != [1920, 1080]:
            path = "E:\BloggerNN\Cash\Video" + RandomIDGenerator(10) + ".mp4"
            c1 = resize(c, newsize=[1920, 1080])
            c1.write_videofile(path)
            l2 = moviepy.editor.VideoFileClip(path)
            Videos.append(l2)
            PathVideos[i] = path
        else:
            Videos.append(c)
        i = i + 1
    VideoKeys = GenerateKeys(Videos, int(audioclip.end))
    VideoSubclips = []
    print(VideoKeys)
    i = 0
    while i < len(VideoKeys):
        subclp = Videos[VideoKeys[i][2]].subclip(VideoKeys[i][0], VideoKeys[i][1])
        VideoSubclips.append(subclp)
        i = i + 1
    final = moviepy.editor.concatenate_videoclips(VideoSubclips)
    pathend = c2 + "EndFinal.mp4"
    final.set_audio(audioclip)
    final.set_fps(60)
    final.audio = audioclip
    final.write_videofile(pathend)
    print("\nКонец генерации видео-базы")

    DeleteNothing(pathaudiosound, PathVideos)
    GenerateImage(pathend, c2)

    input("Работа окончена")
    pass

def DeleteNothing(pathaudiosound, PathVideos):
    try:
        i = 0
        os.remove(pathaudiosound)
        while i < len(PathVideos):
            path = PathVideos[i]
            os.remove(path)
            i = i + 1
        return True
    except:
        return False

def GenerateImage(pathvideo, c2):
    try:
        clp = moviepy.editor.VideoFileClip(pathvideo)
        ir = random.randint(1, int(clp.end))
        im2 = clp.get_frame(ir)
        moviepy.editor.ImageClip(im2).save_frame(c2 + "\EndScreen.png")
        return True
    except:
        return False

start()
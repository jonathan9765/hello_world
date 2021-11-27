# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:08:39 2018

@author: ParkShinil
"""

import os
import shutil
import zipfile
import time

#shutil.move('a','b')
#shutil.copytree('src_dir','tar_dir')
#shutil.move('src_dir','tar_dir')
#os.remove('a')

def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    return s

def make_folder(folder_name, path=''):
    if type(folder_name) == str:
        pass
    else:
        try:
            folder_name = str(folder_name)
        except:
            pass
    if len(path) != 0:
        folder_name = path+'\\'+folder_name
    else:
        pass
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    else:
        pass

def search_folder(path=''):
    slist = []
    if len(path) == 0:
        path = os.getcwd()
    else:
        pass
    for filename in os.listdir(path):
        fullpath = os.path.join(path,filename)
        slist.append(fullpath)
    return slist

def search_folder2(path=''):
    slist = []
    if len(path) == 0:
        path = os.getcwd()
    else:
        pass
    for (pat,dir,fil) in os.walk(path):
        for f in fil:
            fullpath = os.path.join(pat,f)
            slist.append(fullpath)
            
    return slist

def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zf.extractall(path=dest_path)
        zf.close()
 
def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath);
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()
        
def nameplus(src_list, name, src_path, dest):
    try:
        for s in src_list:
            #parts = s.split('\\')
            #news = name + parts[-1]
            news = name + '_' + s
            ns = src_path + '\\' + s
            ndest = dest + '\\' + news
            shutil.move(ns, ndest)
    except:
        print(name+'failed')
        pass
        
def unzip2(src_path,dest_path):
    fl = search_folder(src_path)
    for f in fl:
        ff = f.split('\\')
        filename0 = ff[-1]
        afilename = filename0.split('.')[0]
        src_fold = '\\'.join(ff[:-1])
        zf = zipfile.ZipFile(f, 'r')
        src_list=[]
        for z in range(0,len(zf.filelist)):
            src_list.append(zf.filelist[z].filename)
        zf.extractall(path=dest_path)
        nameplus(src_list, afilename, src_fold, dest_path)
        
def name_editer(nlist, src_path):
    filelist = search_folder2(src_path)
    for n in nlist:
        for f in filelist:
            if n in f:
                sp = f.split(n)
                new = ''.join(sp)
                shutil.move(f, new)
            else:
                pass
    print('Done') #['.--- [ FreeCourseWeb.com ] ---', '--- [ FreeCourseWeb.com ] ---','--- [ FreeCourseWeb.com ] ---']

def chk_del(instr, optlist):
    instr2 = instr
    if len(instr) > 0:
        inlist = list(instr)
        for opt in optlist:
            if opt in inlist:
                cnt = inlist.count(opt)
                for j in range(0, cnt):
                    inlist.remove(opt)
            else:
                pass
        instr2 = ''.join(inlist) 
    else:
        pass
    return instr2
	
def chk_del2(instr, optlist):
    instr2 = instr
    if len(instr) > 0:
        #inlist = list(instr)
        for opt in optlist:
            if opt in instr2:
                instr2 = '_'.join(instr2.split(opt))
				
            else:
                pass
        #instr2 = ''.join(inlist) 
    else:
        pass
    return instr2

def one_boxing(src, dest):
    sf = search_folder2(src)
	#sf.sort()
    for s in sf:
        #ftype = s.split('.')[-1]
        proc1 = ''.join(s.split(src))
        proc2 = chk_del2(proc1, ['\\', ' '])
        newfile = dest+'\\'+proc2
        shutil.copy(s, newfile)

def filesorting(inname, target_list, dest_folder):
    make_folder(inname, path=dest_folder)
    for t in target_list:
        if inname in t:
            try:
                nt = t.split('\\')[-1]
                ndest = dest_folder + '\\' + inname + '\\' + nt
                shutil.move(t, ndest)
            except:
                print('error')
                pass
    #print('Done')

def auto_fs(sample, src_fold, dst_fold=''): #auto filesorting, sample = '1.mp4'
    tlist = search_folder2(src_fold)
    inlist = []
    if len(dst_fold) == 0:
        dst_fold = src_fold
    else:
        pass
    for t in tlist:
        t2 = t.split('\\')[-1]
        if sample in t2:
            t3 = t2.split(sample)[0]
            inlist.append(t3)
        else:
            pass
    for i in inlist:
        filesorting(i, tlist, dst_fold)
    print('done')
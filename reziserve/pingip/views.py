__author__ = 'keshav'
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from pingip.models import m3servers
from pingip.models import states
from pingip.models import teak
from pingip.models import cgw

import shlex,subprocess
from os import system
import os
# Create your views here.

def index(request,value,serv,key):
    rc=[]
    if serv =="s":
        iplist=m3servers.objects.filter(City = key)
    elif serv =="t":
        iplist=teak.objects.filter(City = key)
    if serv =="c":
        iplist=cgw.objects.filter(City = key)

    try:

        for q in iplist :
            response = os.system("ping -c 1 -W 1000" + str(q.IP) + " > /dev/null 2>&1")
            if response == 0:
                rc.append([0,q])

            else:
                rc.append([1,q])




    finally:

        c=RequestContext(request)
        c['rc'] = rc
        t=loader.get_template('index.html')
        return HttpResponse(t.render(c))

def indexi(request,key,serv):


    state = states.objects.filter(id=key)
    cityinfo = [["null", 0,0,[0,],0,0,0]]
    for q in state:
        if serv == "s":
            cityipslist = m3servers.objects.all()
            for citi in cityipslist:
                add = 0
                response = os.system("ping -c 1 -W 1000" + str(citi.IP) + " > /dev/null 2>&1")
                contains = 0
                for i in cityinfo:
                    if citi.City == i[0]:
                        contains = 1
                        i[3].append(citi.IP)
                        if response == 0:
                            i[4]+=1
                            i[6]+=1
                        else:
                            i[5]+=1
                            i[6]+=1
                        break
                if contains ==0:
                    if response == 0:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],1,0,1])
                    else:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],0,1,1])
        elif serv == "t":
            cityipslist = teak.objects.all()
            for citi in cityipslist:
                add = 0
                response = os.system("ping -c 1 -W 1000" + str(citi.IP) + " > /dev/null 2>&1")
                contains = 0
                for i in cityinfo:
                    if citi.City == i[0]:
                        contains = 1
                        i[3].append(citi.IP)
                        if response == 0:
                            i[4]+=1
                            i[6]+=1
                        else:
                            i[5]+=1
                            i[6]+=1
                        break
                if contains ==0:
                    if response == 0:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],1,0,1])
                    else:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],0,1,1])
        elif serv == "c":
            cityipslist = cgw.objects.all()
            for citi in cityipslist:
                add = 0
                response = os.system("ping -c 1 -W 1000" + str(citi.IP) + " > /dev/null 2>&1")
                contains = 0
                for i in cityinfo:
                    if citi.City == i[0]:
                        contains = 1
                        i[3].append(citi.IP)
                        if response == 0:
                            i[4]+=1
                            i[6]+=1
                        else:
                            i[5]+=1
                            i[6]+=1
                        break
                if contains ==0:
                    if response == 0:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],1,0,1])
                    else:
                        cityinfo.append([citi.City, citi.Latitude,citi.Longitude,[citi.IP,],0,1,1])
    #if we want to change for any manual entry
    c=RequestContext(request)
    t=loader.get_template('stateindex.html')
    c['cityinfo'] = cityinfo
    c['serv'] = serv
    return HttpResponse(t.render(c))






def home(request):
    t=loader.get_template('home.html')
    statelist = states.objects.all()
    streamer_servers = m3servers.objects.all()
    scount = []
    tcount = []
    ccount = []
    for q in statelist:
        pings = m3servers.objects.filter(State=q.Abbr)
        avails = 0
        navails = 0
        for s in pings:
            response = os.system("ping -c 1 -W 1000" + str(s.IP) + " > /dev/null 2>&1")
            if response == 0:
                  avails+=1
            else:
                navails+=1
        totals = len(pings)
        pingt = teak.objects.filter(State=q.Abbr)
        availt = 0
        navailt = 0
        for s in pingt:
            response = os.system("ping -c 1 -W 1000" + str(s.IP) + " > /dev/null 2>&1")
            if response == 0:
                  availt+=1
            else:
                navailt+=1
        totalt = len(pingt)
        pingc = cgw.objects.filter(State=q.Abbr)
        availc = 0
        navailc = 0
        for s in pingc:
            response = os.system("ping -c 1 -W 1000" + str(s.IP) + " > /dev/null 2>&1")
            if response == 0:
                  availc+=1
            else:
                navailc+=1
        totalc = len(pingc)
        if totals !=0:
            scount.append([totals,q,avails,navails])
        if totalt !=0:
            tcount.append([totalt,q,availt,navailt])
        if totalc !=0:
            ccount.append([totalc,q,availc,navailc])

    teak_servers = teak.objects.all()
    cgw_servers = cgw.objects.all()
    c=RequestContext(request)
    c['s_server'] = streamer_servers
    c['t_server'] = teak_servers
    c['c_server'] = cgw_servers
    c['scount'] = scount
    c['tcount'] = tcount
    c['ccount'] = ccount
    return HttpResponse(t.render(c))




from codecs import decode
from hashlib import sha1
import hashlib


d=' me ans you'
'''
def ans2(x):
    b=x.upper()
    return b

print(ans2(d))

q4=[5, 3, 8, 3, 76, 332, 5, 0, 3]
def ans4(x):
    x.sort()
    return x


print(ans4(q4))'''

# d= '64.242.88.10 - - [08/Mar/2004:10:40:09 -0800] "GET /twiki/bin/view/TWiki/TWikiTopics?rev=r1.7 HTTP/1.1" 200 8540\n64.242.88.10 - - [08/Mar/2004:10:45:25 -0800] "GET /twiki/bin/search/Main/SearchResult?scope=text&regex=on&search=Thanadon%20*Somdee[^A-Za-z] HTTP/1.1" 200 4287\n64.242.88.10 - - [08/Mar/2004:10:46:34 -0800] "GET /twiki/bin/view/TWiki/TWikiUpgradeTo01May2000?rev=1.3 HTTP/1.1" 200 7441\n10.0.0.153 - - [08/Mar/2004:10:48:02 -0800] "GET / HTTP/1.1" 304 -\n10.0.0.153 - - [08/Mar/2004:10:48:05 -0800] "GET /cgi-bin/mailgraph2.cgi HTTP/1.1" 200 2987\n10.0.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_0_err.png HTTP/1.1" 200 7213\n10.0.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_0.png HTTP/1.1" 200 7970\n10.2.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_1_err.png HTTP/1.1" 200 7254\n10.2.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_1.png HTTP/1.1" 200 8821\n10.0.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_2_err.png HTTP/1.1" 200 6866\n10.4.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_2.png HTTP/1.1" 200 9312\n10.5.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_3.png HTTP/1.1" 200 6596\n10.0.0.153 - - [08/Mar/2004:10:48:06 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_3_err.png HTTP/1.1" 200 5499\n64.22.88.10 - - [08/Mar/2004:10:48:19 -0800] "GET /twiki/bin/edit/Main/Max_use?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/index.html HTTP/1.1" 304 -\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam.1day.png HTTP/1.1" 200 3080\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam-ratio.1day.png HTTP/1.1" 200 2224\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam.1week.png HTTP/1.1" 200 3299\n10.0.32.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam.1month.png HTTP/1.1" 200 2481\n10.0.32.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-hashes.1week.png HTTP/1.1" 200 1667\n10.0.32.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam-ratio.1week.png HTTP/1.1" 200 2346\n10.0.32.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam-ratio.1month.png HTTP/1.1" 200 1872\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-hashes.1month.png HTTP/1.1" 200 1585\n10.0.2.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam.1year.png HTTP/1.1" 200 2202\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-spam-ratio.1year.png HTTP/1.1" 200 1833\n10.0.0.153 - - [08/Mar/2004:10:48:37 -0800] "GET /dccstats/stats-hashes.1year.png HTTP/1.1" 200 1521\n64.242.88.10 - - [08/Mar/2004:10:50:05 -0800] "GET /twiki/bin/rdiff/TWiki/WebRss HTTP/1.1" 200 21483\n64.242.88.10 - - [08/Mar/2004:11:03:34 -0800] "GET /twiki/bin/rdiff/TWiki/WikiCulture?rev1=1.8&rev2=1.7 HTTP/1.1" 200 5326\n128.227.88.79 - - [08/Mar/2004:11:06:20 -0800] "GET /twiki/bin/view/Main/SpamAssassinAndPostFix HTTP/1.1" 200 4034\n128.227.88.79 - - [08/Mar/2004:11:06:20 -0800] "GET /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif HTTP/1.1" 304 -\n128.227.88.78 - - [08/Mar/2004:11:06:28 -0800] "GET /twiki/bin/view/Main/SpamAssassinTaggingOnly HTTP/1.1" 200 5691\n64.242.88.10 - - [08/Mar/2004:11:09:24 -0800] "GET /twiki/bin/edit/Main/Lmtp_mail_timeout?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846\n128.227.88.79 - - [08/Mar/2004:11:10:09 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419\n128.227.88.79 - - [08/Mar/2004:11:10:24 -0800] "GET /twiki/bin/view/Main/PostfixCommands HTTP/1.1" 200 4016\n128.227.88.79 - - [08/Mar/2004:11:11:04 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419\n128.27.88.79 - - [08/Mar/2004:11:11:10 -0800] "GET /twiki/bin/view/Main/TWikiGroups HTTP/1.1" 200 4816\n128.27.88.79 - - [08/Mar/2004:11:11:15 -0800] "GET /twiki/bin/view/Main/TWikiAdminGroup HTTP/1.1" 200 4175\n128.27.88.79 - - [08/Mar/2004:11:11:26 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419\n64.242.88.10 - - [08/Mar/2004:11:11:51 -0800] "GET /twiki/bin/edit/Main/TWikiGuest?t=1078713282 HTTP/1.1" 401 12846\n64.242.88.10 - - [08/Mar/2004:11:15:51 -0800] "GET /twiki/bin/rdiff/TWiki/AdminSkillsAssumptions HTTP/1.1" 200 10368\n64.242.88.10 - - [08/Mar/2004:11:17:49 -0800] "GET /twiki/bin/view/Sandbox/WebHome?rev=r1.3 HTTP/1.1" 200 8708\n64.242.88.10 - - [08/Mar/2004:11:19:43 -0800] "GET /twiki/bin/edit/TWiki/WikiNotation?t=1078726052 HTTP/1.1" 401 12846\n64.242.88.10 - - [08/Mar/2004:11:24:12 -0800] "GET /twiki/bin/search/TWiki/SearchResult?scope=text&regex=on&search=Wiki%20*Notation[^A-Za-z] HTTP/1.1" 200 6558\n6.242.88.10 - - [08/Mar/2004:11:25:16 -0800] "GET /twiki/bin/oops/TWiki/WikiNotation?template=oopsmore&param1=1.3&param2=1.3 HTTP/1.1" 200 11263\n10.0.0.153 - - [08/Mar/2004:11:40:41 -0800] "GET /cgi-bin/mailgraph2.cgi HTTP/1.1" 200 2987\n10.0.0.152 - - [08/Mar/2004:11:40:42 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_0_err.png HTTP/1.1" 200 7226\n10.0.0.153 - - [08/Mar/2004:11:40:42 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_0.png HTTP/1.1" 200 8055\n10.0.0.151 - - [08/Mar/2004:11:40:42 -0800] "GET /cgi-bin/mailgraph.cgi/mailgraph_1.png HTTP/1.1" 200 8787\n'

# def ans19(z): 
#     slp= z.split('\n') 
#     new_lis=[] 

#     for i in slp: 
#         line= i.split(' ') 
#         ips=line[0] 
        
#         if ips not in new_lis: 
#             new_lis.append(ips)  

#     return (new_lis[0:14]) 

# print(ans19(d)) 
#
# 
# 
#question 24
# 
# data=3
# def ans24(N):
#      l=list()
#      for i in range(1,101):
#              if i %3 ==0:
#                      l.append(i+1)
#      return l
 
# print(ans24(3)) 


#question 28
# M= '192.168.1.101,  a4::67:06:8d:83:a1, a4:67:06:8d:a1, a4:67:06:8d:83:a1, ff02::fb' 
# print(M)
# def ans28(x): 

#     spl=x.split(', ') 

#     return spl[3]

# print(ans28(M)) 
# print(type(M))


#question 29:
# d = '2020'

# def ans29(X):
#     resp=int(X)
#     ss=resp-1981
    
#     return ss
# print(ans29(d))



#question 25

d='81976bcf73b15bcb269b92f2f6b66867b9b804c6'

dd= decrypt(d)

print(dd)
def ans25(x):
    #dd= x.decode(sha1)
    l= decrypt("e",x)

    return l
print(ans25(d))




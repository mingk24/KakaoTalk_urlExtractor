'''
written by mingk24@gmail.com / 2018.12.27

카카오톡 덤프파일(KaKaoTalkChats.txt)을 읽어서 
URL을 포함하고 있는 라인의 정보만을 출력하는 코드

ps) 이해를 돕기위해 디버그용 프린트문은 남겨놓음 
'''

# 입출력 파일이름은 하드코딩 -.-a
import msvcrt as m
def wait():
    m.getch()

f_in  = open("KakaoTalkChats.txt", 'rt', encoding='UTF8')
f_out = open("KakaoTalkChats_res.txt", 'wt', encoding='UTF8' )

g_date = ""
g_author =""

while True:
    line = f_in.readline()

    if not line: break

    print ('INPUT = ['+line+']')
    idx = line.find(',')
    if (idx == -1):
        #continue
        if (line.find('http') != -1):
            html_url = line.strip()
            print ('RESULT=', html_url)
            f_out.write(g_date+'\t'+g_author+'\t'+' '+'\t'+html_url+'\n')
            
            #print (html_url)
        else:            
            #print('Skip...\n')
            continue
    else: 
        date = line[0:idx]
        #print('date='+date)

        remains = line[idx+1:]
        #print('remains='+ remains)
        idx2 = remains.find(':')

        #print('idx2=',idx2)

        if (idx2 == -1 ):
            author = ""
            continue   # ex) 콤마(,)는 있지만 콜론(:)이 없음  이2017년 10월 10일 오후 5:03, 이상협과장 UT팀님이 박미령님을 초대했습니다.
        else: 
            author = remains[0: idx2]
            data = remains[idx2+1:].strip() 

    # print ('Date='+date)
    # print ('Author='+author)
    # print ('Message='+data)

    html_idx = data.find('http')
    if (html_idx == -1):
        # print ('No info.\n')
        continue
    else:
        html_message = data [0: html_idx]
        html_url = data[html_idx:]
        # print ('Date='+date)
        # print ('Author='+author)
        # print ('html_message='+html_message)
        # print ('html_url    ='+html_url)

        print ('RESULT=', date, author, html_message, html_url)
        f_out.write(date+'\t'+author+'\t'+html_message+'\t'+html_url+'\n')

    g_date = date
    g_author = author
    #wait()


f_in.close()
f_out.close()
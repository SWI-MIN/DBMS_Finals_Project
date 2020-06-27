# 讀csv檔，並從中依條件搜尋，並列出該條件結果
# import tracemalloc

print ('1. 依學生學號 => input \"1\"')
print ('2. 依課程代號 => input \"2\"')
choose = input()

count = 0   # 紀錄課程人數

if choose == '1' :
    with open('shit.csv', 'r') as fp:      # 開檔一次讀一行，把開啟讀到的檔案丟給fp
        print ('輸入要查詢的學生 ID : ',end= '')
        stuid = input()
        while True:
            s = fp.readline()
            if s == '':
                break
            if stuid in s:
                print(s,end= '')
elif choose == '2' :
    # tracemalloc.start()          # 我們透過 start() 開始記憶體除錯的功能：
    with open('shit.csv', 'r') as fp:    # 開檔一次讀一行
        print ('輸入要查詢的課程 ID : ',end= '')
        courseid = input()
        while True:
            s = fp.readline()    #一次讀一行
            s=s.strip('\n')    #去掉 \n 為了方便判斷 endswith() 是否為 True
            if s == '':        # 沒東西，空了，break
                break
            if s.endswith(courseid) == True:  # 從後面看有符合courseid，endswith(字符或字串, 開始位置, 結束位置)
                s += '\n'       # 把 \n 加回來
                print(s,end= '')
                count+=1
    # snap = tracemalloc.take_snapshot()         # 想要記錄下當前的記憶體配置就使用 snapshot()：
else :
    pass

if count>1:
    print(count)

fp.close  # 關檔

# tracemalloc.stop()          #結束時使用 stop() 結束除錯：
# stats = snap.statistics('lineno')        # 以下三行是查看當前記憶體狀況，但我不知道為什麼這麼用
# for stat in stats:
#     print(stat)



# Python 讀取與寫入 CSV 檔案教學與範例
# https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

# Python 逐行讀取檔案內容的 4 個方法
# https://www.opencli.com/perl/4-ways-write-file-line-by-line-in-python

# Python 使用 open() 開啟大檔案時避免記憶體錯誤的方法
# https://clay-atlas.com/blog/2020/04/20/python-cn-open-big-file-with-read-size/

# Python String endswith()
# https://www.programiz.com/python-programming/methods/string/endswith

# tracemalloc — 記憶體配置除錯 — 你所不知道的 Python 標準函式庫用法 09
# https://blog.louie.lu/2017/08/04/tracemalloc-python-standard-library-09/

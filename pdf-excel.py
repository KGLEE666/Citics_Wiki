import pandas as pd
import pdfplumber
import os



#获取pdf文件名
def file_name(file_dir):
    for files in os.walk(file_dir):
        return files



def parsePDF(files):
    df3 = pd.DataFrame(columns=['A'])
    for file in files:
        #list1 = []
        file_path = file_dir+file
        with pdfplumber.open(file_path) as pdf:
            for i in range(100):
                pages = pdf.pages[i]
                tt = pages.extract_text()
                if tt is None:
                    continue
                elif '分地区' in tt:
                    l1 = tt.split('\n')  #根据换行符将文本拆成list
                    l2 = []
                    for l in l1:
                        l = l.split(' ')  #再根据空格拆成二维list，因为数据字段之间是用空格分开的，属于分列操作
                        l2.append(l)
                    # 得到的table是嵌套list类型，转化成DataFrame更加方便查看和分析
                    df = pd.DataFrame(l2)   
                    break
                else:
                    continue
        rr =  []
        for row in df.itertuples():
            rr.append(row[1])
        k=0
        for r in rr:
            if '分地区' in r:
                df2 = df.drop(list(range(k)))
                k=k+1
                df3 = pd.concat([df2,df3])
                break
            else:
                k=k+1     
    return df3

 
if __name__ == '__main__':

    #年报存放路径
    file_dir = 'D:/中信证券暑期/同业竞争2021/2020年报/'
    files = file_name(file_dir)[-1]
    data = parsePDF(files)
    data.to_excel('D:/中信证券暑期/同业竞争2021/test1.xlsx')




import urllib.request
import json
import csv

def getdata(indate):
    headers={
    'Host': 'huiyan.baidu.com',
    'Connection': 'keep - alive',
    'User - Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': '* / *',
    'Sec - Fetch - Site': 'same - site',
    'Sec - Fetch - Mode': 'no - cors',
    'Referer': 'https: // qianxi.baidu.com /',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh',
    'q' : '0.9',
    'cookie':' BIDUPSID=163D270C00008EE349117DD27AC58CBE; PSTM=1562302546; BAIDUID=5E9E0BBE6DFFC5779D1B5A326398786E:FG=1; delPer=0; PSINO=7; ZD_ENTRY=empty; H_WISE_SIDS=141176_114552_141192_139405_138496_135846_141000_139148_138471_138451_139193_138878_137978_140173_131247_132552_137746_138165_107317_138883_140260_141372_139057_140202_136863_138585_139171_140078_140114_136196_131861_140591_140324_140578_133847_140793_140065_131423_141175_140311_140839_136413_136752_110085_127969_140593_140865_139886_140993_139408_128200_138312_138426_141194_139557_140684_141191_140597_139600_140964; H_PS_PSSID=1450_21096_30495; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PHPSESSID=9lg79hs0alm3ktedls42n17gb2'
    }

    url='https://huiyan.baidu.com/migration/cityrank.jsonp?dt=country&id=420100&type=move_out&date='+str(indate)+'&callback=jsonp_1580799999370_2181648'
    req=urllib.request.Request(url,headers=headers,method='GET')
    response=urllib.request.urlopen(req)

    data2={}
    data2=response.read().decode('utf-8')
    data3=eval(data2.replace('jsonp_1580799999370_2181648',' '))
    data4=data3['data']
    data5=json.dumps(data4)



    data=json.loads(data5)
    filename=str(indate)+'.json'
    with open(filename,'w')as f:
        f.write(json.dumps(data,ensure_ascii=False))
    jname=str(indate)+'.json'
    cname=str(indate)+'.csv'
    jsontocsv(jname,cname)

def jsontocsv(jsonname,csvname):
    #open json file
    dict_list=list()
    with open(jsonname,'r') as jsonfile:
        load_json=json.load(jsonfile)
    with open(csvname, "w", newline='') as csvfile:

        fieldnames=["city_name", "province_name", "value"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(load_json['list'])



for i in range(20200102,20200104):
    getdata(i)
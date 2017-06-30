# coding=utf-8
import re

from modelLoad import response

res = ''
res = raw_input("Bot>")
productName = ''
time = ''
while len(res) > 0:
    botRes = response(res)

    if botRes == 'about':
        if re.match('DAS', res, re.IGNORECASE):
            print botRes + " DAS"
            print "WSO2 Data Analytics Server is a powerful open source analytics product that analyzes data streams " \
                  "in real time. It allows you to understand events, map their impacts, identify patterns and react " \
                  "within milliseconds."
            productName = 'DAS'
            print

        if re.search('APIM', res, re.IGNORECASE):
            print botRes + 'APIM'
            print 'WSO2 API Manager is a 100% open source enterprise-class solution that supports API publishing, ' \
                  'lifecycle management, application development, access control, rate limiting and analytics in one' \
                  'cleanly integrated system.'
            productName = 'APIM'
        if re.search('wso2', res, re.IGNORECASE):
            print botRes + ' WSO2'
            print 'WSO2 (sometimes stylized as WSO2) is an open source technology provider that uniquely increases ' \
                  'the agility of digital businesses and enterprises engaging in digital transformation. It offers' \
                  ' the only completely integrated enterprise platform that enables businesses to build, integrate,' \
                  ' manage, secure and analyze their APIs, applications, and web services—on-premises, in the cloud,' \
                  ' on mobile devices, and across the Internet of Things.'
            print 'For more please visit www.wso2.com'

    if botRes == 'purchaseCount':
        if re.match('DAS', res, re.IGNORECASE):
            time = re.findall(r'\d+\S\d+\S\d+', res)
            if time.__str__() in res:
                print time.__str__() + 'DAS'
            else:
                print botRes + 'No time given'
    print botRes

    res = raw_input("Bot>")

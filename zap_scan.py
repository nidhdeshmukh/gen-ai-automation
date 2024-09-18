#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from zapv2 import ZAPv2

api_key = 'your-api-key'
target = 'https://your-app-url.com'

zap = ZAPv2(apikey=api_key)

print('Accessing target %s' % target)
zap.urlopen(target)

print('Spidering target %s' % target)
zap.spider.scan(target)

print('Waiting for spider to complete...')
while int(zap.spider.status()) < 100:
    print('Spider progress %: ' + zap.spider.status())
    time.sleep(5)

print('Scanning target %s' % target)
zap.ascan.scan(target)

print('Waiting for scan to complete...')
while int(zap.ascan.status()) < 100:
    print('Scan progress %: ' + zap.ascan.status())
    time.sleep(5)

print('Scan completed')
print('Alerts: %s' % zap.core.alerts())


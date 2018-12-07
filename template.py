#!/usr/bin/python

structured_template = '''
<doc docId="%(docId)s">
%(summary)s
</doc>'''

normal_template = '''
<doc docId="%(docId)s">
<item>
<display>
<url><![CDATA[%(url)s]]></url>
<title><![CDATA[%(title)s]]></title>
<content><![CDATA[%(summary)s]]></content>
</display>
</item>
</doc>'''

tuwen_template = '''
<doc docId="%(docId)s">
<item>
<display>
<url><![CDATA[%(url)s]]></url>
<title><![CDATA[%(title)s]]></title>
<imageurl><![CDATA[%(url)s]]></imageurl>
<imagecontent><![CDATA[%(tuwen_summary)s]]></imagecontent>
</display>
</item>
</doc>'''


data = {'title': 'My Home Page', 'text': 'Welcome to my home page.'}

print structured_template % data

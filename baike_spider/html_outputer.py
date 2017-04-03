# Created by joqk12345 on 4/3/17.
# www.github.com/joqk12345

#!/usr/bin/env python
# -*- conding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]

    def collect_data(self,date):
        if date is None:
            return
        self.datas.append(date)

    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

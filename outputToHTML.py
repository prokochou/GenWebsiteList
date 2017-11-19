
import yaml

# input file
listFile = open("topSite.txt", 'r')
htmlFile = open('webPage.html', 'r')
new_htmlFile = open('webPage_new.html', 'w')

# open file and read it

# read html file
html_content = htmlFile.readlines()

# read txt file
site_content = listFile.read()

# make site list to html site list
site_list = site_content.split('\n')

site_html_ls = []
for i in range(len(site_list)):
    link = site_list[i]
    link_format = ('<p><a target="_blank" href="%s">%s</a></p>' % (link, link))
    site_html_ls.append(link_format)

# combine list content into string
all_site = ""
for i in range(len(site_html_ls)):
    all_site = all_site + site_html_ls[i] + '\n' + '\t'


# replace 'to_be_displayed' to site list
for i in range(len(html_content)):
    if html_content[i].find('to_be_displayed\n') != 1:
        content = html_content[i].replace('to_be_displayed\n', all_site)
        new_htmlFile.write(content)

# close files
listFile.close()
htmlFile.close()
new_htmlFile.close()



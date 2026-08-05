import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove any <tr> row that contains style="opacity:0.4;" and 已刪除
html = re.sub(r'<tr style=\"opacity:0.4;\">.*?已刪除.*?</tr>\n?', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(<td>自修（康軒）</td><td><span class="status status-ok">✅) book168 #[0-9]+(</span></td>)', r'\1 已在康軒官網/商城購買\2', html)
html = re.sub(r'(<td>評量（康軒）</td><td><span class="status status-ok">✅) book168 #[0-9]+(</span></td>)', r'\1 已在康軒官網/商城購買\2', html)
html = re.sub(r'(<td>正版測驗卷（康軒）</td><td><span class="status status-ok">✅) book168 #[0-9]+(</span></td>)', r'\1 已在康軒官網/商城購買\2', html)

html = re.sub(r'(<td><span class="status status-ok">✅) 已在 book168 購物車 \(#[0-9]+\)(</span></td></tr>)', r'\1 已在 康軒官網/商城 購買\2', html)

html = re.sub(r'<tr><td>([0-9]+)</td><td>(康軒國小.*?)</td><td>(<code.*?psn:[0-9]+.*?</code>)</td><td>1</td><td>(\\$[0-9]+)</td><td>(<span class="child-tag.*?)>.*?</span></td></tr>', 
              r'<tr style=\"opacity:0.4;\"><td>\1</td><td><s>\2</s></td><td>\3</td><td><strong style=\"color:var(--danger)\">0</strong></td><td>\4</td><td>\5 style=\"background:rgba(255,255,255,0.1);color:var(--text-dim)\">已刪除</span></td></tr>', html)

html = html.replace('扣除 Ken 品項後剩餘 20 筆 20 件 · 原價 ,256 → 9.8 折 <strong style=\"color:var(--accent-green)\">,191</strong>', 
                    '扣除 Ken 與康軒品項後剩餘 8 筆 8 件 · 總價 <strong style=\"color:var(--accent-green)\"></strong> (未達 ,200 免運及折扣門檻)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

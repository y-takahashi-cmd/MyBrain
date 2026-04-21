import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'C:/Users/y-takahashi/MyBrain/work-launcher.json'
new_path = 'C:/Users/y-takahashi/MyBrain/20_Projects/企業のオンライン保健室/クラウドパワー株式会社/02_報告会記録/クラウドパワー様_2026年4月_月次報告書.docx'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

for section in data['localSections']:
    if section['title'] == '📋 報告書':
        for link in section['links']:
            if 'CP 4月報告書' in link['label']:
                print('変更前:', link['path'])
                link['path'] = new_path
                print('変更後:', link['path'])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('保存完了')

from scrapy.selector import Selector


# 1. 读取 xml 文件信息
xml = ''
with open('test.xml') as f:
    xml = f.read()

# 2. 使用 scrapy.selector.Selector 解析 xml
sel = Selector(text=xml)

# 3. 解析需要的数据到 record.txt 中
with open('record.txt', 'w') as f:
    for line in sel.xpath('//testitem'):
        f.write('item1 = ' + line.xpath('./@item1').extract_first()
                + '  item5 = ' + line.xpath('./@item5').extract_first()
                + '\r\n')

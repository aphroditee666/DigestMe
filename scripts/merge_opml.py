import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date

def parse_opml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    body = root.find('body')
    feeds = []
    for outline in body.iter('outline'):
        xml_url = outline.get('xmlUrl', '')
        text = outline.get('text', outline.get('title', ''))
        if xml_url:
            feeds.append({'text': text.strip(), 'xmlUrl': xml_url})
    return feeds

f1 = parse_opml('docs/RSS订阅源/BestBlogs/BestBlogs_RSS_Articles.opml')
f2 = parse_opml('docs/RSS订阅源/awesome-rsshub-routes/feeds_my_fillter.opml')

# Deduplicate by normalized URL
seen = set()
merged = []
for f in f2 + f1:
    url = f['xmlUrl'].rstrip('/')
    if url not in seen:
        seen.add(url)
        merged.append(f)

def categorize(name, url):
    nl = name.lower()
    ul = url.lower()

    if any(k in nl for k in ['arxiv', 'nature', 'acm', 'ieee']):
        return "学术论文"

    if any(k in nl for k in ['techcrunch', 'the verge', 'wired', 'ars technica',
            'mit technology', '极客公园', '爱范儿', '少数派', 'it之家',
            'founder park', '海外独角兽', '创业邦', '经纬创投',
            '真格基金', '暗涌', '甲子光年', '白鲸出海', '硅星人',
            '硅谷', '吴晓波', '刘润', '晚点', '十字路口',
            '42章经', '随机小分队', '有新', 'z potentials',
            '深网', '网易科技', '智东西', '腾讯科技', '笔记侠',
            '强少来了', '土猛的员外', '人人都是产品经理',
            'smashing']):
        return "科技媒体"

    if any(k in nl for k in ['aws', 'amazon', 'google cloud', 'google developers',
            'google for developers', 'the keyword', 'microsoft',
            'engineering at meta', 'netflix', 'spotify', 'stripe',
            'cloudflare', 'vercel', 'supabase', 'github blog', 'mozilla',
            'docker', 'jetbrains', 'intellij', 'visual studio', 'node.js',
            'mongodb', 'elastic', 'grafana', 'spring',
            '阿里技术', '阿里云', '腾讯技术', '腾讯云', '字节跳动',
            '小米技术', '哔哩哔哩技术', '美团技术', '京东技术',
            '百度geek', '大淘宝', '得物技术', 'vivo', 'qunar',
            '快手技术', '小红书技术', '腾讯研究院', '阿里研究院',
            '谷歌开发者', '腾讯混元', '百度ai', 'firecrawl',
            'next.js', 'the github blog', 'microsoft research']):
        return "大厂技术博客"

    if any(k in nl for k in ['ai', 'llm', 'gpt', 'claude', 'openai', 'deepmind',
            'deepseek', 'hugging', 'stability', 'kimi', '智谱', '通义',
            '混元', 'minimax', '阶跃星辰', 'jina ai', 'groq',
            'elevenlabs', 'databricks', 'llamaindex', 'langchain',
            'machine learning', 'deep learning', 'aigc', 'sota', 'ainlp',
            'datawhale', 'qdrant', 'dify', '魔搭', 'copilot',
            'anysphere', 'showmeai', '机器之心', '新智元', '量子位',
            'ai前线', 'ai科技', 'paperweekly', 'ai产品', 'ai思想',
            'aiwalker', 'paperagent', '数源ai', '智能涌现',
            'ai炼金术', 'ai寒武纪', '夕小瑶', '归藏', '卡尔的ai',
            '赛博禅心', 'ai musing', 'latent space', 'last week in ai',
            'supertechfans', 'deeplearning', '李继刚', '山行ai',
            '大模型智能', '数字生命卡兹克', '袋鼠帝ai', '青哥谈ai',
            '沃垠ai', '向阳乔木', 'ai小小将', '小样本视觉',
            'google ai', 'google deepmind', 'meta ai', 'hugging face',
            'stability ai', 'simon willison', 'anthropic',
            'addyo', 'elevate', 'kelvinmu', '字节跳动seed',
            'openclaw', 'dhh', 'ginonotes']):
        return "AI专题"

    if any(k in nl for k in ['hacker news', 'v2ex', 'linuxdo', 'stack overflow',
            'infoq', 'csdn', '掘金', '稀土', '51cto', 'dbaplus',
            'hellogithub', '印记中文', 'freecodecamp', '阮一峰', '宝玉',
            '花叔', 'thoughtworks', 'martin fowler', '前端', '优设',
            '体验进阶', 'clip设计', '开源', '架构师', '奇舞', '超人',
            '浮之静', 'yikai', 'l先生说', '曾天真']):
        return "技术社区"

    if any(k in nl for k in ['weekly', 'newsletter', 'bytebytego', 'this week in']):
        return "技术周刊"

    if 'wechat2rss' in ul or 'wechat/sogou' in ul:
        return "微信公众号"

    if any(k in nl for k in ['ux', 'design']):
        return "设计与UX"

    return "其他"

cats = defaultdict(list)
for f in merged:
    cats[categorize(f['text'], f['xmlUrl'])].append(f)

cat_order = ["AI专题", "大厂技术博客", "技术社区", "科技媒体", "技术周刊", "学术论文", "微信公众号", "设计与UX", "其他"]

# Generate OPML
opml = ET.Element('opml', version='2.0')
head = ET.SubElement(opml, 'head')
ET.SubElement(head, 'title').text = 'Merged RSS Feeds - AI/Tech Research'
ET.SubElement(head, 'dateCreated').text = str(date.today())
body = ET.SubElement(opml, 'body')

for cat_name in cat_order:
    if cat_name not in cats:
        continue
    feeds = sorted(cats[cat_name], key=lambda x: x['text'].lower())
    cat_outline = ET.SubElement(body, 'outline', text=cat_name, title=cat_name)
    for f in feeds:
        ET.SubElement(cat_outline, 'outline', type='rss', text=f['text'], title=f['text'], xmlUrl=f['xmlUrl'])

tree = ET.ElementTree(opml)
ET.indent(tree, space='  ')
opml_path = 'docs/merged_feeds.opml'
tree.write(opml_path, encoding='utf-8', xml_declaration=True)
print(f"OPML written: {opml_path}")

# Generate Markdown
md_lines = [
    "# Merged RSS Feeds - AI/Tech Research",
    "",
    "> 合并自 BestBlogs_RSS_Articles.opml 和 feeds_my_fillter.opml",
    f"> 生成日期: {date.today()}",
    f"> 总计: {sum(len(v) for v in cats.values())} 个唯一订阅源, {len(cats)} 个分类",
    "",
]

for cat_name in cat_order:
    if cat_name not in cats:
        continue
    feeds = sorted(cats[cat_name], key=lambda x: x['text'].lower())
    md_lines.append(f"## {cat_name} ({len(feeds)})")
    md_lines.append("")
    for f in feeds:
        md_lines.append(f"- [{f['text']}]({f['xmlUrl']})")
    md_lines.append("")

md_path = 'docs/merged_feeds.md'
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Markdown written: {md_path}")

# Print stats
for cat_name in cat_order:
    if cat_name in cats:
        print(f"  {cat_name}: {len(cats[cat_name])}")
print(f"  Total: {sum(len(v) for v in cats.values())}")

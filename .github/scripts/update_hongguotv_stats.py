#!/usr/bin/env python3
import json, os, urllib.request, datetime, pathlib, html, math
OWNER, REPO = "xycvip", "AppDownload"
ROOT = pathlib.Path("."); STATS = ROOT / "stats"; STATS.mkdir(exist_ok=True)
HISTORY_FILE, README_FILE = STATS / "history.json", ROOT / "README.md"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
TOKEN, TRAFFIC_TOKEN = os.environ.get("GITHUB_TOKEN",""), os.environ.get("TRAFFIC_TOKEN","")
TODAY = datetime.datetime.now(datetime.timezone.utc).date().isoformat()

def get(url, token=TOKEN):
    h={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"AppDownload-stats"}
    if token: h["Authorization"]="Bearer "+token
    with urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=30) as r:
        return json.loads(r.read().decode())

history=json.loads(HISTORY_FILE.read_text()) if HISTORY_FILE.exists() else {"days":[],"release_downloads":{}}
days={x["date"]:x for x in history.get("days",[])}
counts={}; releases=[]
for page in range(1,11):
    batch=get(f"{API}/releases?per_page=100&page={page}")
    if not batch: break
    for rel in batch:
        tag=rel.get("tag_name","")
        if rel.get("draft") or not tag.startswith("hongguotv-v"): continue
        n=sum(int(a.get("download_count",0)) for a in rel.get("assets",[])
              if a.get("name","").lower().startswith("hongguotv-") and a.get("name","").lower().endswith(".apk"))
        counts[tag]=n
        releases.append({"tag":tag,"name":rel.get("name") or tag,"downloads":n,"published_at":rel.get("published_at") or ""})
    if len(batch)<100: break

previous=history.get("release_downloads",{})
delta=sum(max(0,n-int(previous.get(tag,n))) for tag,n in counts.items())
today=days.get(TODAY,{"date":TODAY,"downloads":0,"views":0,"uniques":0})
today["downloads"]=int(today.get("downloads",0))+delta
today["download_total"]=sum(counts.values())

if TRAFFIC_TOKEN:
    try:
        traffic=get(API+"/traffic/views?per=day",TRAFFIC_TOKEN)
        for item in traffic.get("views",[]):
            date=item.get("timestamp","")[:10]
            if date:
                row=days.get(date,{"date":date,"downloads":0,"views":0,"uniques":0})
                row["views"]=int(item.get("count",0)); row["uniques"]=int(item.get("uniques",0))
                days[date]=row
    except Exception as e:
        print(f"::warning::Traffic API unavailable; retaining prior history: {e}")
else:
    print("::warning::TRAFFIC_TOKEN 未配置，浏览量曲线暂不更新；下载统计正常运行。")
days[TODAY]=today
ordered=sorted(days.values(),key=lambda x:x["date"])
history={"updated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
         "days":ordered,"release_downloads":counts,
         "release_rows":sorted(releases,key=lambda x:x["published_at"],reverse=True)}
HISTORY_FILE.write_text(json.dumps(history,ensure_ascii=False,indent=2)+"\n")

def chart(filename,title,series):
    data=ordered[-90:]; W,H=900,330; L,R,T,B=65,24,52,48; pw,ph=W-L-R,H-T-B
    vals=[float(row.get(k,0)) for row in data for k,_ in series]; mx=max(vals or [1]) or 1
    p=10**math.floor(math.log10(mx)); ymax=math.ceil(mx/p*1.15)*p
    colors=["#2563eb","#16a34a"]
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" rx="14" fill="#fff"/>',
         f'<text x="{L}" y="29" font-size="19" font-weight="700" fill="#111827">{html.escape(title)}</text>']
    for i in range(5):
        y=T+ph*i/4; v=ymax*(1-i/4)
        out += [f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#e5e7eb"/>',
                f'<text x="{L-10}" y="{y+4:.1f}" font-size="11" text-anchor="end" fill="#6b7280">{v:.0f}</text>']
    for si,(key,label) in enumerate(series):
        pts=[]
        for i,row in enumerate(data):
            x=L+pw*i/max(1,len(data)-1); y=T+ph*(1-float(row.get(key,0))/ymax)
            pts.append(f"{x:.1f},{y:.1f}")
        if pts: out.append(f'<polyline fill="none" stroke="{colors[si]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" points="{" ".join(pts)}"/>')
        lx=L+si*190
        out += [f'<line x1="{lx}" y1="{H-15}" x2="{lx+22}" y2="{H-15}" stroke="{colors[si]}" stroke-width="3"/>',
                f'<text x="{lx+29}" y="{H-11}" font-size="12" fill="#374151">{html.escape(label)}</text>']
    for i in range(0,len(data),max(1,len(data)//6)):
        x=L+pw*i/max(1,len(data)-1)
        out.append(f'<text x="{x:.1f}" y="{H-30}" font-size="10" text-anchor="middle" fill="#6b7280">{data[i]["date"][5:]}</text>')
    out.append("</svg>"); (STATS/filename).write_text("\n".join(out))

running=0
for row in ordered:
    running += int(row.get("downloads",0))
    row["cumulative_downloads"] = running
chart("downloads.svg","HongGuoTV APK downloads · last 90 days",[("downloads","Daily downloads"),("cumulative_downloads","Cumulative downloads")])
chart("traffic.svg","AppDownload repository views · last 90 days",[("views","Views"),("uniques","Unique visitors")])
total=sum(counts.values()); last7=sum(int(x.get("downloads",0)) for x in ordered[-7:])
last30=sum(int(x.get("downloads",0)) for x in ordered[-30:])
latest=releases[0]["name"] if releases else "暂无"
section="\n".join([
"<!-- HONGGUOTV_STATS_START -->","## 红果TV数据统计","",
f"> 更新时间：{history['updated_at'][:10]} UTC。仅统计红果TV正式版 Release 中的 HongGuoTV APK，不包含其他应用。","",
"| 指标 | 数据 |","| --- | ---: |",
f"| 红果TV APK 累计下载量 | **{total:,}** |",
f"| 最近 7 天下载量 | **{last7:,}** |",f"| 最近 30 天下载量 | **{last30:,}** |",
f"| 最新正式版 | **{html.escape(latest)}** |","",
"### 历史版本下载量","",
"| 版本 | APK 下载量 |",
"| --- | ---: |",
*([f"| {html.escape(x['name'])} | {int(x['downloads']):,} |" for x in history.get("release_rows",[])[:15]] or ["| 暂无历史版本数据 | — |"]),
"",
"### 每日 APK 下载趋势（最近 90 天）","",
"![红果TV每日APK下载趋势](stats/downloads.svg)","",
"### 仓库浏览量与独立访客（最近 90 天）","",
"![仓库访问趋势](stats/traffic.svg)","",
"浏览量和独立访客来自 GitHub Traffic API。GitHub 原始数据仅保留最近 14 天，工作流每天归档；启用前的历史访问数据无法补回。",
"首次启用访问统计前，请在仓库 Settings → Secrets and variables → Actions 中添加 TRAFFIC_TOKEN；该 Fine-grained PAT 需要对本仓库授予 Administration: Read-only 权限。未配置时下载统计仍会运行，但访问曲线不会更新。","",
"<!-- HONGGUOTV_STATS_END -->"])
readme=README_FILE.read_text(encoding="utf-8")
a,b="<!-- HONGGUOTV_STATS_START -->","<!-- HONGGUOTV_STATS_END -->"
if a in readme and b in readme:
    i,j=readme.index(a),readme.index(b)+len(b); readme=readme[:i]+section+readme[j:]
else:
    marker="## 最新版本"; pos=readme.find(marker)
    readme=readme[:pos]+section+"\n\n"+readme[pos:] if pos>=0 else readme.rstrip()+"\n\n"+section+"\n"
README_FILE.write_text(readme,encoding="utf-8")
print(f"HongGuoTV stats updated: total={total}, daily_delta={delta}, history_days={len(ordered)}")

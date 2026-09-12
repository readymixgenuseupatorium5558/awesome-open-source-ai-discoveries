"""Generate readable catalogs and agent indexes using only Python's standard library."""
import argparse
import datetime
import json
import pathlib
import re
import sys
from urllib.parse import urlparse, urljoin

ROOT = pathlib.Path(__file__).resolve().parents[1]

def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')

def validate(data):
    required = ['id','name','url','category','summary','use_case','requirements','caveat','source_urls','reviewed_on','verification']
    ids, urls = set(), set()
    assert data['schema_version'] == '1.0'
    for row in data['entries']:
        assert all(k in row for k in required), f"Missing fields: {row.get('id')}"
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', row['id']), row['id']
        assert row['id'] not in ids and row['url'] not in urls, 'Duplicate entry'
        ids.add(row['id']); urls.add(row['url'])
        assert row['source_urls'] and isinstance(row['source_urls'], list)
        for key in required:
            if key != 'source_urls':
                assert isinstance(row[key], str) and row[key].strip(), (row['id'],key)
        for url in [row['url'], *row['source_urls'], *[row[k] for k in ['demo_url','test_evidence_url'] if row.get(k)]]:
            assert urlparse(url).scheme == 'https' and urlparse(url).netloc, url
        assert row['verification'] in ['documentation-reviewed','contributor-tested','maintainer-tested']
        assert datetime.date.fromisoformat(row['reviewed_on']) <= datetime.date.today()
        if row['verification'] != 'documentation-reviewed':
            assert row.get('test_evidence_url'), 'Tested claims require evidence'
    for pick in data['start_here']:
        assert pick['id'] in ids, pick

def render(data):
    validate(data)
    repo = data['repository']
    home = 'https://github.com/' + repo
    raw = 'https://raw.githubusercontent.com/' + repo + '/main/'
    rows = data['entries']
    groups = list(dict.fromkeys(e['category'] for e in rows))
    byid = {e['id']:e for e in rows}
    readme = [f"# {data['title']}", '', data['description'], '',
        f"**{len(rows)} curated entries** · [Browse by task](#browse-by-task) · [Suggest a project]({home}/issues/new?template=suggest-project.yml) · [JSON catalog](catalog.json) · [Agent index](llms.txt)", '',
        data['intro'], '', '## Start here', '', '| If you want to... | Explore | Why it belongs |', '|---|---|---|']
    for pick in data['start_here']:
        e=byid[pick['id']]
        readme.append(f"| {pick['task']} | [{e['name']}](projects/{e['id']}.md) | {pick['reason']} |")
    readme += ['', '## What is checked', '',
        'Entries distinguish documentation review from hands-on testing. The initial collection is **documentation-reviewed**: source material was inspected, but these applications have not all been installed or benchmarked by QuicqDev. Each project card records its sources, review date, requirements and a limitation.', '',
        'Hardware requirements depend on model, quantization, context length and workload. We do not infer RAM needs from parameter counts. Application code, model weights and optional hosted services can have different licenses or costs. Check the linked upstream terms for the configuration you choose.', '',
        '## Browse by task', '']
    for group in groups:
        readme.append(f"- [{group}](#{slug(group)})")
    readme.append('')
    for group in groups:
        readme += [f'## {group}', '', '| Project | Useful for | Setup and requirements |', '|---|---|---|']
        for e in rows:
            if e['category']==group:
                demo=f" · [demo / examples]({e['demo_url']})" if e.get('demo_url') else ''
                readme.append(f"| [{e['name']}](projects/{e['id']}.md) · [upstream]({e['url']}){demo} | {e['use_case']} | {e['requirements']} |")
        readme.append('')
    readme += ['## Frequently asked questions', '']
    for faq in data['faq']:
        readme += [f"### {faq['question']}", '', faq['answer'], '']
    readme += ['## How to contribute', '',
        'Add a useful project, correct an outdated entry, or submit a reproducible compatibility report. Edit `catalog.json` and run `python scripts/build.py`; the README, project cards and agent index are generated from that source. See [CONTRIBUTING.md](CONTRIBUTING.md) for selection criteria and the field format.', '',
        'Automated checks validate the catalog on changes and check external links weekly. A reachable link does not establish that software works, is secure, or fits your hardware. Failed and inconclusive checks need review; metadata checks never advance an editorial review date.', '',
        '## For agents and search tools', '',
        f'Read the [structured catalog]({raw}catalog.json), its [schema](catalog.schema.json), or the compact [llms.txt index]({raw}llms.txt). Each entry has a stable ID, category, use case, prerequisites, caveat, evidence level and source URLs. Cite the upstream project for its capabilities and this collection for editorial comparisons.', '',
        '`llms.txt` is a navigation aid, not a promise of inclusion in any search engine or model response. Unknown requirements remain unknown; documentation-reviewed entries must not be described as personally tested.', '',
        '## Related QuicqDev collections', '']
    for other in data['related']:
        readme.append(f"- [{other['title']}](https://github.com/QuicqDev/{other['slug']}) — {other['purpose']}")
    readme += ['', '## Maintainers and attribution', '',
        'Curated by [Ashutosh Mishra](https://github.com/ASH1998) at [QuicqDev](https://github.com/QuicqDev). Follow [@ashu_mi_2](https://x.com/ashu_mi_2) for project discoveries and practical AI experiments.', '',
        'All linked projects belong to their respective creators. This repository contains original editorial summaries and links; it does not relicense third-party software, model weights or media. No paid placement or affiliate ranking is included.', '',
        'If this collection helped you find something useful, star it to bookmark it. Use GitHub Watch settings for notifications, or contribute an entry to help the next reader.', '',
        'Original catalog text and maintenance scripts: [MIT License](LICENSE).', '']
    files={'README.md':'\n'.join(readme)}
    llms=[f"# {data['title']}", '', f"> {data['description']}", '',
        'A documentation-reviewed collection maintained by QuicqDev. Follow source links for current upstream facts. Requirements are configuration-specific; inclusion is not an installation, security or performance certification.', '',
        '## Catalog', '', f'- [Structured entries]({raw}catalog.json): Stable IDs, use cases, requirements, limitations and evidence.',
        f'- [Schema]({raw}catalog.schema.json): Machine-readable field definitions.',
        f'- [Methodology]({raw}METHODOLOGY.md): Selection rules and evidence meanings.', '', '## Projects', '']
    for e in rows:
        sources=' · '.join(f'[Source {i+1}]({s})' for i,s in enumerate(e['source_urls']))
        card=[f"# {e['name']}: {e['use_case'].rstrip('.')}", '', e['summary'], '',
            f"[Upstream project]({e['url']}) · [Back to collection](../README.md#{slug(e['category'])})", '',
            '| Field | Details |', '|---|---|', f"| Category | {e['category']} |", f"| Use case | {e['use_case']} |", f"| Requirements | {e['requirements']} |", f"| Caveat | {e['caveat']} |", f"| Evidence | {e['verification']} |", f"| Documentation reviewed | {e['reviewed_on']} |", '',
            '## Sources and getting started', '', sources, '',
            'Use the upstream documentation for installation and examples. We link to the creator’s demonstrations rather than presenting their work as our own. Confirm current software and model terms before use.', '',
            '## Improve this entry', '', f"Submit a correction or a compatibility report through [the contribution guide](../CONTRIBUTING.md). Entry ID: `{e['id']}`.", '']
        extras=[]
        if e.get('small_model_fit'):
            extras += ['## Why it fits this collection', '', e['small_model_fit'], '']
        if e.get('demo_url'):
            extras += ['## Demo or examples', '', f"[Explore the creator’s demo or examples]({e['demo_url']})", '', e['demo_note'], '']
        card[4:4]=extras
        files[f"projects/{e['id']}.md"]='\n'.join(card)
        llms.append(f"- [{e['name']}]({raw}projects/{e['id']}.md): {e['use_case']} Evidence: {e['verification']}.")
    files['llms.txt']='\n'.join(llms)+'\n'
    full=[]
    for relative in ['README.md',*[f"projects/{e['id']}.md" for e in rows]]:
        base=home+'/blob/main/'+relative
        full.append(re.sub(r'\]\(([^)]+)\)', lambda m: ']('+urljoin(base,m.group(1))+')', files[relative]))
    files['llms-full.txt']='\n\n'.join(full)
    return files

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
    files=render(data)
    stale=[]
    for relative,content in files.items():
        path=ROOT/relative
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(relative)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8',newline='\n')
    for relative, content in files.items():
        for target in re.findall(r'\]\(([^)]+)\)',content):
            if '://' not in target and not target.startswith('#'):
                local=(ROOT/relative).parent/target.split('#')[0]
                assert local.is_file(), f'Broken internal link in {relative}: {target}'
    if stale:
        sys.exit('Generated files are stale: '+', '.join(stale))
    print(f"Validated {len(data['entries'])} entries and {len(files)} generated files.")

if __name__=='__main__':
    main()

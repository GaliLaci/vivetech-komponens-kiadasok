"""A kötött kiadási fájlokból épít HTTPS-futárt, tartalom- és méretellenőrzéssel."""
import hashlib
import json
from pathlib import Path
import re
import shutil


root = Path(__file__).resolve().parent
site = root / '_site'
site.mkdir(exist_ok=False)
for name in ('catalog.json', 'catalog.json.sig'):
    shutil.copyfile(root / name, site / name)

for release in sorted((root / 'releases').iterdir()):
    if not release.is_dir() or not re.fullmatch(r'[a-z0-9.-]+', release.name):
        raise ValueError('Hibás kiadási könyvtár.')
    manifest = json.loads((release / 'manifest.json').read_text())
    target = site / 'releases' / release.name
    target.mkdir(parents=True)
    for name in ('manifest.json', 'manifest.sig'):
        shutil.copyfile(release / name, target / name)
    for artifact in manifest['artifacts']:
        name = artifact['name']
        if name not in ('image.tar', 'assets.tar'):
            raise ValueError('Nem engedélyezett csomagfájl.')
        source = release / name
        files = [source] if source.is_file() else sorted((release / (name + '.parts')).iterdir())
        if not source.is_file() and [p.name for p in files] != [f'{i:03d}' for i in range(len(files))]:
            raise ValueError('Hiányzó vagy hibás csomagrész.')
        digest, size = hashlib.sha256(), 0
        with (target / name).open('xb') as output:
            for part in files:
                if part.is_symlink() or not part.is_file():
                    raise ValueError('Nem reguláris csomagrész.')
                with part.open('rb') as stream:
                    while data := stream.read(1024 * 1024):
                        size += len(data)
                        if size > artifact['size']:
                            raise ValueError('Túl nagy csomagfájl.')
                        output.write(data)
                        digest.update(data)
        if size != artifact['size'] or digest.hexdigest() != artifact['sha256']:
            raise ValueError('A csomag nem egyezik a jegyzékkel.')
(site / '.nojekyll').write_text('')
(site / 'index.html').write_text('<!doctype html><html lang="hu"><meta charset="utf-8"><title>ViVeTech komponenskiadások</title><h1>ViVeTech aláírt komponenskiadások</h1><p>Az AI Box Névjegy felületéről telepíthető kiadások HTTPS-futára.</p><a href="catalog.json">Aláírt katalógus</a></html>')
print(json.dumps({'built': True, 'files': len(list(site.rglob('*')))}))

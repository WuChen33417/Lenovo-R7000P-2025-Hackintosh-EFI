#!/usr/bin/env python3
"""Read-only structural and checksum checks; this is not a boot/runtime test."""
from pathlib import Path
import hashlib
import plistlib

root = Path(__file__).resolve().parents[1]
oc = root / 'EFI' / 'OC'
config = plistlib.loads((oc / 'config.plist').read_bytes())
generic = config['PlatformInfo']['Generic']
assert generic['SystemSerialNumber'] == '', 'Public snapshot contains a serial number'
assert generic['MLB'] == '', 'Public snapshot contains an MLB'
assert generic['SystemUUID'] == '00000000-0000-0000-0000-000000000000'
assert generic['ROM'] == bytes(6)

def require(base, relative):
    target = base / relative
    assert target.resolve().is_relative_to(base.resolve()), f'Unexpected path: {relative}'
    assert target.is_file(), f'Missing: {target.relative_to(root)}'

for entry in config['ACPI']['Add']:
    if entry['Enabled']:
        require(oc / 'ACPI', entry['Path'])
for entry in config['UEFI']['Drivers']:
    if entry['Enabled']:
        require(oc / 'Drivers', entry['Path'])
for entry in config['Kernel']['Add']:
    if entry['Enabled']:
        bundle = oc / 'Kexts' / entry['BundlePath']
        require(bundle, entry['PlistPath'])
        if entry['ExecutablePath']:
            require(bundle, entry['ExecutablePath'])
count = 0
for line in (root / 'EFI-SHA256SUMS.txt').read_text().splitlines():
    expected, name = line.split('  ', 1)
    path = root / name
    assert path.resolve().is_relative_to((root / 'EFI').resolve())
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f'Hash mismatch: {name}'
    count += 1
assert count == sum(p.is_file() for p in (root / 'EFI').rglob('*')), 'Manifest does not cover all files'
print(f'PASS: public identity placeholders, enabled paths, {count} EFI checksums')
print('Not a boot test or full runtime validation.')

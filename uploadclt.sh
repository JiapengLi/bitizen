#!/bin/bash

scp -i /d/keys/beauty/id_ed25519 -R \
cmp_keyshare_a.txt \
cmp_keyshare_b.txt \
frost_keyshare_a.txt \
frost_keyshare_b.txt \
keyshare_a.txt \
keyshare_b.txt \
libmulti_party_sig_amd64.so \
libmulti_party_sig_arm64.so \
README.md \
test_client.py \
upload.sh \
ws_server.py \
beauty@192.168.192.6:/opt/bitizen

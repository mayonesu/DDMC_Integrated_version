!#/bin/sh

curl=`cat <<EOS
curl
 -OL
 https://ddmc.ddlc-jp.com/download/mod_data/latest.zip
  -o
 /dev/null
 -w
 '%{http_code}'
  -s
EOS`
eval ${curl}
#/usr/bin/sh

var="63 74 66 5A 65 72 6F 7B 4C 69 6E 75 73 5F 54 6F 72 76 61 6C 64 73 5F 4F 50 7D"
var="$(echo "$var" | tr -d ' ')"
var="$(tr 'A-Z' 'a-z' <<< $var)"
xxd -r -p - <<< $var

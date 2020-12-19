export f=2020day19input
#export f=test

awk -v RS= 'NR==2' $f > "$f.messages"
awk -v RS= 'NR==1' $f > "$f.rules"

cat "$f.rules" | grep -E "\"" > "$f.lexer"
cat "$f.rules" | grep -E -v "\"" > "$f.parser"

cat "$f.parser" | sort -n | sed -E -e "s@([0-9]+)@_\1@g" -e "s@\$@;@g" | sed 1d >> $f.y
echo "%%" >> $f.y

lex $f.l && yacc -d $f.y && cc lex.yy.c y.tab.c -o $f.out

for l in $(cat "$f.messages") ; do echo "$l" | ./$f.out ; done | grep -c success

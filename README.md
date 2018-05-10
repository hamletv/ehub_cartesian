# ehub_cartesian
Cartesian product from string parameter to simulate Bash

# How to run code:
Run code in terminal, string passed **must** be within quotes: '   ' or "   "

python bcehub.py "a{b,c}d{e,f,g}hi" <br/>
abdehi abdfhi abdghi acdehi acdfhi acdghi

python bcehub.py "a{b,c{d,e,f}g,h}ij{k,l}" <br/>
abijk abijl acdgijk acdgijl acegijk acegijl acfgijk acfgijl ahijk ahijl

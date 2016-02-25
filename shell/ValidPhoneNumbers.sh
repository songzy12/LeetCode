# grep: global search regular expression
# -P: --perl-regexp, PCRE
# grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# sed: stream editor
# -n: --quiet, --silent
# -r: --regexp-extended
# p: print
# sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt

# awk: grep to search, sed to edit, awk to analyse
# default action is to print matched lines
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/{print $0}' file.txt

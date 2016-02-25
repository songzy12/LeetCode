cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'
# tr -s: truncate the string with target string
# uniq -c: filter out the repeated lines which are successive

awk '{
    for (i = 1; i <= NF; i++) {
        ++D[$i]; # default value is 0
    } 
}END {
    for (i in D) {
        print i, D[i]
    }
}' words.txt | sort -nr -k 2

# sort -n: compare according to string numerical value
# sort -r: reverse the result of comparisons
# sort -k 2: sort by the second word

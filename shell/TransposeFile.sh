awk '
{
    # NF: number of field
    for (i = 1; i <= NF; i++) { 
        # NR: number of record, FNR: file number of record
        if (NR == 1) { 
            # $0 is the whole line
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i 
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt

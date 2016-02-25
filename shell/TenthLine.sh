N=$(cat file.txt|wc -l)
if [ $N -gt 9 ]; then
    head file.txt | tail -n 1
else
    echo
fi

echo "Starting at: $(date)"; echo; echo $uptime #You can include multiple commands on the same line using semicolons

#Using variables
example=hello
echo $example
line="-------------------------------------------"
echo $line

#Using globs
echo *.py #Outputs a list of all files that end with .py
echo P* #Outputs a list of all files that start with P
echo * #Outputs all files in the current working directory
echo ?????.py #Outpus all files whose filenames are made up of 5 characters (5 question marks)

#Using conditionals
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything OK"
else
    echo "ERROR"
fi

#Using the test command
if test -n "$PATH"; then echo "Your PATH variable is not empty"; fi #Checks if the given variable ($PATH) is empty
if [ -n "$PATH" ]; then echo "Your PATH variable is not empty"; fi #The square brackets are an alias to the test command


#Using while loops
n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

#Using FOR loops
for fruit in peach orange apple; do
    echo "I like fruit!"
done

for file in *.HTM; do
    name=$(basename "$file" .HTM) #Changes a file name to its basename (filename without extension) and then appending a new extension.
    mv "$file" "$name.html"
done

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5 #Formats logs nicely
done

student-01-45e97e6e6cfd@35.230.75.36
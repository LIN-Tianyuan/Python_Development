# Linux
## 1. Basic command

### 1.1 grep：Text Search

> "find all lines in a log file that contain the word 'error'"

```bash
grep "error" /var/log/syslog
```

✅ **Ideal for log analysis**

------

> "Search for 'error' but exclude lines containing 'debug'"

```bash
grep "error" /var/log/syslog | grep -v "debug"
```

✅ **Pipeline (`|`) filters unwanted content**

```bash
grep "error" app.log # search for "error" in the file
grep -i "error" app.log # Ignore case
grep -r "TODO" /home/user/ # Recursive search for directories
grep -o '[0-9]\+' file.txt # show only matching numbers
```

### 1.2. awk：Handle structured text

> "Extract the second column from a space-separated file"

```bash
awk '{print $2}' file.txt
```

✅ **Suitable for extracting data from specific columns**

------

> "Calculate the sum of the numbers in the second column?"

```bash
awk '{sum+=$2} END {print sum}' file.txt
```

✅ **Ideal for data analysis, such as counting the number of requests in a log.**

### 1.3 sed：Text replacement

> "Replace 'apple' with 'orange' in a file."

```bash
sed -i 's/apple/orange/g' file.txt
```

✅ **For batch text replacement**
```bash
sed 's/apple/banana/g' file.txt # replace "apple" with "banana"
sed '/^$/d' file.txt # Delete blank lines
sed -i 's/oldtext/newtext/g' file.txt # modify the file directly
```
 - s/old/new/g : replace text
 - -i : modify the file directly

### 1.4 ps：View Processes


> "Find the PID of a process named `nginx`."

```bash
ps aux | grep nginx
```

✅ **For finding processes**

### 1.5. top：Monitor system performance

> "Check which processes are consuming the most CPU?"


```bash
top
```

Or

```bash
ps aux --sort=-%cpu | head -10
```

✅ **For server performance monitoring**

### 1.6. netstat：View Network Connections


> "List all open ports on a system?"

```bash
netstat -tulnp
```

✅ **For checking server ports**

------

> "Check which process is using port 80?"

```bash
netstat -tulnp | grep ":80"
```

✅ **Ideal for troubleshooting occupied ports**

### 1.7 lsof：View Files and Ports

> "Check which process is using a specific file?"

```bash
lsof /var/log/syslog
```

✅ **For troubleshooting which process a file is occupied by**

------

> "Check which process is using port 3306 (MySQL)?"

```bash
lsof -i :3306
```

✅ **For network debugging**

### 1.8. tcpdump：capture network traffic


> "Capture all HTTP traffic on a network interface."


```bash
tcpdump -i eth0 port 80 -A
```

✅ **Ideal for capturing HTTP traffic**

------

> "Capture packets from a specific IP."

```bash
tcpdump -i eth0 src host 192.168.1.100
```

✅ **For analyzing traffic to specific IPs**

### 1.9. strace：Trace system calls


> "Trace system calls made by a process?"


```bash
strace -p 1234  # 1234 is process ID
```

✅ **Ideal for troubleshooting process issues, such as file access failures**

------


> "Trace all file system calls of a process?"


```bash
strace -e trace=open,read,write -p 1234
```

✅ **For debugging file IO related issues**

------

### **1.10 Summary**

| Commands    | Functions                  | Common Usage Scenarios             |
|-------------|----------------------------|------------------------------------|
| **grep**    | Text search                | Find errors in logs                |
| **awk**     | Process structured text    | Calculate sum of columns           |
| **sed**     | Text Replacement           | Modify Configuration File Contents |
| **ps**      | View Processes             | Find the PID of a process          |
| **top**     | Monitor system performance         | Find the process with the highest CPU usage | 
| **netstat** | Check network connectivity | Find all open ports                | 
| **lsof**    | List open files and ports  | Find processes on port 80          |
| **tcpdump** | Capture network traffic    | Analyze HTTP request traffic       |
| **strace**  | Trace system calls         | Debug file access failures         |

### 1.11 find: Find a file
```sql
find /var/log -name "*.log" # Find `.log` files
find /home -type f -mtime +7 # Find files modified 7 days ago.
find / -size +100M # Finds files larger than 100MB.
find . -type f -exec rm {} \; # Batch delete all files in current directory.
```
**`-mtime +7`** Files modified 7 days ago.

**`-size +100M`** Files larger than 100MB.

### 1.12 xargs: batch processing
```sql
find . -name "*.tmp" | xargs rm -f # Bulk delete .tmp files
ls *.log | xargs tar -czf logs.tar.gz # Batch compress log files
```
**`xargs`** Used to pass the output of the previous command to the next one.

## 2. Process management

### 2.1 fork vs exec

> "What is the difference between `fork()` and `exec()` in Linux?"

> `fork()` creates a new process (child process) which is a **copy** of the parent process. The child process inherits the parent process's **address space, file descriptors, signal handling** etc.

> ``exec()`` is used to **replace the process's address space** and load a new program, which does not create a new process but overwrites the current one."

#### **Code example（C language `fork + exec`）：**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();
    
    if (pid == 0) {  // Child process
        execl("/bin/ls", "ls", "-l", NULL);  // Replace processes with ls
    } else {  // Parent process
        wait(NULL);  // Wait child process to be finished
        printf("Child process finished.\n");
    }

    return 0;
}
```

✅ **Scenarios**: **Multi-process applications (e.g., Web servers, databases, distributed computing)**

### 2.2 vfork vs fork

> "What is the difference between `fork()` and `vfork()`?"


> "`vfork()` is an optimized version of `fork()` where the child process **shares the address space** with the parent process, and instead of copying the parent's address space, the child process **runs exec()** directly before the parent resumes execution."

✅ **`vfork()` is faster, but prone to problems (child processes may modify variables of the parent process).**

### 2.3 How to avoid zombie processes?

> "What is a zombie process? How do we prevent it?"

> "A Zombie Process is a process whose **child process terminates but is not reclaimed by the parent process**.The Linux kernel retains its **process ID (PID) and exit status**, resulting in a `<defunct>` process being displayed in `ps`."

#### **Avoidance methods:**

```
void sigchld_handler(int signum) {
    while (waitpid(-1, NULL, WNOHANG) > 0);  // Recycle all child processes
}
signal(SIGCHLD, sigchld_handler);
```

✅ **The parent process can listen to the `SIGCHLD` signal to automatically recycle child processes to avoid creating zombie processes.**

## 3. Signal processing (Signals)

### 3.1 How to terminate a process gracefully (handling SIGTERM)?

> "How do we handle `SIGTERM` properly in a process?"

> "We can trap `SIGTERM` signals and perform cleanup operations such as closing database connections and freeing resources when received."

#### **Sample code (Python implementation):**

```python
import signal
import sys
import time

def graceful_exit(signum, frame):
    print("Received SIGTERM. Cleaning up...")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_exit)  # Handle SIGTERM

while True:
    print("Running...")
    time.sleep(1)
```

✅ **For long-running processes such as web servers, daemons, etc.**

### 3.2 How do we make Ctrl+C (SIGINT) not terminate a process?

```python
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore SIGINT
print("Try pressing Ctrl+C...")
while True:
    pass
```

✅ **For CLI tools or highly available services**

## 4. Shell
if-else
```bash
# Check if the file exists
/bin/bash /bin/bash
if [ -f "/etc/passwd" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
```
 - **`-f`** Check for the existence of documents
```bash
#!/bin/bash
num=15
if [ "$num" -gt 10 ]; then
    echo "Greater than 10"
else
    echo "Less than or equal to 10"
fi
``` 
 - **`-gt`** denotes greater than

for loop

```bash
# Batch rename `.txt` files
#!/bin/bash
for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done
```
 - **`${file%.txt}`** Delete `.txt` Extension
```bash
# 
#!/bin/bash
for file in *.log; do
    gzip "$file"
done
```
 - **Batch compression of `.log` files**

`crontab`: timed task
```bash
crontab -e # Edit timed tasks
```
Execute `backup.sh` at 2am every day.
```bash
0 2 * * * /home/user/backup.sh
```
Execute `script.sh` every 5 minutes.
```bash
*/5 * * * * /home/user/script.sh
```
📌 **Format**: `minutes hours days months weeks orders`

How to batch delete `.log` files that are 7 days old?
```bash
find /var/log -name "*.log" -mtime +7 | xargs rm -f
```
How to automatically backup database at 3am every day?
```bash
crontab -e
0 3 * * * /home/user/backup.sh
```
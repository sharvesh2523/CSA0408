#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
int main(int c,char **v){
 if(c<3){printf("usage src dst\n");return 1;}
 int in=open(v[1],O_RDONLY),out=open(v[2],O_WRONLY|O_CREAT,0644);
 char buf[4096];ssize_t n;
 while((n=read(in,buf,sizeof buf))>0) write(out,buf,n);
 close(in);close(out);return 0;
}

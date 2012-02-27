#ifndef SENDRECVLOOP_H_
#define SENDRECVLOOP_H_

#ifdef WIN32
	#include <winsock2.h>
	#include <sys/types.h>
#else
	#include <unistd.h>
	#include <sys/socket.h>
#endif

int sendloop(int sockfd, const void *buf, size_t len, int flags);
int recvloop(int sockfd, void *buf, size_t len, int flags);

#endif /* SENDRECVLOOP_H_ */

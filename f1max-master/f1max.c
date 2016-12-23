#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NNODES 10000000 //max number of nodes: will increase if needed
#define NCOMS 10000000 //max number of communities: will increase if needed
#define SCOM 10000000 //max size of community: will increase if needed
#define NCPN 10 //max number of community per nodes: will increase if needed

typedef struct {
	unsigned s;//size of the community
	unsigned smax;//maximum size of the community
	unsigned *nodes;//nodes in the community
} community;

typedef struct {
	unsigned n;//number of nodes
	unsigned m;//max number of nodes

	unsigned **c;//c[i]=communities containing node i.
	unsigned *s;//s[i]=number of communities containing node i.
	unsigned *smax;//smax[i]=max number of communities

	unsigned nc;//number of communities
	unsigned mc;//max number of communities
	unsigned *size;//size[i]=size of the community i

	unsigned *tmp;//tmp[i] number of nodes shared by the current community and community i
	unsigned *list;//list of the community sharing at least one node with the current community
	unsigned nlist;//length of list
} compare;


compare *alloccompare(){
	compare *comp=malloc(sizeof(compare));
	comp->n=0;
	comp->m=NNODES;
	comp->c=calloc(comp->m,sizeof(unsigned*));
	comp->s=calloc(comp->m,sizeof(unsigned));
	comp->smax=calloc(comp->m,sizeof(unsigned));

	comp->nc=0;
	comp->mc=NCOMS;
	comp->size=malloc(comp->mc*sizeof(unsigned));

	comp->tmp=calloc(comp->mc,sizeof(unsigned));
	comp->list=calloc(comp->mc,sizeof(unsigned));
	comp->nlist=0;
	return comp;
}

community *alloccom(){
	community *com=malloc(sizeof(community));
	com->smax=SCOM;
	com->nodes=malloc(SCOM*sizeof(unsigned));
	return com;
}

bool readlinecom(FILE* file,community* com){
	char c;

	com->s=0;
	while(fscanf(file,"%u%c",com->nodes+com->s,&c)==2){
		if ( ++(com->s) == com->smax) {
			com->smax+=SCOM;
			com->nodes=realloc(com->nodes,com->smax*sizeof(unsigned));
		}
		if (c=='\n') {
			return 1;
		}
	}
	return 0;
}

void com2comp(community* com,compare* comp){
	unsigned i,j,tmp;

	if (comp->nc==comp->mc){
		comp->mc+=NCOMS;
		comp->size=realloc(comp->size,comp->mc*sizeof(unsigned));
		comp->tmp=realloc(comp->tmp,comp->mc*sizeof(unsigned));
		comp->list=realloc(comp->size,comp->mc*sizeof(unsigned));
		for (i=comp->mc-NCOMS;i<comp->mc;i++){
			comp->tmp[i]=0;
		}
	}
	comp->size[comp->nc]=com->s;
	for (i=0;i<com->s;i++){
		if (com->nodes[i]>comp->m){
			tmp=com->nodes[i]-comp->m+NCOMS;
			comp->m+=tmp;
			comp->c=realloc(comp->c,comp->m*sizeof(unsigned*));
			comp->s=realloc(comp->s,comp->m*sizeof(unsigned));
			comp->smax=realloc(comp->smax,comp->m*sizeof(unsigned));
			for (j=comp->m-tmp;j<comp->m;j++){
				comp->c[j]=NULL;
				comp->s[j]=0;
				comp->smax[j]=0;
			}
		}
		if (comp->s[com->nodes[i]]==comp->smax[com->nodes[i]]){
			if (comp->s[com->nodes[i]]==0){
				comp->c[com->nodes[i]]=malloc(NCPN*sizeof(unsigned));
				comp->smax[com->nodes[i]]=NCPN;
			}
			else {
				comp->smax[com->nodes[i]]+=NCPN;
				comp->c[com->nodes[i]]=realloc(comp->c[com->nodes[i]],comp->smax[com->nodes[i]]*sizeof(unsigned));
			}
		}
		comp->c[com->nodes[i]][comp->s[com->nodes[i]]++]=comp->nc;
	}
	comp->nc++;
}

double comsim(community* com,compare *comp){
	double sim=0,sim2;
	unsigned i,j;
	for (i=0;i<com->s;i++){
		for (j=0;j<comp->s[com->nodes[i]];j++){
			if (comp->tmp[comp->c[com->nodes[i]][j]]==0){
				comp->list[comp->nlist++]=comp->c[com->nodes[i]][j];
			}
			comp->tmp[comp->c[com->nodes[i]][j]]++;
		}
	}

	for (i=0;i<comp->nlist;i++){
		sim2=((double)(comp->tmp[comp->list[i]]))/(com->s+comp->size[comp->list[i]]);
		if (sim2>sim){
			sim=sim2;
		}
		comp->tmp[comp->list[i]]=0;
	}
	comp->nlist=0;
	return 2*sim;
}

int main(int argc,char** argv){

	unsigned ncom=0;
	double score=0;
	community *com=alloccom();
	compare *comp=alloccompare();
	FILE* file;

	file=fopen(argv[2],"r");
	while(readlinecom(file,com)){
		com2comp(com,comp);
	}
	fclose(file);

	file=fopen(argv[1],"r");
	while(readlinecom(file,com)){
		score+=comsim(com,comp);
		ncom++;
	}
	fclose(file);

	score/=(double)ncom;

	printf("%lf\n",score);

	return 0;
}

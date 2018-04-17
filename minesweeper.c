#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>

#define SIZE 10
#define NUM_BOMBS 20

char init = '.';
char mine = '*';
char flag = 'P';

void welcome();
char **initialize();
void clear(char **a);
void build(char **a);
void print(char **grid);
int count_mines(char **ar, int a, int b);
void reveal(char **fld, char **brd, int a, int b);
void flag_tile(char **brd, int a, int b);
void start(char **brd, char **fld);
void gameplay(char **brd, char **fld);
int count_correct_flags(char **brd, char **fld);

int main (void) {
	srand(time(NULL));
	setvbuf(stdout, NULL, _IONBF, 0);
	welcome();
	char **board; // user's board
	char **field; // field with hidden mines
	start(board, field);	
	return 0;
}

void welcome() {
	printf("------------------------------\n");
	printf("    Welcome to Minesweeper    \n");
	printf("------------------------------\n\n");
}

void start(char **brd, char **fld)  {
	brd = initialize();
	fld = initialize();
	build(fld);
	clear(brd);
	printf("Would you like to start the game? y/n\n");
	char input;
	input = getchar();
	if (input == 'y' || input == 'Y') {
		gameplay(brd, fld);
	} else if (input == 'n' || input == 'N') {
		printf("Exiting...\n");
	}
}

void gameplay(char **b, char **f) {
	char s0[15], s1[15], s2[15];
	int in[3];
	while(1) {
		print(b);
		printf("Please enter tile coordinate ([row] [colums] [option], where [optiot]: 0 - reveal tile, 1 - flag): ");		
		scanf("%s %s %s", s0, s1, s2);
		in[0] = atoi(s0);
		in[1] = atoi(s1);
		in[2] = atoi(s2);
		if (!(in[0] > 0 && in[0] < 9 && in[1] > 0 && in[1] < 9 && in[2] >= 0 && in[2] <= 1)) {
			printf("Wrong input. Try again.\n");
			continue;
		} else {
			puts("");
			if (in[2] == 0) {
				if (f[in[0]][in[1]] == mine) {
					for (int i = 1; i < SIZE-1; i++) 
						for (int j = 1; j < SIZE-1; j++) 
							if (f[i][j] == mine) b[i][j] = mine;
					print(b);
					printf("You lost!\n");
					return;
				}
				reveal(f, b, in[0], in[1]);
			} else {
				flag_tile(b, in[0], in[1]);
			}
		}
		if (count_correct_flags(b, f) == NUM_BOMBS) {
			for (int i = 1; i < SIZE-1; i++) 
				for (int j = 1; j < SIZE-1; j++) 
					if (f[i][j] == mine) f[i][j] = flag;
			print(f);
			printf("You won!\n");
			return;
		}
	}
}

char **initialize() {
	char **a = calloc(SIZE, sizeof(char *));
	for (int i = 0; i < SIZE; i++) 
		a[i] = calloc(SIZE, sizeof(char));
	return a;
}

void clear(char **a) {
	for (int i = 0; i < SIZE; i++)
		for (int j = 0; j < SIZE; j++) {
			a[i][j] = init;
		}
}

void build(char **a) {
	clear(a);
	int pos[NUM_BOMBS];
	for (int i = 0; i < NUM_BOMBS; i++) {
		pos[i] = rand()%((SIZE-2)*(SIZE-2));
		for (int j = 0; j < i; j++) {
			if (pos[i] == pos[j]) {
				i--;
				break;
			}
		}
	}
	for (int i = 0; i < NUM_BOMBS; i++) 
		a[pos[i]%(SIZE-2)+1][pos[i]/(SIZE-2)+1] = mine;
	for (int i = 1; i < SIZE-1; i++) 
		for (int j = 1; j < SIZE-1; j++) 
			if (a[i][j] != mine)
				a[i][j] = (char) (((int)'0') + count_mines(a, i, j));
}

void print(char **grid) {
	printf("    1 2 3 4 5 6 7 8\n");
	printf("    ---------------\n");
	for (int i = 1; i < SIZE-1; i++) {
		printf("%i | ", i);
		for (int  j = 1; j < SIZE-1; j++) {
			putchar(grid[i][j]);
			putchar(' ');
		}
		puts("|");
	}
	printf("    ---------------\n\n");
}

int count_mines(char **ar, int a, int b) {
	int count = 0;
	for (int i = 0; i < 3; i++) {
		if (ar[a-1][b+i-1] == mine)
			count++;
		if (ar[a+1][b+i-1] == mine) 
			count++;
	}
	if (ar[a][b-1] == mine) count++;
	if (ar[a][b+1] == mine) count++;
	return count;
}

void reveal(char **fld, char **brd, int a, int b) {
	if (a < 1 || a >= SIZE-1) return;
	if (b < 1 || b >= SIZE-1) return;
	
	if (brd[a][b] - '0' >= 0 && brd[a][b] - '0' < 9) return;
	if (brd[a][b] == flag) return;
	
	if (brd[a][b] == mine) {
		return;
	} else {
		brd[a][b] = fld[a][b];
		if (brd[a][b] - '0' == 0) {
			reveal(fld, brd, a-1, b-1);
			reveal(fld, brd, a-1, b  );
			reveal(fld, brd, a-1, b+1);
			reveal(fld, brd, a+1, b-1);
			reveal(fld, brd, a+1, b  );
			reveal(fld, brd, a+1, b+1);
			reveal(fld, brd, a  , b-1);
			reveal(fld, brd, a  , b+1);
		}
	}
}

void flag_tile(char **brd, int a, int b) {
	if (brd[a][b] == flag) { 
		brd[a][b] = init;
	} else if (brd[a][b] == init) {
		brd[a][b] = flag;
	}
}

int count_correct_flags(char **brd, char **fld) {
	int count = 0;
	for (int i = 1; i < SIZE-1; i++)
		for (int j = 1; j < SIZE-1; j++)
			if (brd[i][j] == flag && fld[i][j] == mine)
				count++;
	return count;
}
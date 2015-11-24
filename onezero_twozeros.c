#include <stdio.h>

struct CalcParams {
	int zeros;
	int limit;
};

int count_zeros(int number){
	int zero_total=0;
	while (number > 0){
		if ((number % 2) == 0){
			zero_total ++;
		}
		number = number / 2;
	}
	return zero_total;
}

int calculate(struct CalcParams params){
	int zeros, i, total=0;
	for (i=0; i <= params.limit; i++){
		zeros = count_zeros(i);
		if (zeros == params.zeros){
			total ++;
		}
	}
	return total;
}

struct CalcParams read_input(char *line) {
	char chzero[10], chlimit[10];
	struct CalcParams params;
	int zeros, limit, i, j;
	for (i=0; line[i] != ' '; i++){
		chzero[i] = line[i];
	}
	params.zeros = atoi(chzero);
	i ++;
	for (j=i; line[j] != '\0'; j++){
		chlimit[j-i] = line[j];
	}
	params.limit = atoi(chlimit);

	return params;
}


int main(int argc, const char * argv[]) {
	FILE *file = fopen(argv[1], "r");
	char line[1024];
	struct CalcParams input;
	int total;
	while (fgets(line, 1024, file)) {
		input = read_input(line);
		total = calculate(input);
		printf("%d\n",total);
	}
	return 0;
} 

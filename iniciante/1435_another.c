#include <stdio.h>

int main(){

    int size;
    int matriz[100][100];
    int half = 0;

    scanf("%d", &size);

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            matriz[i][j] = 1;
        }
    }

    if(size % 2 == 0){
        half = size / 2;
    }else{
        half = (size + 1 ) / 2;
    }

    for(int i = 1; i < half; i++){
        for(int j = 1; j < size - 1; j++){
            matriz[i][j] = matriz[i - 1][j - 1] + 1;
        }
    }

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}
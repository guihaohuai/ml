#include <string.h>
#include <stdio.h>
void score(double * input, double * output) {
    double var0[2];
    if (input[2] <= 0.5) {
        if (input[3] <= 0.5) {
            if (input[0] <= -1.502433717250824) {
                if (input[12] <= 0.5) {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                } else {
                    memcpy(var0, (double[]){0.9333333333333333, 0.06666666666666667}, 2 * sizeof(double));
                }
            } else {
                if (input[0] <= 0.20838219672441483) {
                    if (input[0] <= 0.13852711766958237) {
                        memcpy(var0, (double[]){0.8861209964412812, 0.11387900355871886}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.5, 0.5}, 2 * sizeof(double));
                    }
                } else {
                    if (input[14] <= 0.5) {
                        memcpy(var0, (double[]){1.0, 0.0}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.9270833333333334, 0.07291666666666667}, 2 * sizeof(double));
                    }
                }
            }
        } else {
            if (input[0] <= 1.7657992243766785) {
                if (input[0] <= 0.5066370815038681) {
                    if (input[10] <= 0.5) {
                        memcpy(var0, (double[]){0.56, 0.44}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.2857142857142857, 0.7142857142857143}, 2 * sizeof(double));
                    }
                } else {
                    if (input[0] <= 1.3251474499702454) {
                        memcpy(var0, (double[]){0.7692307692307693, 0.23076923076923078}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.4444444444444444, 0.5555555555555556}, 2 * sizeof(double));
                    }
                }
            } else {
                memcpy(var0, (double[]){0.875, 0.125}, 2 * sizeof(double));
            }
        }
    } else {
        if (input[5] <= 0.5) {
            if (input[9] <= 0.5) {
                if (input[0] <= -0.4606933146715164) {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                } else {
                    if (input[0] <= -0.16305319219827652) {
                        memcpy(var0, (double[]){0.21428571428571427, 0.7857142857142857}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.08333333333333333, 0.9166666666666666}, 2 * sizeof(double));
                    }
                }
            } else {
                if (input[0] <= -0.3418852984905243) {
                    if (input[7] <= 0.5) {
                        memcpy(var0, (double[]){0.14285714285714285, 0.8571428571428571}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                    }
                } else {
                    memcpy(var0, (double[]){0.0, 1.0}, 2 * sizeof(double));
                }
            }
        } else {
            if (input[12] <= 0.5) {
                if (input[0] <= -1.601027011871338) {
                    memcpy(var0, (double[]){0.08333333333333333, 0.9166666666666666}, 2 * sizeof(double));
                } else {
                    if (input[8] <= 0.5) {
                        memcpy(var0, (double[]){0.5342465753424658, 0.4657534246575342}, 2 * sizeof(double));
                    } else {
                        memcpy(var0, (double[]){0.25, 0.75}, 2 * sizeof(double));
                    }
                }
            } else {
                if (input[0] <= -0.981563538312912) {
                    memcpy(var0, (double[]){0.9411764705882353, 0.058823529411764705}, 2 * sizeof(double));
                } else {
                    memcpy(var0, (double[]){0.8, 0.2}, 2 * sizeof(double));
                }
            }
        }
    }
    memcpy(output, var0, 2 * sizeof(double));
}


int main(){
    double features[1][15] = {{0.393645337, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0 }};
    //-0.427001517	1	0	0	0	1	0	0	1	0	0	1	0	0	1---0   √
    //-1.688458828	1	0	0	0	1	1	0	0	0	1	0	1	0	0---0   √
    //0.393645337	0	1	0	0	1	0	0	1	0	0	1	0	0	1---1   √
    double output; 
    score(&features,&output);
    //double var0[2];
    //memcpy(var0, (double[]){0.5342465753424658, 0.4657534246575342}, 2 * sizeof(double));
    //memcpy(&output, var0, 2 * sizeof(double));
	//printf("%f",output);
    //可以注意到所有上述结构都是两个概率！因为加和为1，所以应该是大于0.5就可以归类。该方法测试下来比较靠谱
    printf("\n");
    //printf()
    printf("\n");
    if(output>=0.5){
        printf("predict:\t0");
    }else{
        printf("predict:\t1");
    }
    return 0;
}


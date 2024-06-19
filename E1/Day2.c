#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024
#define MAX_ROWS 1000
#define MAX_COLS 10

typedef struct {
    double r;
    double z;
    double Er;
    double Ez;
    double p;
    double E_multiplier;
    double K;
    double total_distance;
} DataRow;

double alpha(double E, double p) {
    p *= 133.322;
    E *= 1000;
    if (E / p < 31.6) {
        return 0;
    } else if (31.6 <= E / p && E / p < 60.0) {
        return (p / 10000) * (1.047 * (E / p - 28.5) * (E / p - 28.5) - 12.6);
    } else if (60.0 <= E / p && E / p < 100.0) {
        return (1.0 - 0.00674755 * (E / p - 60.0)) * (p / 10000) * (1.047 * (E / p - 28.5) * (E / p - 28.5) - 12.6);
    } else {
        return 15.0 * p * exp(-365 / (E / p));
    }
}

void calculate_K(DataRow* data, int row_count, double E_multiplier, double p) {
    double K = 0;
    for (int i = 0; i < row_count - 1; ++i) {
        double r1 = data[i].r, r2 = data[i + 1].r;
        double z1 = data[i].z, z2 = data[i + 1].z;
        double Er = data[i].Er;
        double Ez = data[i].Ez;
        double E = sqrt(Er * Er + Ez * Ez) * E_multiplier;
        double d = sqrt((r2 - r1) * (r2 - r1) + (z2 - z1) * (z2 - z1));
        K += alpha(E, p) * d;
    }
    for (int i = 0; i < row_count; ++i) {
        data[i].K = K;
        data[i].E_multiplier = E_multiplier;
        data[i].p = p;
    }
}

void read_csv(const char* filename, DataRow data[MAX_ROWS], int* row_count) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Could not open file %s for reading\n", filename);
        exit(EXIT_FAILURE);
    }

    char line[MAX_LINE_LENGTH];
    int row = 0;
    while (fgets(line, sizeof(line), file)) {
        if (row == 0) {
            // Skip header
            row++;
            continue;
        }
        sscanf(line, "%lf,%lf,%lf,%lf",
               &data[row - 1].r, &data[row - 1].z,
               &data[row - 1].Er, &data[row - 1].Ez);
        row++;
    }
    *row_count = row - 1;
    fclose(file);
}

void write_csv(const char* filename, DataRow* data, int row_count) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        fprintf(stderr, "Could not open file %s for writing\n", filename);
        exit(EXIT_FAILURE);
    }

    fprintf(file, "r,z,Er,Ez,p,E_multiplier,K,total_distance\n");
    for (int i = 0; i < row_count; ++i) {
        fprintf(file, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf\n",
                data[i].r, data[i].z, data[i].Er, data[i].Ez,
                data[i].p, data[i].E_multiplier, data[i].K, data[i].total_distance);
    }
    fclose(file);
}

int main() {
    DataRow data[MAX_ROWS];
    int row_count;

    read_csv("gap0_5.csv", data, &row_count);

    double E_multipliers[] = {0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0};
    double p_values[] = {0.01, 0.1, 0.5, 1.0, 2.0, 5.0};
    int num_E_multipliers = sizeof(E_multipliers) / sizeof(E_multipliers[0]);
    int num_p_values = sizeof(p_values) / sizeof(p_values[0]);

    for (int i = 0; i < num_E_multipliers; ++i) {
        for (int j = 0; j < num_p_values; ++j) {
            calculate_K(data, row_count, E_multipliers[i], p_values[j]);
        }
    }

    write_csv("results.csv", data, row_count);

    return 0;
}

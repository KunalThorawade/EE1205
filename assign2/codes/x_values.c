#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("result.dat", "w");

    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    // Print header
    fprintf(file, "Years (n)\tAmount\n");

    for (int n = 0; n <= 10; ++n) {
        double amount = 550 * pow(1.1, n);
        fprintf(file, "%d\t\t%.2f\n", n, amount);
    }

    fclose(file);

    return 0;
}

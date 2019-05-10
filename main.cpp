#include <iostream>

int main()
{
    std::cout << "Enter a natural number: ";

    unsigned int N;

    std::cin >> N;

    std::cout << "The number " << N << " can be present by next three summands:\n";

    unsigned int limit_1_summand = (N / 3) + 1;
    unsigned int limit_2_summand;

    for (unsigned int i = 0; i < limit_1_summand; i++) {

        limit_2_summand = ((N - i) / 2) + 1;

        for (unsigned int j = i; j < limit_2_summand; j++) {

            std::cout << i << " " << j << " " << N - i - j << std::endl;

        }
    }

    std::cin.get();
    std::cin.get();

    return 0;
}

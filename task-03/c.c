#include <stdbool.h>
#include <stdio.h>
  
// function check whether a number is prime or not
bool isPrime(int n)
{
    // Corner case
    if (n <= 1)
        return false;
  
    // Check from 2 to n-1
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;
  
    return true;
}
  
// Function to print primes
void printPrime(int n)
{
    for (int i = 2; i <= n; i++)
        if (isPrime(i))
            printf("%d ", i);
}
  
// Driver Code
int main()
{
    int n = 7;
    printPrime(n);
}
  
// This code is contributed by Sania Kumari Gupta
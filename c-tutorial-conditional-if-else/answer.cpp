#include <bits/stdc++.h>
#include <string>

using namespace std;



int main()
{
  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  std:string number;
  if (n == 1) {
    number = "one";
  } else if (n == 2) {
    number = "two";
  } else if (n == 3) {
    number = "three";
  } else if (n == 4) {
    number = "four";
  } else if (n == 5) {
    number = "five";
  } else if (n == 6) {
    number = "six";
  } else if (n == 7) {
    number = "seven";
  } else if (n == 8) {
    number = "eight";
  } else if (n == 9) {
    number = "nine";
  } else if (n > 9) {
    number = "Greater than 9";
  }
  cout << number << endl;

  // Write Your Code Here

  return 0;
}

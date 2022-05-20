# Python Challenges


___
___

## Day 1
___

### Plus-Minus
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#### Note: 
This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

#### Example
    arr = [1,1,0,-1,-1]

There are `n = 5` elements, two positive, two negative and one zero. Their ratios are `2/5 = 0.400000`, `2/5 = 0.400000` and `1/5 = 0.200000`. Results are printed as:

    0.400000
    0.400000
    0.200000

#### Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers

#### Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with `6` digits after the decimal. The function should not return a value.

#### Input Format

The first line contains an integer, `n`, the size of the array.
The second line contains `n` space-separated integers that describe `arr[n]`.

#### Constraints
    0 < n <= 100
    -100 <= arr[i] <= 100

#### Output Format

Print the following `3` lines, each to `6` decimals:

1. proportion of positive values
2. proportion of negative values
3. proportion of zeros

#### Sample Input

    STDIN           Function
    -----           --------
    6               arr[] size n = 6
    -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

#### Sample Output

    0.500000
    0.333333
    0.166667

#### Explanation

There are `3` positive numbers, `2` negative numbers, and `1` zero in the array.
The proportions of occurrence are positive: `3/6 = 0.500000`, negative: `2/6 = 0.333333` and zeros: `1/6 = 0.166667`.

___

### Mini-Max Sum
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#### Example

	arr = [1,3,5,7,9]
The minimum sum is `1+3+5+7=16` and the maximum sum is `3+5+7+9=24`. The function prints

	16 24
#### Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of `5` integers
#### Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of `4` of `5` elements.

#### Input Format

A single line of five space-separated integers.

#### Constraints
	1 <= arr[i] <= 10^9

#### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

#### Sample Input

	1 2 3 4 5

#### Sample Output

	10 14

#### Explanation

The numbers are `1`, `2`, `3`, `4`, and `5`. Calculate the following sums using four of the five integers:

1. Sum everything except `1`, the sum is `2+3+4+5=14`.
2. Sum everything except `2`, the sum is `1+3+4+5=13`.
3. Sum everything except `3`, the sum is `1+2+4+5=12`.
4. Sum everything except `4`, the sum is `1+2+3+5=11`.
5. Sum everything except `5`, the sum is `1+2+3+4=10`.

Hints: Beware of integer overflow! Use 64-bit Integer.
___
### Time conversion

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#### Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#### Example

`s = '12:01:00PM''`
Return '12:01:00'.

`s = '12:01:00AM'`
Return '00:01:00'.

#### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12-hour format
#### Returns

string: the time in 24-hour format
#### Input Format

A single string `s` that represents a time in 12-hour clock format (i.e.: `hh:mm:ssAM` or `hh:mm:ssPM` ).

#### Constraints

All input times are valid
#### Sample Input

    07:05:45PM
#### Sample Output

    19:05:45
___
___

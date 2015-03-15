# WarbyChallenge
Solution to Warby Parker coding challenge completed Summer of 2014. Passed all but one of a grueling series of tests and was recognized as one of the top 5 out of hundreds of submissions. Challenge description below:


#Problem Description

You've been given two lists: the first is a list of patterns, the second is a list of slash-separated paths. Your job is to print, for each path, the pattern which best matches that path. ("Best" is defined more rigorously below, under "Output Format".)

A pattern is a comma-separated sequence of non-empty strings. For a pattern to match a path, each string in the pattern must match exactly the corresponding sub-part of the path. For example, the pattern x,y can only match the path x/y. (Note that leading and trailing slashes in paths should be ignored, so that x/y and /x/y/ are equivalent.)

Patterns can also contain a special string consisting of a single asterisk, which is a wildcard and will match any string in the path. For example, the pattern A,*,B,*,C consists of five fields: three strings and two wildcards. It will successfully match the paths A/foo/B/bar/C and A/123/B/456/C, but not A/B/C, A/foo/bar/B/baz/C, or foo/B/bar/C.

Input Format

The first line contains an integer, N, specifying the number of patterns. The following N lines contain one pattern per line. Each pattern is unique. The next line contains a second integer, M, specifying the number of paths. The following M lines contain one path per line.

Output Format

For each path encountered in the input, print the best-matching pattern. The best-matching pattern is the one which matches the path using the fewest wildcards.

If there is a tie—i.e. if two or more patterns with the same number of wildcards match a path—prefer the pattern whose first wildcard appears furthest to the right. (If two or more patterns' first wildcard appears in the same spot, apply this rule recursively to the remainder of the pattern.)

For example, given the patterns a,*,c,* and a,*,*,d, and the path /a/b/c/d, the best-matching pattern would be a,*,c,*.

If no pattern matches the path, print NO MATCH.

Submission Requirements

You should submit a working program, runnable from a command line, that reads from standard input and prints to standard output. In Unix parlance, it should be runnable like this:

    ./your_program.ext < input_file > output_file

Of course, the actual command line may vary depending on the language you choose; your program file doesn't need to executable on its own, but it should read input directly from stdin.

You may use any programming language in your implementation, though we encourage you to choose one used in the Computer Language Benchmarks Game.

Extra credit: What's the algorithmic complexity of your program? In other words, how does its running time change as the number of patterns or number of paths increases? Would your program complete quickly even when given tens of thousands of patterns and paths? Is there a faster solution? Can you trade memory for reduced execution time? (Hint: although a correct program is sufficient, there is extra credit for an algorithm that's better than sub-quadratic.)

Example Input

6
*,b,*
a,*,*
*,*,c
foo,bar,baz
w,x,*,*
*,x,y,z
5
/w/x/y/z/
a/b/c
foo/
foo/bar/
foo/bar/baz/

Example Output

*,x,y,z
a,*,*
NO MATCH
NO MATCH
foo,bar,baz

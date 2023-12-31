# ChatGPT_Code_Project

## Objective:

_To measure the accuracy of code generated by ChatGPT._

A variety of programming tasks will be selected based on level of difficulty from [LeetCode](https://leetcode.com/). ChatGPT will be prompted to complete these programming tasks in Python. Tests will be created in order to check the accuracy of the code generated by ChatGPT. ChatGPT will be prompted with each programming task three times. In the event of errors being present in the generated code, ChatGPT will be prompted to fix those errors. Three attempts will be made for debugging.

**_Each attempt will be measured by the following metrics:_**

- Did the code run with compilation or runtime errors? _(Yes or No)_
- How many of the three attempts ran successfully? _(0 - 3)_
- Was the output of the code as expected? _(Is there a presence of logical errors? Yes or No)_
- If errors were present, was ChatGPT able to remedy them?
  - How many error remedy attempts we made before success?
    _(if less than or equal to 3)_

## Abstract:

ChatGPT grows in popularity every day.
Standard users and enterprises alike are integrating it into
everyday life and the workplace.
However, with great power comes great responsibility,
and though it may be tempting to ask ChatGPT to write what you may perceive
as a trivial programming problem,
consider the level of trust you are putting into a Large Language Model.

In this paper I explore the results of an experiment conducted in
November of 2023 using ChatGPT (GPT-3.5).
This experiment was performed in order to measure the accuracy of code generated by ChatGPT,
as well as explore ChatGPT’s ability to remedy coding errors that it created.
63 coding programs were generated in total using three difficulty levels,_Easy_, _Medium_ and _Hard_, 7 different coding problems for each difficulty level. The results of this experiment suggest that ChatGPT has a high level of accuracy overall in the code it generates, however its ability to correct its own coding errors may be lacking at the current time.
Also discussed are results and analysis on performance metrics not originally intended in this experiment, but potentially insightful nonetheless.

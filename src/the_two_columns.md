# The Two Columns

The given directory is again a git repository. However, it only gives you a hint if you check the previous commit. The zip name is `exclusive_chall.zip`. As we did in [I'm Committed, or am I?](./im_committed.md), we unzip the git repo and navigate to the required file. 

We need to XOR the two columns one by one to get the required ASCII values of the flag. Here is a simple sheel script to do that.

```py
{{#include ./includes/two_columns.py}}
```

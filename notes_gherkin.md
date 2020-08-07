## what was I doing

* I created data in dexample
* added the option to auto add the 0_ 1_ etc so I don't have to do it manually
* Then I messed with the example.py, and started a function that prints the final sensible paths

This doesn't clean up nicely like before where we found the actual paths for the addresses.

If a word has a double meaning, like V and N, then we get like V V-N for the second word.
Before we were just checking the end point and getting the sequence I think.

But anyhow, this present effort can be turned into a function and added to minicolumn.

It should be fairly easy to get the correct proper paths now.

And with that, we have valid candidates before cutting out the ones that don't match context.

Have fun!

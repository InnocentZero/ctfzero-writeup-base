# Challenge 4

The webpage includes a JavaScript file called `guess2.js`. `guess2.js` is obscured using [JSFuck](https://jsfuck.com/).

The way that JSFuck works is that it constructs a string using fucked-up JavaScript semantics, and then passes it to the [`eval`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) function.

So after all the fucked-up JavaScript expressions are evaluated, you will eventually get something like this:

```js
eval("<your original code>")
```

Those two brackets over there are part of the original JSFuck as-is -- `guess.js` will be some thing like:

```
<some expression that evalutes to eval>(<some expression that evaluates to your code>) 
```

Now there are two ways to do this:

1. You can try to isolate the expression inside those braces -- `guess2.js` ends in a `)`, find the opening `(` for that one (you can use `vim` to do this -- the `%` key on vim matches braces).
2. You can exploit a loophole in how the code is written.

The loophole here is that the code uses [jQuery](https://jquery.com/) (this is the `<script>` included in the the `<head>` of the HTML document), so if you try to `eval` this code in a context where jQuery isn't available (like [an online executor](https://www.programiz.com/javascript/online-compiler/), or [node.js](https://nodejs.org/en)), the debugger will throw an error which contains the code being executed:

![nodejs output](https://i.imgur.com/OhTRJwH.png)

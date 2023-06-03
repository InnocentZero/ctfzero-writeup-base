# Challenge 3

If you inspect the sources, you will see that the webpage loads a `guess.js`, which has the following code:

```js
$(document).ready(function() {
  $("#header-wrap").animate({
      "top": "0"
  }, 1000);

  setTimeout(function() {
    $("#layer3").animate({
        "top": "-100vh"
    }, 2000);
  }, 100);

  setTimeout(function() {
    $("#layer2").animate({
        "top": "-100vh"
    }, 2000);
  }, 500);

  setTimeout(function() {
    $("#layer1").animate({
        "top": "-100vh"
    }, 2000);
  }, 1000);
});

$("#guess-btn").click(function() {
  const jumble = [
    '6f}',   '_s4',
    'c11',   '1da93',
    '1734',  'Zero',
    '{fl4g', 'a29',
    '_0f2',  'ctf',
    'l4d'
  ];

  const mixer = [
    9, 5, 6, 1, 10,
    8, 3, 4, 2,  7,
    0
  ];

  const trueFlag = [];
  const guess = $("#guess-box").val();

  for (let i = 0; i < mixer.length; i++) {
    trueFlag.push(jumble[mixer[i]]);
  }

  if (guess === trueFlag.join("")) {
    $("#result").text("correct. Congratuations!");
  } else {
    $("#result").text("wrong. Try again.");
  }
});
```

The first part is just used for the page animations. The second part is checking your guess and verifying if it's equal to the flag.

You can execute the un-jumbling code separately in your browser's JavaScript cconsole, and see what the final array evaluates to:

![browser console](https://i.imgur.com/WEkG0L7.png)

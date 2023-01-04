

# Vue Redo

Let's redo one of the following Python labs in [Vue](https://github.com/PdxCodeGuild/HB3/blob/main/4%20JavaScript/docs/13%20-%20Vue.md)!

- [Rock, Paper, Scissors](https://github.com/PdxCodeGuild/HB3/blob/main/1%20Python/labs/Rock%20Paper%20Scissors.md)
  - Have the user choose rock, paper, or scissors, and show the user who won.
- [Rot Cipher](https://github.com/PdxCodeGuild/HB3/blob/main/1%20Python/labs/Rot%20Cipher.md)
  - Simple version: the user could just input the word to encode.
  - Complex version: the user could also input the amount to rotate by.
- [Unit Converter](https://github.com/PdxCodeGuild/HB3/blob/main/1%20Python/labs/01%20Unit%20Converter.md)
  - Simple version: the user enters the distance and units and the app shows them the converted distance in meters
  - Complex version: the user also enters output units
- [Random Password Generator](https://github.com/PdxCodeGuild/HB3/blob/main/1%20Python/labs/Random%20Password%20Generator.md)
  - Simple version: the user just enters in the number of characters in the password
  - Complex version: the user enters the number of uppercase letters, lowercase letters, numbers, and special characters
- [Number to Phrase](https://github.com/PdxCodeGuild/HB3/blob/main/1%20Python/labs/02%20Number%20to%20Phrase.md)
  - Have the user enter the number (5) and get back the corresponding word in english (five)


**Vue starter template**
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
    </head>
    <body>
        <div id="app">
            {{ message }}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <script>
            var app = new Vue({
                el: '#app',
                data: {
                    message: 'Hello Vue!'
                },
                methods: {

                },
                created: function() {

                }
            })
        </script>
    </body>
</html>
```

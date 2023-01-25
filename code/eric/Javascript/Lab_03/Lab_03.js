const text = document.getElementById("quote");
const author = document.getElementById("author");
const tweetButton = document.getElementById("tweet");

const getNewQuote = async () => {
    const url = "https://type.fit/api/quotes"; //api for quotes
    const response = await fetch(url);  // fetch the data from the quote api
        console.log(typeof response);
    const allQuotes = await response.json(); //convert the response to json and store it in quotes array
    const indx = Math.floor(Math.random() * allQuotes.length); //generate a random number between 0 and the length of the quotes array
    const quote = allQuotes[indx].text; //store the quote present at the randomly generated index
    const auth = allQuotes[indx].author; //store the author of the respective quote

    //return anonymous for quotes without an author
    if (auth == null) {
        author = "Anonymous";
    }

    //function to dynamically display the quote and the author
    text.innerHTML = '"'+quote+'"';
    author.innerHTML = "~ " + auth;

    //tweet the quote
    window.twttr = (function (d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0],
            t = window.twttr || {};
        if (d.getElementById(id)) return t;
        js = d.createElement(s);
        js.id = id;
        js.src = "https://platform.twitter.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);

        t._e = [];
        t.ready = function (f) {
            t._e.push(f);
        };
        return t;
    }(document, "script", "twitter-wjs"));
    
    tweetButton.href = "https://twitter.com/intent/tweet?text=" + quote + " ~ " + auth;
};
getNewQuote();
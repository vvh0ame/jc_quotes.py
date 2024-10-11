# jc_quotes.js
Web-API for [jcquotes.com](https://www.jcquotes.com) website that gives random james clear quotes

## Example
```JavaScript
async function main() {
	const { JcQuotes } = require("./jc_quotes.js")
	const jcQuotes = new JcQuotes()
	const randomQuote = await jcQuotes.getRandomQuote()
	console.log(randomQuote)
}

main()
```

//set request variable and assign xmlhttprequest object to it
var request = new XMLHttpRequest();

//open new connection, using GET method
request.open('GET', 'https://thesimpsonsquoteapi.glitch.me/quotes', true);

request.onload = function() {
  var data = JSON.parse(this.response);

  //ensure response is successful
  if (request.status >=200 && request.status < 400) {
    data.forEach(quote => {

      //create div set class=card
      const card = document.createElement('div');
      card.setAttribute('class', 'card');

      //create h1 element set text content to character name
      const h2 = document.createElement('h2');
      h2.textContent = quote.character;

      //create p element set text content to quote
      const p = document.createElement('p');
      quote.quote = quote.quote.substring(0,1000); //limit to 100 chars
      p.textContent = quote.quote; //end with ellipses

      //create img element for character image
      const img = document.createElement('img');
      img.setAttribute('src', `${quote.image}`)

      //append cards to the container element
      container.appendChild(card);

      //give each card h1,p & img elements
      card.appendChild(h2);
      card.appendChild(p);
      card.appendChild(img);
    });
  } else {
    console.log('error!!')
  }
}

request.send();

//create main content elements
//div id root set to app
const app = document.getElementById('root');

//create div element and set to container
const container = document.createElement('div');

//set container element class = container
container.setAttribute('class', 'container');

//append container element to app root
app.appendChild(container);

<template>
    <div>
        <div class="box">
            <h1>Question List</h1>
            <h2>Are you looking for fiction of nonfiction?</h2>
                <input type="radio" id="fiction" name="general_topic" value="Fiction">
                <label for="fiction">Fiction</label><br>
                <input type="radio" id="non-fiction" name="general_topic" value="Non-fiction">
                <label for="non-fiction">Non-fiction</label><br>
            <h2>Out of the listed genres, which ones are you looking for?</h2>
            <label v-for="genre in genres" :key="genre">
                <input type="checkbox"  :value="genre">{{ genre }}
            </label>
            <h2>Of the following authors, who's books do you enjoy?</h2>
            <label v-for="author in authors" :key="author">
                <input type="checkbox"  :value="author">{{ author }}
            </label>
            <h2>What is the lenght in pages of the book you would like to read?</h2>
            <select name="length" id="length">
                <option value="AnyLength">Any length</option>
                <option value="200-300">200-300</option>
                <option value="300-400">300-400</option>
                <option value="400+">400+</option>
            </select>
            <h2>From what period of time would you like the book to be from?</h2>
            <select name="period" id="period">
                <option value="AnyPeriod">Any period</option>
                <option value="-1980">-1980</option>
                <option value="1980-1990">1980-1990</option>
                <option value="1990-2000">1990-2000</option>
                <option value="2000-2010">2000-2010</option>
                <option value="2010-2020">2010-2020</option>
                <option value="2020-">2020-</option>
            </select>
            <h2>In what format do you want the book to be in?</h2>
            <select name="format" id="format" >
                    <option value="format" v-for="format in formats" :key="format">{{ format }}</option>
            </select>
            <h2>Pick a language for the book</h2>
            <select name="language" id="language" >
                    <option value="language" v-for="language in languages" :key="language">{{ language }}</option>
            </select>
            <h2>What is your price range?</h2>
            <select name="price" id="price" >
                    <option value="None">None</option>
                    <option value="<10"> &lt; 10</option>
                    <option value="10-20"> 10-20</option>
                    <option value="20-40"> 20-40</option>
                    <option value=">50"> &gt; 50</option>
            </select>

            <button  class="button" type="submit" @click="goToBookPage">Submit</button>
		</div>
    </div>
  </template>
  
  <script>
  import books from '../b2.json'

  export default {
    name: 'Questionnaire',
    data(){
        return{
            genres: [],
            authors:[],
            formats:[],
            languages:[],

        }
    },
    methods: {
      goToBookPage(){
            this.$emit('go-to-book-page')
        }
    },
    mounted() {


        const genreSet = new Set([]);
        const authorSet = new Set([]);
        const formatSet = new Set([]);
        const languageSet = new Set([]);

        for (const bookTitle in books) {
          if (Object.hasOwnProperty.call(books, bookTitle)) {
            const book = books[bookTitle];
            genreSet.add(book.Genre);
            authorSet.add(book.Author);
            formatSet.add(book.Type);
            languageSet.add(book.Language);
        }
        this.genres=genreSet;
        this.authors=authorSet;
        this.formats=formatSet;
        this.languages=languageSet;
}



      

        
  },
    
  };
  

  </script>
  
  <style>

.box {
	padding: 3em 2em ;
    margin: 5em 3em;
	background: #DEB687;
	text-align: left;
	border-radius: 3px 3px 6px 6px;
	border-top-color: #452C0E;

}

.button{
    float: right;
    background-color: #452C0E;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;

}
.button:hover{
    background-color: #4E6C50;

}

  h1 {
    font-size: 36px;
    color: #333;
    margin-bottom: 20px;
  }
  h2{
    color:  #333;
  }
  
  p {
    font-size: 18px;
    color: #666;
    line-height: 1.5;
  }
  </style>
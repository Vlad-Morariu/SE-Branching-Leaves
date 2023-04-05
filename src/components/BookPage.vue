<template>
    <div>
        <div class="box">
            <h1>{{ book.Title }}</h1>
            <p>Description: {{ book.Description }}</p>
            <p>Author: {{ book.Author }}</p>
            <p>Genre: {{ book.Genre }}</p>
            <p>Published Date: {{ book['Published Date'] }}</p>
            <p>Pages: {{ book.Pages }}</p>
            <p>Language: {{ book.Language }}</p>
            <p>Price: {{ book.Price }}</p>
            <p>Type: {{ book.Type }}</p>
            <button class="button" type="back" @click="goToQuestionnaire">Back</button>
         </div>
    </div>
  </template>

  <script>
    import books from '../b2.json'
    export default {
        name: 'BookPage',
        props: {
        BookPageId: {
            type: Number,
            required: true
        }
  },

        data() {
        return {
            book:{},
        };
    },
    methods: {
        goToQuestionnaire(){
            this.$emit('go-to-questionnaire')
        }
    },
    mounted() {
        
        for (const bookTitle in books) {
          if (Object.hasOwnProperty.call(books, bookTitle)) {
            const book = books[bookTitle];
            if (book.ID === this.BookPageId) {
                this.book = book;
            }

          }
        }
  },
  }
  
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
    color: black;
    margin-bottom: 20px;
}
  
p {
    font-size: 18px;
    color: black;
    line-height: 1.5;
}
  </style>
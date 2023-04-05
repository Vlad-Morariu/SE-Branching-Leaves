<template>
  <div  class="wrapper">
    <title>Branching Leaves</title>
	<head>  
		<title>Branching Leaves</title>
		<link rel="shortcut icon" type="image/png" href="../src/assets/tree_logo.png"/>
	</head>
    <div id="header" class="skel-panels-fixed">
						<nav id="nav">
							<ul>
								<li><a href="MainPage.vue">Homepage</a></li>
								<li><a href="#" @click.prevent="page = 'Questionnaire'">Find Books</a></li>
								<li><a href="About.vue">About</a></li>
							</ul>
							<img id="logo" src="../src/assets/tree_logo.png" alt="tree">
						</nav>
						
					</div>
					<div v-if="page ==='Questionnaire'">
					<Questionnaire @go-to-book-page="page = 'BookPage'"/>
					</div>
					<div v-else-if="page ==='BookPage'" :id="'BookPage' + BookPageId">
					<BookPage :BookPageId="BookPageId"  @go-to-questionnaire="page = 'Questionnaire'"/>
					</div>

					
					

  </div>
</template>

<script>
import Questionnaire from './components/Questionnaire.vue'
import BookPage from './components/BookPage.vue'

export default {
  name: 'App',

  components: {
    Questionnaire,
	BookPage
  },
  data(){
	return{
		page:'Questionnaire',
		BookPageId:9
	}
  }
}
</script>

<style>

body {
  margin: 0;
  padding: 0;
  background-image: url('./assets/background_1.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}


.wrapper {
  padding-top: 10em;
	padding-bottom: 4em;
	background-size: cover;
	background-attachment: fixed;
}

#logo{
	float: left;
	width: 10em;
	height: 10em;
}

nav {
  position: absolute;
	right: 0;
	top: 0;
  width: 100%;
	cursor: default;
	display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.2em;

  align-items: center;
  background-color: #452C0E;
  color: #DEB687  ;
  justify-content: space-between
  
}

#nav ul li {
	display: inline-block;
	padding: 1em 1.5em;
	font-size: 1.8em;
	font-weight: bold;
	
}

#nav ul li a {
	-moz-transition: color 0.35s ease-in-out;
	-webkit-transition: color 0.35s ease-in-out;
	-o-transition: color 0.35s ease-in-out;
	-ms-transition: color 0.35s ease-in-out;
	transition: color 0.35s ease-in-out;
	display: inline-block;
	color: #ddd;
	color: rgba(255, 255, 255, 0.75);
	text-decoration: none;
}

#nav ul li a:hover {
	color: #4E6C50;
}

#nav ul li input {
	display: inline-block;
	padding-top: 0.7em;
	padding-bottom: 0.7em;
	
}

</style>

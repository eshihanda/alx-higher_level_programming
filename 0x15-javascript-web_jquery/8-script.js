$(document).ready(function) {
	$.ajax( {
		url: 'https://swapi-api.alx-tools.com/
		    api/people/5/?format=json',
		method:'GET',
		success.function(data) {
			for (const movie of data.results) {
				$('ul#list_movies').append('<li>' +
					movie.title + '</li>');
			});
		});
	});
});

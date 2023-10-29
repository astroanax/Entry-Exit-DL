while(true) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", 'http://127.0.0.1:8000/get_reader_data', false ); // false for synchronous request
	xmlHttp.send( null );
	let rollno = xmlHttp.responseText;
	if (!(rollno === 'None'))
		postMessage(rollno);
	new Promise(r => setTimeout(r, 500));
}

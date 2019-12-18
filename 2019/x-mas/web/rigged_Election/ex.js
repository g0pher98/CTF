function vote (id) {
	var xhttp = new XMLHttpRequest ();
	xhttp.open ("GET", "/vote.php?g=1", false);
	xhttp.send ();
	var work = xhttp.responseText;

	var found = false;
	while (!found) {
		var randomLength = Math.floor (7 + Math.random () * 18);
		var stringGen = generateRandom (randomLength);
		var md5Gen = md5 ("watch__bisqwit__" + stringGen);

		if (md5Gen.substring (0, work.length).localeCompare (work) === 0) {
			var url = "/vote.php?id=" + id + "&h=" + stringGen + "&u=1";
			console.log("vote!!!");
			xhttp.open ("GET", url, false);
			xhttp.send ();
			found = true;
		}
	}
}

for(var i=0; i < 200; i++) {
	console.log(i);
	vote(17565);
}
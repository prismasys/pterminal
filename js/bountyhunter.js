function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function loadCartels()
{

    url = "https://prismaterminal.herokuapp.com/mission/"

    console.log('Loading Cartels M8!')

    cartelraw = httpGet(url)

    var cartel = JSON.parse(cartelraw);
    console.log();

    document.getElementById("cartel-title").innerHTML = cartel['title'];
    document.getElementById("cartel-button").href = cartel['link'];
    document.getElementById("cartel-date").innerHTML = cartel['published'];
    console.log(cartel)

}

function loadCartelsIndex()
{

    url = "https://prismaterminal.herokuapp.com/mission/index/%";

    var jsn = '{"index":%}'


    var index =  document.getElementById("vainaloca").value;

    var jsnt = jsn.replace('%', index)

    query = url.replace('%',jsnt);

    console.log('oh boy im loading that Cartel!');
    console.log(index)

    cartelraw = httpGet(query);

    var cartel = JSON.parse(cartelraw);

    document.getElementById("cartel-title").innerHTML = cartel['title'];
    document.getElementById("cartel-button").href = cartel['link'];
    document.getElementById("cartel-date").innerHTML = cartel['published'];
    console.log(cartel);

}

function loadAllCartels()
{

    url = "https://prismaterminal.herokuapp.com/mission/all/";

    console.log('oh goooosh kiddo, you give hard work today doncha?');


    cartelraw = httpGet(url);

    var cartel = JSON.parse(cartelraw);


    console.log(cartel);

    loadcarteldiv(cartel);

}

function loadcarteldiv(cartel){

    document.getElementById("cartel-list").innerHTML = "";

    for (let k in cartel) {
        console.log(k + ' is ' + cartel[k]['title'])

        var currentDiv = document.getElementById("cartel-list");

        var ptit = document.createElement("h4");
        ptit.innerHTML = cartel[k]['title'];

        var ppub = document.createElement("p");
        ppub.innerHTML = cartel[k]['published'];

        var newDiv = document.createElement("div");
        newDiv.className="w3-panel";

        var hr = document.createElement("hr");

        var a = document.createElement("a");
        a.href = cartel[k]['link'];
        a.id = "cartel-button"
        a.className - "button";
        a.innerHTML = "Claim";



        newDiv.appendChild(ptit);
        newDiv.appendChild(ppub);
        newDiv.appendChild(a);
        newDiv.appendChild(hr);
        currentDiv.appendChild(newDiv);
    }




}
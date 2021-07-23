function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function asyncresquest(url){

    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onload = function (e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          console.log(xhr.responseText);
        } else {
          console.error(xhr.statusText);
        }
      }
    };
    xhr.onerror = function (e) {
      console.error(xhr.statusText);
    };
    xhr.send(null);
}


function refreshADA (){


    apiurl = "https://ada-ai-forecast-sys.herokuapp.com/";

    asyncrefresh(apiurl, 'ada-status')

}

function asyncrefresh (url, idapi){

    document.getElementById(idapi).innerHTML = "🟠";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onload = function (e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          console.log(xhr.responseText);
          document.getElementById(idapi).innerHTML = '🟢';
        } else {
          console.error(xhr.statusText);
          document.getElementById(idapi).innerHTML = '🔴';
        }
      }
    };
    xhr.onerror = function (e) {
      console.error(xhr.statusText);
    };
    xhr.send(null);
}


function refreshsnk (){

    apiurl = "https://sneakers-app-api.herokuapp.com/init/refreshing-motiv";

    asyncrefresh(apiurl, 'snk-status');



}

function refreshbh (){

    apiurl = "https://prismaterminal.herokuapp.com/mission/all/";

    asyncrefresh(apiurl, 'bh-status');


}
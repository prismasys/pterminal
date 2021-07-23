function activatepush(){

    document.getElementById('push-status').innerHTML = "🟠";

    getpushpermission();

    //getworker();

}

function getpushpermission(){

Notification.requestPermission(function(status) {
    console.log('Notification permission status:', status);
});


}
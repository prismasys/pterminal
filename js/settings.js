// THIS CLIENT MUST REQUEST TO https://prismaterminal.herokuapp.com/

navigator.serviceWorker.register('./js/sw.js', {
      scope: './js/'
    });

navigator.serviceWorker.ready
.then(function(registration) {
  console.log('service worker registered');

  return registration.pushManager.getSubscription();
}).then(function(subscription) {
  if (subscription) {
    console.log('Already subscribed', subscription.endpoint);
    setUnsubscribeButton();
  } else {
    setSubscribeButton();
  }
});

function checkperm(){

if (Notification.permission === "granted") {

        document.getElementById('push-status').innerHTML = "🟢";

    } else if (Notification.permission === "blocked") {
        document.getElementById('push-status').innerHTML = "🟠";
     /* the user has previously denied push. Can't reprompt. */
    } else {
    document.getElementById('push-status').innerHTML = "🟠";


    }

}



function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

function asyncsub2(sub){

     // THIS CLIENT MUST REQUEST TO https://prismaterminal.herokuapp.com/

    document.getElementById('push-status').innerHTML = "🟠";

    var tsub = JSON.stringify(sub);

    var ysub = tsub.replace('https://fcm.googleapis.com/fcm/send/','totona')

    var qurl = "https://prismaterminal.herokuapp.com/push/%";

    console.log(tsub);

    var url = qurl.replace('%',ysub);

    //fetch(url, {mode: 'no-cors'})
      //.then(response => response);

    fetch(url)
      .then(response => response.json())
      .then(data => console.log(data));

     console.log('Subscription sended');

     document.getElementById('push-status').innerHTML = "🟢";

}

function asyncsub(sub){

    var tsub = JSON.stringify(sub);

    var qurl = "https://prismaterminal.herokuapp.com/push/%";

    var url = qurl.replace('%',tsub);

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

const publicVapidKey = 'BOHuVL9KC3wF1FsXl9YtqUpx6lJevXJIMYu0DHwdAatsQ2-y2jQny1rM8LXCQyXOS_5rDsUpCy5VP4DemhghWe4';


async function triggerPushNotification() {
    document.getElementById('push-status').innerHTML = "🟠";
  if ('serviceWorker' in navigator) {
    const register = await navigator.serviceWorker.register('./js/sw.js', {
      scope: './js/'
    });

    console.log('waiting for acceptance');
    const subscription = await register.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(publicVapidKey),
    });
    console.log('acceptance complete');
    console.log(subscription);
    asyncsub2(subscription);

  } else {
    console.error('Service workers are not supported in this browser');
  }
}

function activatepush(){

    if (Notification.permission === "granted") {

        document.getElementById('push-status').innerHTML = "🟢";

    } else if (Notification.permission === "blocked") {
        document.getElementById('push-status').innerHTML = "🟠";
     /* the user has previously denied push. Can't reprompt. */
    } else {
    document.getElementById('push-status').innerHTML = "🟠";
      Notification.requestPermission(function(status) {
        console.log('Notification permission status:', status);
        document.getElementById('push-status').innerHTML = "🟢";
    });

    }

}

function subscribeto(){

}
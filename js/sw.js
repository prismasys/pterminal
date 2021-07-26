// client/sw.js

 self.addEventListener('push', event => {
   const data = event.data.json();

   self.registration.showNotification(data.title, {
     body: data.body,
     icon: 'https://prismasys.site/img/prisma-logo.png',
     vibrate: [500, 100, 500],
     data: {
     url: data.url
   }
   });
 });

 self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(
    clients.openWindow(event.notification.data.url)
  );
});

self.addEventListener('pushsubscriptionchange', function(event) {
  console.log('Subscription expired');
  event.waitUntil(
    self.registration.pushManager.subscribe({ userVisibleOnly: true })
    .then(function(subscription) {
      console.log('Subscribed after expiration', subscription.endpoint);
      return fetch('register', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify({
          endpoint: subscription.endpoint
        })
      });
    })
  );
});
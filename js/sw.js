// client/sw.js

 self.addEventListener('push', event => {
   const data = event.data.json();

   self.registration.showNotification(data.title, {
     body: data.body,
     icon: 'https://prismasys.site/img/prisma-logo.png',
     tag:  "push-notification-tag",
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

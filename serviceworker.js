// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/bootstrap.min.css',
    '/static/css/main.css',
    '/static/images/dog.png',
    '/static/images/user.png',
    '/static/images/instagram.png',
    '/static/images/facebook.png',
    '/static/images/carrito.png',
    '/static/images/petworld-black.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});

//codigo para notificaciones push

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyDYgPWad1qxNEBDDRsLo1bXcqjgSs4WDMQ",
  authDomain: "petworld-4cd53.firebaseapp.com",
  projectId: "petworld-4cd53",
  storageBucket: "petworld-4cd53.appspot.com",
  messagingSenderId: "912564427555",
  appId: "1:912564427555:web:4f4ffba5b88f43b30a0a96"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
  let title = payload.notification.title;
  let options ={
    body: payload.notification.body,
    icon: payload.notification.icon
  }
  self.registration.showNotification(title, options);
})

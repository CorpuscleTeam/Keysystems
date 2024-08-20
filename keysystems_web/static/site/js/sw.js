
self.addEventListener('push', function(event) {
    const data = event.data.json();
    console.log('sw data')
    console.log(data)
    self.registration.showNotification(data.title, {
        body: data.body,
        icon: data.icon
    });
});
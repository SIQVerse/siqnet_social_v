const video = document.getElementById('liveVideo');
navigator.mediaDevices.getUserMedia({ video: true, audio: true })
  .then(stream => video.srcObject = stream)
  .catch(err => console.error('Stream error:', err));
